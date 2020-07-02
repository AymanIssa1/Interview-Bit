class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, n):
        result = []

        for i in range(0, n):
            if i == 0:
                result.append([1])
            else:
                val = i + 1
                for j in range(0, len(result)):
                    result[j] = [val] + result[j] + [val]

                row_length = len(result[0])
                generate_row = [val for _ in range(0, row_length)]
                result.insert(0, generate_row)
                result.append(generate_row)

        return result


print(Solution.prettyPrint('', 3))
