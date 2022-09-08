class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        index = 0
        while index != n:
            if A[index] == 0:
                del A[index]
                A.append(0)
                n -= 1
            else:
                index += 1

        return A


A = [0, 0, 9, 4, 0, 10, 3, 8, 6, 2, 6]
print(Solution.solve(None, A))
