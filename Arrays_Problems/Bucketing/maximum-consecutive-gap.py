class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) < 2:
            return 0

        A = sorted(A)

        result = 0

        for i in range(1, len(A)):
            result = max(result, A[i] - A[i - 1])

        return result
