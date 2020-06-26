# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, root, sum):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1 if root.val == sum else 0

        return self.hasPathSum(root.right, sum - root.val) or self.hasPathSum(root.left, sum - root.val)
