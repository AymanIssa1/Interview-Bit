# https://www.interviewbit.com/problems/power-of-2/

class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        number = int(A)

        while number > 2:
            if number % 2 == 1:
                return 1
            number /= 2
            print(number)

        if number == 2:
            return 1
        return 0


print('solution: ', Solution.power(0, "20"))
