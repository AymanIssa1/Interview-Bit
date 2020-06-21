def x(A):
    max_result = []
    max_sum = 0

    current_result = []

    for element in A:
        if element >= 0:
            current_result.append(element)
        else:
            current_sum = sum(current_result)
            if current_sum > max_sum:
                max_sum = current_sum
                max_result = current_result
            elif current_sum == 0 and max_sum == 0 and len(current_result) > len(max_result):
                max_result = current_result
            current_result = []

    if sum(current_result) == 0 and sum(max_result) == 0 and len(max_result) > len(current_result):
        return max_result
    elif max_sum > sum(current_result):
        return max_result
    return current_result


print(x([10, -1, 2, 3, -4, 100]))
print(x([1, 2, 5, -7, 2, 3]))
print(x([0, 0, -1, 0]))
