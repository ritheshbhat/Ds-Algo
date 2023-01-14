'''
sub sequence element can be repeated
sum = 7
sub-seq are: 2,2,3 and [7]
'''

all_combinations = []


def f(arr, sum, index, temp_sum, sub_seq):
    # print("sub sequence and index is ",sub_seq, index)
    if index == len(arr):
        if sum == temp_sum:
            all_combinations.append(sub_seq[::])
            # print(sub_seq)
        return

    temp_sum = temp_sum + arr[index]
    # print("line 18 is: ", temp_sum)
    if temp_sum <= sum:
        sub_seq.append(arr[index])
        # print("temp sum is =>", temp_sum, "index is ", index, "sub seq is", sub_seq)
        # print("sub sequence before rec. call", sub_seq)
        f(arr, sum, index, temp_sum, sub_seq)
        # print("temp_sum, index ",temp_sum, sub_seq)
        sub_seq.pop()
        # print("popping the element =>", sub_seq)
    # print("temp sum after pop ", temp_sum, sub_seq)
    temp_sum = temp_sum - arr[index]
    # print("second recursion call", sub_seq, "index is", index+1)
    f(arr, sum, index + 1, temp_sum, sub_seq)


f([2, 3, 6, 7], 7, 0, 0, [])
print(all_combinations)