class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        s = set(A)

        for element in A:
            if element in s:
                s.remove(element)
            else:
                return element
