class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        index = 0
        for i in range(0, len(A)):
            if index < 2 or A[i] != A[index - 2]:
                A[index] = A[i]
                index += 1

        del A[index:]
        return index


print(Solution.removeDuplicates('', [1, 1, 1, 2]))
print(Solution.removeDuplicates('',
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
                                 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
