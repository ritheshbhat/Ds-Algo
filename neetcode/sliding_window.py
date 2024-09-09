def solve(arr,id, t: str, sub_array: list, final_array:list):
    if id == len(arr):
        final_array.append(''.join(sub_array[::]) )#IMP: always append a copy of list to another list.
        return

    sub_array.append(arr[id])
    solve(arr,id+1,t,sub_array, final_array)
    sub_array.pop()
    solve(arr,id+1,t,sub_array,final_array)
    return final_array

if __name__=="__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    id = 0
    final_array = []
    sub_array = []
    f = solve(s, id, t,sub_array, final_array)
    # print(final_array)
    # min = 0
    # min_arr = ""
    # max = 0
    # for i in range(len(final_array)):
    #     c = 0
    #     for x in t:
    #         if x in final_array[i]:
    #             c+=1
    #     if c == len(t):
    #         # print(final_array[i])
    #         if len(final_array[i])>= max:
    #             max = len(final_array)
    #         else:
    #             if min> len(final_array[i]):
    #                 min = len(final_array[i])
    #                 min_arr = final_array[i]
    # print(min_arr)