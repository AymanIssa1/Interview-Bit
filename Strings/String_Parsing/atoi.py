class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        A = A.strip()
        decimal = 0
        result = 0
        is_minus_number = False
        for i in range(len(A)):
            if A[i] == '-':
                is_minus_number = True
            elif A[i] == '+':
                pass
            elif A[i].isdigit():
                result = (result * 10) + int(A[i])
                decimal += 1
            else:
                break

        if is_minus_number:
            result *= -1

        if result > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif result < -pow(2, 31):
            return -pow(2, 31)

        return result


print(Solution.atoi('', "a42"))
print(Solution.atoi('', "   -42"))
print(Solution.atoi('', "4193 with words"))
print(Solution.atoi('', "words and 987"))
print(Solution.atoi('', "-88297 248252140B12 37239U4622733246I218 9 1303 44 A83793H3G2 1674443R591 4368 7 97"))
