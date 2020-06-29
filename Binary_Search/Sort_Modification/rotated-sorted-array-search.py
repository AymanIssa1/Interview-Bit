class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left < right:
            middle = left + (right - left) // 2
            if arr[middle] > arr[right]:
                left = middle + 1
            else:
                right = middle

        start = left
        left = 0
        right = len(arr) - 1

        if arr[start] <= target <= arr[right]:
            left = start
        else:
            right = start

        while left <= right:
            middle = left + (right - left) // 2

            if arr[middle] == target:
                return middle

            if arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1


print(Solution.search('', [4, 5, 6, 7, 0, 1, 2, 3], 6))
print(Solution.search('',
                      [192, 194, 197, 198, 199, 200, 201, 203, 204, 2, 3, 4, 7, 9, 10, 11, 14, 15, 16, 17, 20, 21, 22,
                       23, 24, 25, 26, 27, 28, 29, 30, 33, 34, 35, 36, 39, 40, 42, 43, 46, 47, 50, 51, 52, 53, 55, 57,
                       59, 60, 64, 66, 68, 70, 71, 72, 75, 76, 78, 85, 86, 87, 91, 92, 94, 95, 96, 99, 102, 105, 106,
                       107, 109, 111, 113, 114, 115, 119, 120, 121, 123, 125, 129, 130, 131, 133, 134, 137, 138, 139,
                       140, 141, 142, 143, 145, 146, 149, 151, 152, 156, 160, 161, 165, 167, 168, 170, 171, 176, 177,
                       178, 179, 180, 181, 182, 185, 186, 190], 70))
