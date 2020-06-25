# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, root):
        if not root:
            return root

        result = []
        stack = [root]

        while len(stack) > 0:
            current_node = stack.pop()
            result.append(current_node.val)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

        return result

    def preorderTraversal(self, root):
        array = []
        self.preOrderTraversalHelper(root, array)
        return array

    def preOrderTraversalHelper(self, root, array):
        array.append(root.val)

        if root.left is not None:
            self.preOrderTraversalHelper(root.left, array)

        if root.right is not None:
            self.preOrderTraversalHelper(root.right, array)
