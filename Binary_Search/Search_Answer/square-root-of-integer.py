class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, number):
        if number in [0, 1]:
            return number

        front = 1
        back = number
        while front <= back:
            middle = (front + back) // 2

            expected_value = middle * middle
            if expected_value == number:
                return middle

            if expected_value < number:
                front = middle + 1
            else:
                back = middle - 1

        return front - 1
