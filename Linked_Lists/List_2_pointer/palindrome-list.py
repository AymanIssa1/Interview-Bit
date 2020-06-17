# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, head):
        l = list()

        current_node = head
        while current_node:
            l.append(current_node.val)
            current_node = current_node.next

        j = len(l) - 1
        for i in range(0, len(l) // 2):
            if l[i] != l[j]:
                return 0
            j -= 1

        return 1
