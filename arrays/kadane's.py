'''
find max continous sub array
'''
import sys


# def kadanes(arr):
#     temp_sum = arr[0]
#     max_size = arr[0]
#
#     for i in arr[1:]:
#         if i+temp_sum >i:
#             temp_sum = temp_sum+i
#         else:
#             temp_sum = i
#         if temp_sum > max_size:
#             max_size = temp_sum
#     return max_size


def kadanes(arr):
    max_size = temp_sum = arr[0]

    for i in arr[1:]:
        temp_sum = max(temp_sum+i, i)
        max_size = max(max_size, temp_sum)
    return max_size

if __name__ == "__main__":
    arr =  [-2,1,-3,1,4,-1,2,1,-5,4]
    # arr = [4,-1,2,1]
    print(kadanes(arr))