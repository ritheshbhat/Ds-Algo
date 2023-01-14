'''
Program to generate Pascal’s Triangle
Problem Statement: Given an integer N, return the first N rows of Pascal’s triangle.

In Pascal’s triangle, each number is the sum of the two numbers directly above it as shown in the figure below:
'''

def solve_pascal(num):
    arr = [[-1]*(i+1) for i in range(num)]
    if num == 1:
        arr[0][0] = 1
        return arr
    if num ==2:
        arr[1][0] = 1
        arr[1][1] = 1
        return arr

    arr[0][0] = 1
    arr[1][0] = 1
    arr[1][1] = 1
    for layer in range(2,num):
        arr[layer][0]=1
        arr[layer][layer]=1
        for i in range(1,layer):
            arr[layer][i] = arr[layer-1][i]+ arr[layer-1][i-1] #current index value is, sum of prev rows 2 indexes ( i, i-1)
    return arr





if __name__=="__main__":
    num = 8
    print(solve_pascal(num))