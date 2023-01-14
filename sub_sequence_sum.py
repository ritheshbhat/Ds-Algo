def f(arr: list, index, sum, temp_sum, sub_seq: list):
    # print("sub s, index", sub_seq, index)
    if index == len(arr):
        # print(temp_sum)
        if temp_sum == sum:
            print(sub_seq)
        return

    sub_seq.append(arr[index])

    temp_sum = temp_sum + arr[index]
    f(arr, index + 1, sum, temp_sum, sub_seq)
    sub_seq.pop()
    temp_sum = temp_sum - arr[index]
    f(arr, index + 1, sum, temp_sum, sub_seq)


f([1, 2, 1], 0, 2, 0, [])
