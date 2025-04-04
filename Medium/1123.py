from typing import Optional

# Assuming TreeNode is defined elsewhere as:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return None, 0

            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)

            if left_depth > right_depth:
                return left_lca, left_depth + 1
            if left_depth < right_depth:
                return right_lca, right_depth + 1

            return node, left_depth + 1

        return dfs(root)[0]

# Example Usage (assuming TreeNode is defined):
def create_tree(values):
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    root = nodes[0]
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        node = queue.pop(0)
        if node:
            if i < len(nodes):
                node.left = nodes[i]
                i += 1
            if i < len(nodes):
                node.right = nodes[i]
                i += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return root

if __name__ == "__main__":
    # Test case 1
    root1 = create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    sol = Solution()
    result1 = sol.lcaDeepestLeaves(root1)
    print(f"LCA of deepest leaves: {result1.val if result1 else None}")  # Expected: 4

    # Test case 2
    root2 = create_tree([1])
    result2 = sol.lcaDeepestLeaves(root2)
    print(f"LCA of deepest leaves: {result2.val if result2 else None}")  # Expected: 1

    # Test case 3
    root3 = create_tree([0, 1, 3, None, 2])
    result3 = sol.lcaDeepestLeaves(root3)
    print(f"LCA of deepest leaves: {result3.val if result3 else None}") # Expected: 2

    # Test case 4
    root4 = create_tree([3,5,1,6,2,0,8,None,None,7,4,None,None,None,None,None,None,None,None,None,None])
    result4 = sol.lcaDeepestLeaves(root4)
    print(f"LCA of deepest leaves: {result4.val if result4 else None}") # Expected: 4