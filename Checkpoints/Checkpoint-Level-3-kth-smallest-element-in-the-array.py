class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, arr, k):
        arr = sorted(arr)
        return arr[k - 1]
