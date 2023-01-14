



def sort_arr(arr):
    low,mid,high = 0,0,len(arr)-1


    while mid<high:
        if arr[mid] ==0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid +=1
            low +=1
        if arr[mid] ==1:
            mid+=1

        if arr[mid] ==2:
            # temp = arr[mid]
            # arr[mid]=arr[high]
            # arr[high] = temp

            #usual swap replaced with pythonic swap

            arr[mid],arr[high]= arr[high], arr[mid]
            mid+=1
            high -=1













if __name__ == "__main__":
    arr = [2,0,2,1,1,0]
    sort_arr(arr)
    print(arr)