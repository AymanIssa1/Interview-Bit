# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, root, sum):
        result = []
        self.getPaths(root, [], sum, result)
        return result

    def getPaths(self, root, arr, sum, result):
        if root:
            arr.append(root.val)

        if not root.right and not root.left:
            if root.val == sum:
                result.append(arr)

        if root.right:
            self.getPaths(root.right, arr[:], sum - root.val, result)

        if root.left:
            self.getPaths(root.left, arr[:], sum - root.val, result)

        return result
