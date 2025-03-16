# Problem 1: Invert a Binary Tree
# Problem Statement:
# Invert a binary tree (mirror it).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=" ")
        inorderTraversal(root.right)

# Example Usage
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))

print("Original Tree (Inorder):")
inorderTraversal(root)
print("\nInverted Tree (Inorder):")
inorderTraversal(invertTree(root))

# Output
# Original Tree (Inorder):
# 1 2 3 4 6 7 9
# Inverted Tree (Inorder):
# 9 7 6 4 3 2 1


# Explanation
# I recursively invert the left and right subtrees of the current node.
# I swap the left and right children of the current node.   
# The base case is when the current node is None, in which case I return None.
# The time complexity of this solution is O(n) since we visit each node exactly once.
# The space complexity is also O(n) due to the recursive calls on the stack.