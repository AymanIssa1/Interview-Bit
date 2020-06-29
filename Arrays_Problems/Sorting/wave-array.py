# @param A : list of integers
# @return a list of integers
def wave(A):
    A.sort()
    for i in range(0, len(A) - 1, 2):
        A[i], A[i + 1] = A[i + 1], A[i]
    return A


print(wave([5, 1, 3, 2, 4]))
