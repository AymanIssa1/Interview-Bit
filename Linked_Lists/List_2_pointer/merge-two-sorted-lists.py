# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A is None:
            return B
        if B is None:
            return A

        current_A = A
        current_B = B

        head = None
        tail = None

        while current_A is not None and current_B is not None:
            if current_A.val <= current_B.val:
                if head is None and tail is None:
                    head = ListNode(current_A.val)
                    tail = head
                else:
                    tail.next = ListNode(current_A.val)
                    tail = tail.next
                current_A = current_A.next
            elif current_B.val <= current_A.val:
                if head is None and tail is None:
                    head = ListNode(current_B.val)
                    tail = head
                else:
                    tail.next = ListNode(current_B.val)
                    tail = tail.next
                current_B = current_B.next

        if current_A is not None:
            while current_A is not None:
                tail.next = ListNode(current_A.val)
                tail = tail.next
                current_A = current_A.next

        if current_B is not None:
            while current_B is not None:
                tail.next = ListNode(current_B.val)
                tail = tail.next
                current_B = current_B.next

        return head
