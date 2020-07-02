# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, head):
        if head or head.next:
            return head

        temp = head
        slow = head
        fast = head

        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next

        temp.next = None

        left_side = self.sortList(head)
        right_side = self.sortList(slow)

        return self.merge(left_side, right_side)

    def merge(self, left_side, right_side):
        sorted_temp = ListNode(0)
        current_node = sorted_temp

        while left_side and right_side:
            if left_side.val < right_side.val:
                current_node.next = left_side
                left_side = left_side.next
            else:
                current_node.next = right_side
                right_side = right_side.next

            current_node = current_node.next

        while right_side:
            current_node.next = right_side
            right_side = right_side.next
            current_node = current_node.next

        while left_side:
            current_node.next = left_side
            left_side = left_side.next
            current_node = current_node.next

        return sorted_temp.next

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


head = ListNode(10)
head.next = ListNode(4)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)

head = Solution.bubbleSort('', head)

while head:
    print(head.val)
    head = head.next
