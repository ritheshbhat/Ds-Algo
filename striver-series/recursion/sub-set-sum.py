#https://takeuforward.org/data-structure/subset-sum-sum-of-all-subsets/



def solve(arr,id, sub_array: list,final_array:list):
    if id == len(arr):
        final_array.append(sum(sub_array[::])) #IMP: always append a copy of list to another list.
        return
    sub_array.append(arr[id])
    solve(arr,id+1,sub_array, final_array)
    sub_array.pop()
    solve(arr,id+1,sub_array,final_array)
    return final_array

if __name__=="__main__":
    arr = [5,2,1]
    id=0
    sub_arrays=[]
    final_array=[]
    f = solve(arr, id, sub_arrays, final_array)
    print(sorted(f))