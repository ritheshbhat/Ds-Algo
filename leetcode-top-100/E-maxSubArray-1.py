'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

'''

def max_avg_sum(arr, k):
    window_start = 0
    max_sum = sum(arr[window_start: k])
    for i in range(k, len(arr)):
        temp_sum = max_sum - arr[window_start]
        window_start +=1
        temp_sum += + arr[i]

        max_sum = max(temp_sum, max_sum)
    return max_sum / k

print(max_avg_sum([1,12,-5,-6,50,3], 4))
