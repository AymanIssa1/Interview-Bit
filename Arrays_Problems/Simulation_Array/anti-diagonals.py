class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        N = len(A)

        result = []

        for i in range(0, N):
            x = 0
            y = i
            arr = []
            for j in range(0, i + 1):
                arr.append(A[x][y])
                x += 1
                y -= 1
            result.append(arr)

        result2 = []
        for i in range(N - 1, 0, -1):
            x = N - 1
            y = i
            arr = []
            while y < N:
                arr.append(A[x][y])
                x -= 1
                y += 1
            arr.reverse()
            result2.append(arr)

        result2.reverse()
        for arr in result2:
            result.append(arr)

        return result


print(Solution.diagonal('', [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
