class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        result = 0
        n = len(A)
        for i in range(0, n):
            char_value = ord(A[i]) - ord('A') + 1
            result += (pow(26, n - i - 1)) * char_value

        return result
