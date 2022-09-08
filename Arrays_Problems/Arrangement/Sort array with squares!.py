class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        arr = []
        for a in A:
            arr.append(abs(a) * abs(a))

        arr.sort()
        return arr
