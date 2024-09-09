

def valid_square(n):
    '''
    iterate through 1 to sqrt of n. no need to iterate thru n because sqrt of n  * sqrt of n is n
    TC: sqrt(n)
    :param n:
    :return:
    '''
    for i in range(1, n+1):
        if i * i == n:
            return True
        if i *i > n:
            return False
    return False


    #approach 2 using binary search.

def binary_search_approach(n):
    '''
    log(n)
    we check mid of the number to see if square of mid == n
    :param n:
    :return:
    '''
    low,  high = 0, n
    while low <=high:
        mid = low + (high-low) // 2
        if mid * mid == n:
            return True
        if mid * mid < n:
            low = mid +1
        if mid * mid > n:
            high = mid - 1
    return False



if __name__ == "__main__":
    n =[16,15,14,4]
    for i in n:
        print(valid_square(i))
    print('bin')
    for i in n:
        print(binary_search_approach(i))