class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []

        for item in A:
            if item == "(":
                stack.append(item)
            elif item == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return 0

        if len(stack) == 0:
            return 1
        else:
            return 0
