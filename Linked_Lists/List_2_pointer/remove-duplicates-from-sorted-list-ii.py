# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A is None or A.next is None:
            return A

        dummy_head = ListNode(None)
        dummy_head.next = A
        pre = dummy_head

        while pre.next:
            node = pre.next
            while node.next and node.val == node.next.val:
                node = node.next

            if node != pre.next:
                pre.next = node.next
            else:
                pre = node

        return dummy_head.next
