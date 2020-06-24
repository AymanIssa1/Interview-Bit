class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        result = [[0 for _ in range(A)] for i in range(A)]

        row_start = 0
        row_end = A
        col_start = 0
        col_end = A

        numbers_max = A * A
        i = 1

        while i <= numbers_max:
            for _ in range(col_start, row_end):
                result[col_start][_] = i
                i += 1

            row_start += 1
            if i > numbers_max:
                break

            for _ in range(row_start, col_end):
                result[_][col_end - 1] = i
                i += 1

            col_end -= 1
            if i > numbers_max:
                break

            for _ in range(col_end - 1, col_start - 1, -1):
                result[row_end - 1][_] = i
                i += 1

            row_end -= 1
            if i > numbers_max:
                break

            for _ in range(row_end - 1, row_start - 1, -1):
                result[_][row_start - 1] = i
                i += 1

            col_start += 1
            if i > numbers_max:
                break

        return result


x = Solution.generateMatrix('', 4)
for _ in x:
    print(_)
