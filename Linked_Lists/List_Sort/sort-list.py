# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def bubbleSort(self, head):
        dummy_head = ListNode(-1)
        dummy_head.next = head

        length = 0
        counter_node = dummy_head.next
        while counter_node:
            length += 1
            counter_node = counter_node.next

        for i in range(0, length):
            prev = dummy_head
            for j in range(i, length):
                current = prev.next
                post = current.next
                if post and current.val > post.val:
                    current.next = post.next
                    post.next = current
                    prev.next = post

                prev = prev.next

        return dummy_head.next
