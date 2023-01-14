'''
Given an array of distinct integers and a target, you have to return the list of all unique combinations where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from the given array an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: array = [2,3,6,7], target = 7

Output: [[2,2,3],[7]]

Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
             7 is a candidate, and 7 = 7.
             These are the only two combinations.


Example 2:

Input: array = [2], target = 1

Output: []

Explaination: No combination is possible.

'''

#Optimize this by removing call to sum(sub_array) and reducing the target value to target - arr[i] in line 39 and line 33 will be if target ==0: then return.
def solve(id, arr,target,sub_array: list,result):
    if id == len(arr):
        return
    if sum(sub_array) ==target:
        result.append(sub_array[::])
        return
    if sum(sub_array)< target:
        sub_array.append(arr[id])
        print(sub_array)
        solve(id,arr,target,sub_array, result)
        sub_array.pop()
    print("id for not pick is",id+1)
    solve(id+1,arr,target,sub_array,result)

if __name__=="__main__":
    arr = [2,3,6,7]
    target = 7
    res = []
    solve(0,arr,target,[],res)
    print(res)