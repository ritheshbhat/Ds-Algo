#Combination Sum II – Find all unique combinations

'''
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8

Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]]


Explanation: These are the unique combinations whose sum is equal to target.

Example 2:

Input: candidates = [2,5,2,1,2], target = 5

Output: [[1,2,2],[5]]

Explanation: These are the unique combinations whose sum is equal to target.
'''

def solve(id,arr,target,sub_array,result):
    if target ==0:
        result.append(sub_array[::])

    for i in range(id,len(arr)):
        if i!=id and arr[i]==arr[i-1]:
            continue
        if arr[i]>target:
            break
        sub_array.append(arr[i])
        solve(i+1,arr,target-arr[i],sub_array,result)
        sub_array.pop()




if __name__=="__main__":
    arr = [10,1,2,7,6,1,5]
    target = 8
    sub_array = []
    result = []
    solve(0,sorted(arr),target, sub_array,result)
    print(result)