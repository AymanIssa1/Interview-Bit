# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, root):
        if not root:
            return root

        current = root
        temp_left = root.left
        temp_right = root.right

        root.left = None
        root.right = self.flatten(temp_left)

        while current.right:
            current = current.right

        current.right = self.flatten(temp_right)

        return root
