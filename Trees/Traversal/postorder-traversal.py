# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, root):
        result = []

        stack = [root]
        while len(stack) != 0:
            current_node = stack.pop()
            result.append(current_node.val)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)

        return result[::-1]

    # Recursion
    def postorderTraversal2(self, root):
        array = []
        self.postorderTraversalHelper(root, array)
        return array

    def postorderTraversalHelper(self, root, array):
        if root.left is not None:
            self.postorderTraversalHelper(root.left, array)

        if root.right is not None:
            self.postorderTraversalHelper(root.right, array)

        array.append(root.val)


root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

print(Solution.postorderTraversal('', root))
