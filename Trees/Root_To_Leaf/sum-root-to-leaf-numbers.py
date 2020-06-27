# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, root):
        result = []
        self.getPaths(root, 0, result)
        return sum(result) % 1003

    def getPaths(self, root, value, result):
        if root:
            value = (value * 10) + root.val

        if not root.right and not root.left:
            result.append(value)

        if root.left:
            self.getPaths(root.left, value, result)

        if root.right:
            self.getPaths(root.right, value, result)
