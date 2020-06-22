class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        s = set(A)
        for i in range(1, len(A) + 1):
            if i not in s:
                return i

        return len(A) + 1


print(Solution.firstMissingPositive('', [1]))
print(Solution.firstMissingPositive('', [1, 2, 0]))
print(Solution.firstMissingPositive('', [3, 4, -1, 1]))
print(Solution.firstMissingPositive('', [-8, -7, -6]))
