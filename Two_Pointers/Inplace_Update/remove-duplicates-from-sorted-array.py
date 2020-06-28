class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 1
        j = 0
        length = len(A)
        while i < length:
            if A[i] != A[j]:
                A[j + 1] = A[i]
                j += 1

            i += 1

        del A[j + 1:]
        return len(A)
