class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []

        for item in A:
            if item in ('(', '-', '+', '/', '*'):
                stack.append(item)
            elif item == ")":
                latestItem = stack.pop()
                if latestItem == "(":
                    return 1
                else:
                    while True:
                        if stack.pop() in ('-', '+', '/', '*'):
                            continue
                        else:
                            break

        return 0
