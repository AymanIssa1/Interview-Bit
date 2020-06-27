class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        if len(A) == 0:
            return B
        if len(B) == 0:
            return A

        a_index = 0
        b_index = 0

        while a_index != len(A) and b_index != len(B):
            if A[a_index] >= B[b_index]:
                A.insert(a_index, B[b_index])
                b_index += 1
            else:
                a_index += 1

        for i in range(b_index, len(B)):
            A.append(B[i])

        return A


A = [1, 5, 8]
B = [6, 9]
print(Solution.merge('', A, B))
