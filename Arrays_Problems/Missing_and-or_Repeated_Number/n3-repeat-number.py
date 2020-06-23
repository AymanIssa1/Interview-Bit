class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        if len(A) == 1:
            return A[0]

        expected_length = len(A) // 3
        d = dict()

        for element in A:
            if element in d:
                val = d[element]
                if val >= expected_length:
                    return element
                d[element] = val + 1
            else:
                d[element] = 1

        return -1


print(Solution.repeatedNumber('', [1]))
print(Solution.repeatedNumber('', [1, 2, 3, 1, 1]))
print(Solution.repeatedNumber('', [1000441, 1000441, 1000994]))
