# https://www.interviewbit.com/problems/repeat-and-missing-number-array/


def repeatedNumber(A):
    n = len(A)
    return [sum(A) - sum(set(A)), (n * (n + 1) // 2) - sum(set(A))]
