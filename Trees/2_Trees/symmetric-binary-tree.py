# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, root):
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, root1, root2):
        if root1 == root2 is None:
            return 1
        elif (not root1 and root2) or (root1 and not root2):
            return 0

        if root1.val != root2.val:
            return 0

        if not self.isSymmetricHelper(root1.left, root2.right):
            return 0

        if not self.isSymmetricHelper(root1.right, root2.left):
            return 0

        return 1


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.left = TreeNode(2)

tree.right.right = TreeNode(3)
tree.right.left = TreeNode(4)

tree.left.right = TreeNode(4)
# tree.left.left = TreeNode(3)

x = Solution()
print(x.isSymmetric(tree))
