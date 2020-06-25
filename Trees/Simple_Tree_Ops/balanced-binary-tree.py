# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, root):
        res = self.isBalancedHelper(root, 0)
        if res == float('inf'):
            return 0
        else:
            return 1

    def isBalancedHelper(self, root, depth):
        if not root:
            return depth

        rightDepth = self.isBalancedHelper(root.right, depth + 1)
        leftDepth = self.isBalancedHelper(root.left, depth + 1)

        if abs(rightDepth - leftDepth) > 1:
            return float('inf')
        else:
            return max(rightDepth, leftDepth)
