class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        length = len(A)
        for i in range(length):
            if A[:length - i] == A[length - i - 1::-1]:
                return i
        return length
