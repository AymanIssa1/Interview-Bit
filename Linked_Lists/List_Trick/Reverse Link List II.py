# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        dummy = ListNode(-1)
        dummy.next = A
        headB = dummy
        headC = dummy

        for _ in range(1, B + 1):
            headB = headB.next

        for _ in range(1, C + 1):
            headC = headC.next

        stack = []
        node = headB

        for _ in range(0, C - B + 1):
            stack.append(node)
            node = node.next

        head = dummy
        tail = headC.next
        for _ in range(1, B):
            head = head.next

        while len(stack) != 0:
            head.next = stack.pop()
            head = head.next

        head.next = tail

        return dummy.next


# testing
A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)

solution = Solution.reverseBetween(None, A, 1, 2)
s = ""
while solution:
    s += str(solution.val) + " -> "
    solution = solution.next

print(s)
