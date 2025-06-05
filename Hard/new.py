class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque

def build_tree(nodes):
    if not nodes or nodes[0] == "null":
        return None

    root = TreeNode(int(nodes[0]))
    q = deque([root])
    i = 1

    while q and i < len(nodes):
        current = q.popleft()

        # Left child
        if nodes[i] != "null":
            current.left = TreeNode(int(nodes[i]))
            q.append(current.left)
        i += 1
        if i >= len(nodes):
            break

        # Right child
        if nodes[i] != "null":
            current.right = TreeNode(int(nodes[i]))
            q.append(current.right)
        i += 1

    return root

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# -------- Main Execution --------
if __name__ == "__main__":
    user_input = input("Enter tree nodes in level-order (use 'null' for missing nodes, space-separated): ")
    node_values = user_input.strip().split()
    root = build_tree(node_values)
    print("Inorder Traversal of Tree:", inorder_traversal(root))
