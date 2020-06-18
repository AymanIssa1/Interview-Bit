class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, word):
        word = word.strip()
        result = 0

        for char in word:
            if char == ' ':
                result = 0
            else:
                result += 1

        return result
