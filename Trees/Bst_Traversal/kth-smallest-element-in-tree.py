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
    def kthsmallest(self, root, k):
        arr = self.convertTreeToArray(root, [])

        arr.sort()

        return arr[k - 1]

    def convertTreeToArray(self, root, array):

        if root.left:
            self.convertTreeToArray(root.left, array)

        array.append(root.val)

        if root.right:
            self.convertTreeToArray(root.right, array)

        return array
