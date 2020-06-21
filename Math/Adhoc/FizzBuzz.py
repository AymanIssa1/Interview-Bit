class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        result = []

        for i in range(1, A + 1):
            if i % 5 == 0 and i % 3 == 0:
                result.append('FizzBuzz')
            elif i % 5 == 0:
                result.append('Buzz')
            elif i % 3 == 0:
                result.append('Fizz')
            else:
                result.append(i)

        return result


print(Solution.fizzBuzz(None, 10))
print(Solution.fizzBuzz(None, 15))
