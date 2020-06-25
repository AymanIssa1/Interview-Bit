# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, root):
        array = []
        self.inOrderTraversalHelper(root, array)
        return array

    def inOrderTraversalHelper(self, root, array):
        if root.left is not None:
            self.inOrderTraversalHelper(root.left, array)

        array.append(root.val)

        if root.right is not None:
            self.inOrderTraversalHelper(root.right, array)
