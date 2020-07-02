# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, head):
        if not head and not head.next:
            return head

        current_node = head

        while current_node:
            pointer = head
            while pointer != current_node:
                if pointer.val > current_node.val:
                    temp = current_node.val
                    current_node.val = pointer.val
                    pointer.val = temp
                else:
                    pointer = pointer.next

            current_node = current_node.next

        return head
