#find all unique sub sets.


'''
Example 1:

Input: array[] = [1,2,2]

Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]

Explanation: We can have subsets ranging from  length 0 to 3. which are listed above. Also the subset [1,2] appears twice but is printed only once as we require only unique subsets.

Input: array[] = [1]

Output: [ [ ], [1] ]

Explanation: Only two unique subsets are available
'''

def solve(id,arr,result : list,sub_array:list):
    if id==len(arr):
        result.append(sub_array[::])
        return

    sub_array.append(arr[id])
    solve(id+1,arr,result,sub_array)
    sub_array.pop()
    solve(id+1,arr,result,sub_array)



def optimal_solve(id,arr,sub_array,result):

    result.append(sub_array[::])
    for i in range(id,len(arr)):
        if i!=id and arr[i]==arr[i-1]:
            print("duplicate found at i,id",i,id,arr[i],arr[i-1])
            continue

        print("appending now",i,id)
        sub_array.append(arr[i])
        print(sub_array)
        # print("i,id is",i,id,sub_array)

        optimal_solve(i+1,arr,sub_array,result)

        sub_array.pop()


if __name__=="__main__":
    arr = sorted([1,2,2])
    result=[]
    sub_array = []
    solve(0,arr,result, sub_array)
    # print("res",result)
    # my_set = set(tuple(x) for x in result) #This removes duplicate sub arrays
    # print(my_set)
    result=[]
    optimal_solve(0,arr,[],result)
    print("optimal",result)

    # optimal_solve(arr)