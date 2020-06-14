# https://www.interviewbit.com/problems/pascal-triangle/


# @param A : integer
# @return a list of list of integers
def solve(A):
    if A == 0:
        return []
    elif A == 1:
        return [[1]]
    elif A == 2:
        return [[1], [1, 1]]

    pascal = [[1], [1, 1]]

    for _ in range(2, A):
        next_row = [1]
        previous_row = pascal[len(pascal) - 1]
        for i in range(1, len(previous_row)):
            next_row.append(previous_row[i - 1] + previous_row[i])

        next_row.append(1)
        pascal.append(next_row)

    return pascal


print(solve(1))
print(solve(2))
print(solve(3))
print(solve(4))
print(solve(5))
