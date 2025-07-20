import collections
from typing import List, Dict

class TrieNode:
  def __init__(self):
    self.children: Dict[str, 'TrieNode'] = {}
    self.deleted = False

class Solution:
  def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
    ans = []
    root = TrieNode()
    # Stores a mapping from a subtree's unique string representation to a list of TrieNodes
    # that are roots of such subtrees.
    subtreeToNodes: Dict[str, List[TrieNode]] = collections.defaultdict(list)

    # Construct the Trie by inserting all paths.
    # Sorting paths ensures a consistent order of insertion for identical subtrees
    # (though not strictly necessary for correctness, it can help with debugging/predictability).
    for path in sorted(paths):
      node = root
      for s in path:
        # If a child for 's' doesn't exist, create it.
        node = node.children.setdefault(s, TrieNode())

    # Recursively build a unique string representation for each subtree
    # and populate the `subtreeToNodes` dictionary.
    def buildSubtreeToRoots(node: TrieNode) -> str:
      # Build the subtree string: (child1_name + child1_subtree_string)(child2_name + child2_subtree_string)...
      # The '()' for an empty subtree is important to distinguish it.
      # Children are sorted by name to ensure a consistent subtree string for identical subtrees.
      subtree = '(' + ''.join(s + buildSubtreeToRoots(node.children[s])
                              for s in sorted(node.children.keys())) + ')'
      
      # Only consider non-empty subtrees for duplication detection.
      # An empty subtree '()' would be the representation of a leaf node.
      if subtree != '()':
        subtreeToNodes[subtree].append(node) # Add the current node as a root of this subtree type
      return subtree

    # Start building subtree representations from the root of the main Trie.
    buildSubtreeToRoots(root)

    # Mark nodes that represent duplicate subtrees as deleted.
    for nodes in subtreeToNodes.values():
      # If more than one node has the exact same subtree representation, they are duplicates.
      if len(nodes) > 1:
        for node in nodes:
          node.deleted = True # Mark all such duplicate roots for deletion.

    # Reconstruct the paths that are not marked for deletion.
    def constructPath(node: TrieNode, current_path: List[str]) -> None:
      # Iterate through children, ensuring consistent order by sorting keys.
      for s, child in sorted(node.children.items()):
        # If the child node itself is not marked for deletion,
        # recursively continue building the path.
        if not child.deleted:
          constructPath(child, current_path + [s])
      
      # If the current_path is not empty, it means we have reached a valid folder path
      # (either a leaf or a folder whose children are all valid).
      if current_path:
        ans.append(current_path)

    # Start path construction from the root with an empty initial path.
    constructPath(root, [])
    return ans

def get_paths_input() -> List[List[str]]:
    paths_input = []
    print("Enter each folder path as space-separated names (e.g., 'a b c').")
    print("Type 'done' and press Enter when you have finished entering all paths.")
    
    while True:
        line = input("Enter path (or 'done'): ").strip()
        if line.lower() == 'done':
            break
        if not line:
            print("Empty path entered. Please enter folder names or 'done'.")
            continue
        
        path_components = line.split()
        if not path_components:
            print("Path must contain at least one folder name. Please re-enter.")
            continue
        
        paths_input.append(path_components)
    return paths_input

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Delete Duplicate Folders ---")
    
    user_paths = get_paths_input()
    
    if not user_paths:
        print("No paths entered. Result: []")
    else:
        result = sol.deleteDuplicateFolder(user_paths)
        print("\nOriginal paths entered:")
        for p in user_paths:
            print(f"  /{'/'.join(p)}")
        print("\nPaths after deleting duplicate subfolders:")
        for p in result:
            print(f"  /{'/'.join(p)}")