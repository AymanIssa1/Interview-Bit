# https://www.interviewbit.com/problems/swap-list-nodes-in-pairs/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        dummy_head = ListNode(-1)
        current_node = dummy_head
        current_node.next = head

        while current_node.next and current_node.next.next:
            post = current_node.next.next.next
            last = current_node.next

            current_node.next.next.next = current_node.next
            current_node.next = current_node.next.next
            last.next = post

            current_node = last
        return dummy_head.next
