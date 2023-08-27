# rotate matrix clockwise

def solve_with_seperate_array(arr):
    size = len(arr)
    new_arr = [[0]*(size) for _ in range(size)]
    for i in range(size):
        for j in range(size):
            new_arr[i][j] = arr[size-1-j][i]
    print(new_arr)

def optimal(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(n):
        arr[i].reverse()
    print(arr)
if __name__=="__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    solve_with_seperate_array(arr) # brute force

    optimal(arr)