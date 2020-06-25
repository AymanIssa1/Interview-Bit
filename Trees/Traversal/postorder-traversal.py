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

        stack = []
        stack.append(root)
        while len(stack) != 0:
            current_node = stack[len(stack) - 1]  # peek
            if current_node.left and current_node.left.val not in result:
                stack.append(current_node.left)
            elif current_node.right and current_node.right.val not in result:
                stack.append(current_node.right)
            else:
                result.append(current_node.val)
                stack.pop()

        return result

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
