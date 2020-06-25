# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, root):
        if not root:
            return float('inf')
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
