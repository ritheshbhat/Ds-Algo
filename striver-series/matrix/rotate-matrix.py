
def rotate(arr):
    length = len(arr)

    for rings in range(length//2): # there are n/2 squares which can be formed in a n*n matrix. we start fixing the outmost square and move inwards.

        for i in range(rings,length-1-rings):

            top = arr[rings][i]

            arr[rings][i] = arr[-i-1][rings] #top getting values from bottom_left


            arr[-i-1][rings] = arr[-rings-1][-i-1] #bottom left getting value from bottom right


            arr[-rings - 1][-i - 1] = arr[i][-rings-1] #bottom right getting value from top right
            arr[i][-rings-1] = top

if __name__=="__main__":
    arr = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # arr = [[1,2,3],[4,5,6],[7,8,9]]
    for i in arr:
        print(i)
    rotate(arr)
    print("rotated")
    for i in (arr):
        print(i)