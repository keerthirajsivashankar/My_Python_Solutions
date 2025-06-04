from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root):
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def postorder(self, root):
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]

def build_tree(values):
    if not values or values[0] == 'None':
        return None
    
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        current = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] != 'None':
            current.left = TreeNode(int(values[i]))
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] != 'None':
            current.right = TreeNode(int(values[i]))
            queue.append(current.right)
        i += 1
    
    return root

# Taking input from user
print("Enter tree nodes in level order (space separated), use 'None' for no node:")
user_input = input().strip().split()

root = build_tree(user_input)
sol = Solution()

print("Preorder traversal:", sol.preorder(root))
print("Inorder traversal:", sol.inorder(root))
print("Postorder traversal:", sol.postorder(root))
