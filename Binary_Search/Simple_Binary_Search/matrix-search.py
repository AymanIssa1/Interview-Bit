class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, matrix, target):
        for row in matrix:
            start = 0
            end = len(row)
            while start < end:
                middle = (start + end) // 2
                if row[middle] == target:
                    return 1

                if target > row[middle]:
                    start = middle + 1
                else:
                    end = middle

        return 0


print(Solution.searchMatrix('', [[1]], 1))
print(Solution.searchMatrix('', [
    [3, 3, 11, 12, 14],
    [16, 17, 30, 34, 35],
    [45, 48, 49, 50, 52],
    [56, 59, 63, 63, 65],
    [67, 71, 72, 73, 79],
    [80, 84, 85, 85, 88],
    [88, 91, 92, 93, 94],
], 94))
