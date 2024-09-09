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



# def solve(s,id,sub,res,target):
#     if id == len(s):
#         return
#     if sum(sub) == target:
#         res.append(sub[::])
#         return res
#
#     for i in range(id, len(s)):
#         if i!=id and s[id] == s[id-1]:
#             continue
#         if sum(sub)> target:
#             break
#         sub.append(id)
#         solve(s,id+1,sub,res,target)
#         sub.pop()



def solve(id,arr,target,sub_array,result):
    if target ==0:
        print(sub_array)
        return result.append(sub_array[::])

    for i in range(id,len(arr)):
        if i!=id and arr[i]==arr[i-1]:
            continue
        if arr[i]>target:
            break
        sub_array.append(arr[i])
        solve(i+1,arr,target-arr[i],sub_array,result)
        sub_array.pop()




if __name__=="__main__":
    arr = [10,1,6,1]
    target = 8
    sub_array = []
    result = []
    solve(0,sorted(arr),target, sub_array,result)
    print(result)