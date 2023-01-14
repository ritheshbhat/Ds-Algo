import sys

#easy problem, just buy 1 share and get max profit. [ make sure buy should happen before sell ]
#brute force, take 2 for loops and check each buy price with every sell price and return max of profit.
#eg:
''' for i in range(arr):
        for j in range(i+1, arr):
            if arr[i]< arr[j]:
                profit = max(profit, arr[j]- arr[i])
        '''
#program is written for optimal solution.

def solve(arr):
    max_profit = 0
    minz = sys.maxsize
    for i in range(len(arr)):
        minz=min(minz,arr[i])
        max_profit = max(max_profit, arr[i]-minz)
    return max_profit



if __name__ == "__main__":
    arr =  [7 ,1 ,5 ,3 ,6 ,4]
    print(solve(arr))
