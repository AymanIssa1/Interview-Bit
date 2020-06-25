# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSameTree(self, root1, root2):
        if root1 == root2 is None:
            return 1
        elif (not root1 and root2) or (root1 and not root2):
            return 0

        if root1.val != root2.val:
            return 0

        if not self.isSameTree(root1.left, root2.left):
            return 0

        if not self.isSameTree(root1.right, root2.right):
            return 0

        return 1


tree1 = TreeNode(1)
tree1.right = TreeNode(2)
tree1.left = TreeNode(3)

tree2 = TreeNode(1)
tree2.right = TreeNode(2)
tree2.left = TreeNode(4)

x = Solution()
print(x.isSameTree(tree1, tree2))
