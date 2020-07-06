# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, root, target):
        found = self.t2SumHelper(root, target)
        if found:
            return 1
        return 0

    def t2SumHelper(self, root, target):
        if not root:
            return False

        if (root.right and root.val + root.right.val == target) or (root.left and root.val + root.left.val == target):
            return True

        return self.t2Sum(root.right, target) or self.t2Sum(root.left, target)


root = TreeNode(7)
root.left = TreeNode(14)
root.right = TreeNode(1)
root.left.left = TreeNode(20)

print(Solution.t2Sum('', root, 21))
