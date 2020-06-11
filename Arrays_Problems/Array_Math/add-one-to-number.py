# https://www.interviewbit.com/problems/add-one-to-number/

# @param A : list of integers
# @return a list of integers
def plusOne(A):
    rest = 1

    i = len(A) - 1
    while i != -1:
        if A[i] == 9 and rest == 1:
            A[i] = 0
        elif A[i] < 9 and rest == 1:
            A[i] += 1
            rest = 0

        i -= 1

    if rest == 1:
        A.insert(0, rest)

    i = 0
    while i != len(A):
        if A[i] == 0:
            A.pop(i)
            i = 0
        else:
            break

    return A


def test_function(test_case):
    input = test_case[0]
    output = test_case[1]
    solution = plusOne(input)
    if output == solution:
        print("Pass")
    else:
        print("Fail. Expected: ", output, ", recevied: ", solution)


test_case1 = [[1, 2, 3, 4], [1, 2, 3, 5]]
test_function(test_case1)

test_case1 = [[9, 9, 9, 9], [1, 0, 0, 0, 0]]
test_function(test_case1)

test_case1 = [[0], [1]]
test_function(test_case1)

test_case1 = [[0, 3, 7, 6, 4, 0, 5, 5, 5], [3, 7, 6, 4, 0, 5, 5, 6]]
test_function(test_case1)
