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
        f(arr, sum, index, temp_sum, sub_seq)
        sub_seq.pop()
    temp_sum = temp_sum - arr[index]
    f(arr, sum, index + 1, temp_sum, sub_seq)


f([2, 3, 6, 7], 7, 0, 0, [])
print(all_combinations)