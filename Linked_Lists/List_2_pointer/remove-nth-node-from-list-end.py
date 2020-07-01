# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, head, k):
        dummy_head = ListNode(0)
        dummy_head.next = head

        slow_runner = dummy_head
        fast_runner = dummy_head

        i = 0
        while i <= k and fast_runner:
            fast_runner = fast_runner.next
            i += 1

        if not fast_runner:
            dummy_head.next = dummy_head.next.next
            return dummy_head.next

        while fast_runner:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next

        slow_runner.next = slow_runner.next.next
        return dummy_head.next
