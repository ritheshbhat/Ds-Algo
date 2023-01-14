def f(arr, index, sum, temp_sum, sub_sequence):
    if index == len(arr):
        if temp_sum == sum:
            return 1
        else:
            return 0

    temp_sum = temp_sum + arr[index]
    sub_sequence.append(arr[index])
    l = f(arr, index + 1, sum, temp_sum, sub_sequence)
    temp_sum = temp_sum - arr[index]
    sub_sequence.pop()
    r = f(arr, index + 1, sum, temp_sum, sub_sequence)

    return l + r


print(f([1, 2, 1, 2, 2], 0, 2, 0, []))
