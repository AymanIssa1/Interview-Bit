class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        if len(A) == 0 or len(B) == 0:
            return []

        big_arr = A if len(A) >= len(B) else B
        small_arr = A if len(A) < len(B) else B

        big_arr_index = 0
        small_arr_index = 0

        result = []

        while small_arr_index != len(small_arr) and big_arr_index != len(big_arr):
            if small_arr[small_arr_index] == big_arr[big_arr_index]:
                result.append(small_arr[small_arr_index])
                small_arr_index += 1
                big_arr_index += 1
            elif small_arr[small_arr_index] > big_arr[big_arr_index]:
                big_arr_index += 1
            else:
                small_arr_index += 1

        return result


A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 5]

print(Solution.intersect('', A, B))
