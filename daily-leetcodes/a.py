# def dp_sol(subarrays_dict):
#     for key in subarrays_dict:
#         subarrays_dict[key].sort(key=lambda x: x[1][1])
#     n = max(subarrays_dict.keys()) + 1
#     dp = [0] * n
#
#     for start_index in range(n):
#         for subarray, (start, end) in subarrays_dict.get(start_index, []):
#             if start_index == 0:
#                 dp[end] = max(dp[end], 1)
#             else:
#                 dp[end] = max(dp[end], dp[start_index - 1] + 1)
#     return max(dp)
#
# def findMaximumBalancedShipments(weight):
#     if not weight:
#         return 0
#     n = len(weight)
#     subarrays_dict = {}
#     for start in range(n):
#         subarrays_dict[start] = []
#         for end in range(start, n):
#             subarray = weight[start:end + 1]
#             if len(subarray) > 1:
#                 if subarray[-1] != max(subarray):
#                     subarrays_dict[start].append((subarray, (start, end)))
#
#
#
#
#     return dp_sol(subarrays_dict)

#
# def findMaximumBalancedShipments(weight):
#     if not weight:
#         return 0
#
#     n = len(weight)
#     dp = [0] * n
#
#     for end in range(n):
#         max_balance = 0
#         for start in range(end):
#             if weight[end] != max(weight[start:end + 1]):
#                 max_balance = max(max_balance, dp[start] + 1)
#         dp[end] = max(max_balance, dp[end - 1] if end > 0 else 0)
#
#     return dp[-1]


def findMaximumBalancedShipments(weight):
    if not weight:
        return 0

    n = len(weight)
    dp = [0] * n

    for end in range(n):
        max_balance = 0
        for start in range(end):
            if weight[end] != max(weight[start:end + 1]):
                max_balance = \






                    max(max_balance, dp[start] + 1)
        dp[end] = max(max_balance, dp[end - 1] if end > 0 else 0)

    return dp[-1]


# Example usage:
weights = [4, 3, 6, 5, 3, 4, 7, 1]
print(findMaximumBalancedShipments(weights))  # Output: 3

# Example usage:
# weights = [3, 1, 5, 4, 2]
# print(findMaximumBalancedShipments(weights))  # Output: 2

if __name__=="__main__":
    n = [1,2,3,2,6,3]
    # n = [8,5,4,7,2]
    n = [4,3,6,5,3,4,7,1]
    # n = [1,2,3,4,5,6]

    print(findMaximumBalancedShipments(n))
