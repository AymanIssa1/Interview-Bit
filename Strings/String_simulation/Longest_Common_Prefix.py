class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        index = 0
        result = ''

        while index < len(A[0]):
            current_char = A[0][index]
            should_add_char = True
            for i in range(1, len(A)):
                if index >= len(A[i]) or current_char != A[i][index]:
                    should_add_char = False
                    break

            if should_add_char:
                result += current_char
                index += 1
            else:
                break

        return result


print(Solution.longestCommonPrefix(None, ["flower", "flow", "flight"]))
print(Solution.longestCommonPrefix(None, ["abab", "ab", "abcd"]))
print(Solution.longestCommonPrefix(None, ["dog", "racecar", "car"]))
print(Solution.longestCommonPrefix(None, ["aaaaaaaaaaaaaaaaaaaaaaa",
                                          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                          "aaaaaaaaaaaaaaaaaaaaaaaaaa",
                                          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaa",
                                          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                          "aaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                          "aaaaaaaaaaaaaaaaaaaaaa",
                                          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]))
