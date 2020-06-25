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
        result = []

        stack = []
        stack.append(root)
        while len(stack) != 0:
            current_node = stack[len(stack) - 1]  # peek
            if current_node.val not in result:
                result.append(current_node.val)

            if current_node.left and current_node.left.val not in result:
                stack.append(current_node.left)
            elif current_node.right and current_node.right.val not in result:
                stack.append(current_node.right)
            else:
                stack.pop()

        return result
