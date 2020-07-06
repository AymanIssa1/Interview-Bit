class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, arr, start, end):
        continuous_subsequence = 0

        for i in range(0, len(arr)):
            sum = 0
            for j in range(i, len(arr)):
                sum += arr[j]
                if start <= sum <= end:
                    continuous_subsequence += 1
                elif sum > end:
                    break

        return continuous_subsequence


print(Solution.numRange('', [1], 0, 0))
print(Solution.numRange('', [80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90], 99,
                        269))
