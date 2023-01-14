# def knapSack(W, wt, val, n):
#     dp = [0 for i in range( W +1)]  # Making the dp array
#
#     for i in range(1,len(wt)+1):  # taking first i elements
#         for w in range(W, 0, -1):  # starting from back,so that we also have data of
#                                    # previous computation when taking i-1 items
#             if wt[i - 1] <= w:
#                 # finding the maximum value
#                 dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])
#
#     return dp[W]  # returning the maximum value of knapsack
#
#
# # Driver code
# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
# # This code is contributed by Suyash Saxena
# print(knapSack(W, wt, val, n))

def knapsack(max_weight, given_weights, values_for_each_weight, current_index): #current_index starts from last index of array
    if current_index == 0 or max_weight == 0:
        return 0

    if given_weights[current_index] > max_weight:
        return knapsack(max_weight, given_weights, values_for_each_weight, current_index - 1)
    else:
        return max(
            values_for_each_weight[current_index] + knapsack(max_weight - given_weights[current_index],
                                                                 given_weights, values_for_each_weight,
                                                                 current_index - 1),
            knapsack(max_weight, given_weights, values_for_each_weight, current_index - 1)
        )


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
# This code is contributed by Suyash Saxena
print(knapsack(W, wt, val, len(wt)-1))
