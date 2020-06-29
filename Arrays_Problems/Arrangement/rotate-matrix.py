class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, matrix):
        N = len(matrix)

        for x in range(0, int(N / 2)):
            for y in range(x, N - 1 - x):
                # store top-left cell value
                temp = matrix[x][y]

                matrix[x][y] = matrix[N - 1 - y][x]

                matrix[N - 1 - y][x] = matrix[N - 1 - x][N - 1 - y]

                matrix[N - 1 - x][N - 1 - y] = matrix[y][N - 1 - x]

                matrix[y][N - 1 - x] = temp

        return matrix
