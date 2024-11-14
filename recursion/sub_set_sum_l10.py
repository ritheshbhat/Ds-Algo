'''
find sum of all sub sets
'''

sum_a = []
def f(arr, index, temp_sum):
    if index == len(arr):
        sum_a.append(temp_sum)
        return

    f(arr, index+1,temp_sum +arr[index])
    f(arr, index+1,temp_sum)



f([1,2,3],0,0)
sum_a.sort()
print(sum_a)