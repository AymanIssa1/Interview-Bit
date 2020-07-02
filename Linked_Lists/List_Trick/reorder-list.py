# https://www.interviewbit.com/problems/reorder-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, head):
        if not head or not head.next:
            return head

        temp = slow = fast = head

        stack = []
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next

        left_side = head
        right_side = slow
        temp.next = None  # to split the linkedlist into 2 halves
        while right_side:
            stack.append(right_side)
            right_side = right_side.next

        while len(stack) != 0 and left_side:
            temp = left_side.next
            left_side.next = stack.pop()
            left_side = left_side.next
            left_side.next = None
            left_side.next = temp
            left_side = left_side.next

        if len(stack) == 1:
            last_element = stack.pop()
            last_element.next = None
            current_node = head
            while current_node.next:
                current_node = current_node.next
            current_node.next = last_element

        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = Solution.reorderList('', head)

while head:
    print(head.val)
    head = head.next
