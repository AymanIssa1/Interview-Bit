class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        x_length = len(A)
        y_length = len(A[0])

        zeros_x_indices = set()
        zeros_y_indices = set()

        for x in range(0, x_length):
            for y in range(0, y_length):
                if A[x][y] == 0:
                    zeros_x_indices.add(x)
                    zeros_y_indices.add(y)

        for x in zeros_x_indices:
            for i in range(0, y_length):
                A[x][i] = 0

        for y in zeros_y_indices:
            for i in range(0, x_length):
                A[i][y] = 0

        return A
