class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        words = A.split(' ')

        result = ''

        for word in words[::-1]:
            result += word + ' '

        return result.strip()


print(Solution.solve('', "the sky is blue"))
