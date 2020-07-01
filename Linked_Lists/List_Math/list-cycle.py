# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, head):
        elements = set()

        current = head
        while current:
            if current in elements:
                return current
            elements.add(current)
            current = current.next

        return None
