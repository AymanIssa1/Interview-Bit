# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param A : head node of linked list
# @return the head node in the linked list
def deleteDuplicates(A):
    if A is None or A.next is None:
        return A

    current_node = A

    while current_node.next is not None:
        if current_node.val == current_node.next.val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

    return A


# time exceeded
def deleteDuplicates2(A):
    if A is None or A.next is None:
        return A

    l = list()

    previous_node = A
    current_node = A.next

    while current_node is not None and previous_node is not None:
        if current_node.val not in l:
            l.append(current_node.val)

            if previous_node.val == current_node.val:
                previous_node.next = previous_node.next.next
                current_node = current_node.next
            else:
                previous_node = previous_node.next
                current_node = current_node.next

        else:
            previous_node.next = previous_node.next.next
            current_node = current_node.next

    return A
