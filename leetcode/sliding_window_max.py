from collections import deque

def sliding_window_max(arr,k):
    result = []

    for i in range(len(arr)-k+1):
        m = float('-inf')
        for j in range(i,i+k):
            if arr[j]> m:
                m = arr[j]
        result.append(m)
    print(result)

    sorted(k)
if __name__=="__main__":
    sliding_window_max([1,3,-1,2,5,6,-2,7], 3)