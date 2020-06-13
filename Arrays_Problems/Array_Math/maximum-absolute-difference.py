# https://www.interviewbit.com/problems/maximum-absolute-difference/
import sys


# Efficiency:  Time Limit Exceeded
def maxArr2(A):
    result = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            new_result = abs(A[i] - A[j]) + abs(i - j)
            result = max(new_result, result)

    return result


# Optimized

def maxArr(A):
    max1 = -sys.maxsize - 1
    min1 = sys.maxsize
    max2 = -sys.maxsize - 1
    min2 = sys.maxsize

    for i in range(len(A)):
        max1 = max(max1, A[i] + i)
        min1 = min(min1, A[i] + i)
        max2 = max(max2, A[i] - i)
        min2 = min(min2, A[i] - i)

    return max(max1 - min1, max2 - min2)


def test_function(test_case):
    input = test_case[0]
    expected = test_case[1]
    solution = maxArr(input)
    if solution == expected:
        print("Pass")
    else:
        print("Fail. Expected: ", expected, ", found: ", solution)


A = [1, 3, -1]
test_case = [A, 5]
test_function(test_case)
