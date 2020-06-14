# https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/

# @param A : integer
# @return a list of integers
def getRow(A):
    if A == 0:
        return [1]
    elif A == 1:
        return [1, 1]

    previous_row = [1, 1]
    current_row = []

    for _ in range(1, A):
        current_row = [1]
        for i in range(1, len(previous_row)):
            current_row.append(previous_row[i - 1] + previous_row[i])

        current_row.append(1)
        previous_row = current_row

    return current_row


print(getRow(3))
