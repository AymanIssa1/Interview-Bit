# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, root):
        if not root:
            return root

        result = []
        stack = []
        current_node = root
        while len(stack) != 0 and current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                result.append(current_node.val)
                current_node = current_node.right

        return result

    # Recursion
    def inorderTraversal2(self, root):
        array = []
        self.inOrderTraversalHelper(root, array)
        return array

    def inOrderTraversalHelper(self, root, array):
        if root.left is not None:
            self.inOrderTraversalHelper(root.left, array)

        array.append(root.val)

        if root.right is not None:
            self.inOrderTraversalHelper(root.right, array)
