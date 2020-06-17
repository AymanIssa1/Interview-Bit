# https://www.interviewbit.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head : head node of linked list
    # @param k : integer
    # @return the head node in the linked list
    def rotateRight(self, head, k):
        current = head
        size = 1
        while current.next:
            size += 1
            current = current.next

        current.next = head

        count = size - (k % size)
        for _ in range(0, count):
            current = current.next

        new_head = current.next
        current.next = None

        return new_head
