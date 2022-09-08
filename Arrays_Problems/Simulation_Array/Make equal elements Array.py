class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for outerIndex in range(0, len(A)):
            val = A[outerIndex]
            for innerIndex in range(0, len(A)):
                if outerIndex == innerIndex:
                    continue

                if (val == A[innerIndex]) or (val < A[innerIndex] and val == A[innerIndex] - B) or (
                        val > A[innerIndex] and val == A[innerIndex] + B):
                    if innerIndex == len(A) - 1:
                        return 1
                    continue
                else:
                    break

        return 0


A = [3, 2, 3, 3, 1, 2, 3, 2, 2, 1, 2, 2, 1, 3, 2, 3, 2, 2, 1, 2, 1, 1, 1, 1, 1, 3, 3, 1, 1, 3, 3, 3, 2, 3, 2]
B = 2
print(Solution.solve(None, A, B))
