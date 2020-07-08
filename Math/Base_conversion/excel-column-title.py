class Solution:
    # @param A : string
    # @return an integer
    def convertToTitle(self, A):
        result = ''
        while A != 0:
            A -= 1
            char_value = (A % 26) + 65
            result = chr(char_value) + result
            A = A // 26

        return result
