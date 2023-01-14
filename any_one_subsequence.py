
def f(arr, index, sum, temp_sum, sub_sequence, status) -> bool:
    if index == len(arr):
        if temp_sum == sum:
            print(sub_sequence)
            return True
        else:
            return False

    temp_sum = temp_sum + arr[index]
    sub_sequence.append(arr[index])
    if f(arr, index + 1, sum, temp_sum, sub_sequence, status):
        return True
    else:
        temp_sum = temp_sum - arr[index]
        sub_sequence.pop()
        if f(arr, index + 1, sum, temp_sum, sub_sequence, status):
            return True


f([1, 2, 1], 0, 2, 0, [], False)
