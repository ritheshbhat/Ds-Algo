def multi_recursion(index: int, original_arr: list, arr: list):
    print(original_arr, arr)
    if index == len(original_arr):
        print(arr)
        return
    print(original_arr[index])
    multi_recursion(index + 1, original_arr, arr.append(5))
    arr.pop()
    multi_recursion(index + 1, original_arr, arr)


a = []
multi_recursion(0, [3, 1, 2], a)
