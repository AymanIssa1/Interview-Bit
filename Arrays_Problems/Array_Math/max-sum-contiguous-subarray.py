# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

import sys


# First attempt O(lonN*N^2) - Time exceeded :/
def maxSubArray1(A):
    result = -sys.maxsize

    array_range = 0
    while array_range < len(A):
        for i in range(array_range, len(A)):
            new_result = 0
            for j in range(i - array_range, i + 1):
                new_result += A[j]

            result = max(result, new_result)

        array_range += 1

    return result


# Optimized attempt
def maxSubArray(A):
    result = -sys.maxsize
    new_result = 0
    for i in A:
        new_result += i
        if new_result > result:
            result = new_result
        if new_result <= 0:
            new_result = 0
    return result


def test_function(test_case):
    input = test_case[0]
    expected = test_case[1]
    solution = maxSubArray(input)
    if solution == expected:
        print("Pass")
    else:
        print("Fail. Expected: ", expected, ", found: ", solution)


test_case = [[10], 10]
test_function(test_case)

test_case = [[1, 2, 3, 4, -10], 10]
test_function(test_case)

test_case = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6]
test_function(test_case)
