class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        # in case of A larger or smaller then INT
        if A > pow(2, 31) - 1 or A < -pow(2, 31):
            return 0

        is_minus_number = False
        if A < 0:
            is_minus_number = True
            A = A * -1

        number_length = len(str(A)) - 1
        result = 0

        while A != 0:
            n = A % 10
            A = A // 10
            result = result + (pow(10, number_length) * n)
            number_length -= 1

        # in case of result larger or smaller then INT
        if result > pow(2, 31) - 1 or result < -pow(2, 31):
            return 0

        if is_minus_number:
            result = result * -1

        return result


print(Solution.reverse(None, 123))
print(Solution.reverse(None, -123))
print(Solution.reverse(None, -1146467285))
