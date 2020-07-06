class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')

        min1 = float('inf')
        min2 = float('inf')

        for i in range(0, len(A)):
            if A[i] > max1:
                max3 = max2
                max2 = max1
                max1 = A[i]
            elif A[i] > max2:
                max3 = max2
                max2 = A[i]
            elif A[i] > max3:
                max3 = A[i]

            if A[i] < min1:
                min2 = min1
                min1 = A[i]
            elif A[i] < min2:
                min2 = A[i]

        return max((max1 * max2 * max3), (max1 * min1 * min2))
