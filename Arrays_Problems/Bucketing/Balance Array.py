class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        specialElementsCount = 0
        for outerIndex in range(0, len(A)):
            oddCount = 0
            evenCount = 0
            isEven = False

            for innerIndex in range(0, len(A)):
                if outerIndex == innerIndex:
                    continue
                elif isEven:
                    evenCount += A[innerIndex]
                    isEven = False
                else:
                    oddCount += A[innerIndex]
                    isEven = True

            if oddCount == evenCount:
                specialElementsCount += 1

        return specialElementsCount


print(Solution.solve(None, [2, 1, 6, 4]))
print(Solution.solve(None, [5, 5, 2, 5, 8]))
print(Solution.solve(None, [2, 8, 2, 2, 6, 3]))
