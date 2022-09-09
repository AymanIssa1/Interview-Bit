# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        stack = []
        len = 0
        node = A

        while node:
            stack.append(node.val)
            len += 1
            node = node.next

        requestElementIndex = int(len / 2) - B

        if requestElementIndex < 0:
            return -1

        return stack[requestElementIndex]
