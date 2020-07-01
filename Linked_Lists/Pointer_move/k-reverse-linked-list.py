# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, head, k):
        current = head
        new_head = None
        last_node = head
        while current:
            previous = None
            next = None
            current_last = current
            for i in range(0, k):
                next = current.next
                current.next = previous
                previous = current
                current = next
            if not new_head:
                new_head = previous
            else:
                last_node.next = previous
            last_node = current_last

        return new_head
