


def solve(parcel):
    count = 0
    temp = []
    res = []

    def dfs(idx, temp):
        if idx == len(parcel):
            return res.append(temp[::])

        if len(temp)>1:
            if temp[-1] > temp[-2]:
                temp.append(parcel[idx])
                dfs(idx+1, temp)
                temp.pop()




    for i in range():
        if i == 0:
            temp.append(n[i])





def brute_force(parcel):
    sub_array = []
    for i in range(len(parcel)):
        for j in range(i, len(parcel)):
            sub_array.append((parcel[i: j+1], j))

    unique_pairs = {}

    print(sub_array)
    count = 0
    for i in sub_array:
        if len(i[0]) >1:
            max_elem = max(i)
            if max_elem != i[-1]:
                count+=1
                print(count, i, max_elem)
    print(count)


def find_subarrays_last_not_max(arr):
    n = len(arr)
    subarrays_dict = {}

    for start in range(n):
        subarrays_dict[start] = []
        for end in range(start, n):
            subarray = arr[start:end + 1]
            if subarray[-1] != max(subarray):
                subarrays_dict[start].append((subarray, (start, end)))


    print(subarrays_dict)

    def find_max_non_overlapping_subarrays(subarrays_dict):
        # Sort subarrays in each list by their end index
        for key in subarrays_dict:
            subarrays_dict[key].sort(key=lambda x: x[1][1])

        # Initialize dp array
        n = max(subarrays_dict.keys()) + 1
        dp = [0] * n

        # Iterate through each starting index and its subarrays
        for start_index in range(n):
            for subarray, (start, end) in subarrays_dict.get(start_index, []):
                # Check if we can include this subarray
                if start_index == 0:
                    dp[end] = max(dp[end], 1)
                else:
                    dp[end] = max(dp[end], dp[start_index - 1] + 1)

        # The maximum value in dp array is the result
        return max(dp)
    print(find_max_non_overlapping_subarrays(subarrays_dict))
    # index = 0
    # count = 0
    # while index !=len(arr):
    #     parcels = subarrays_dict[index]
    #     parcel_index = index
    #     while parcel_index != len(arr):



    # return subarrays



# Example usage
arr = [1, 2, 3, 2, 6, 3]
subarrays = find_subarrays_last_not_max(arr)
for subarray in subarrays:
    print(subarray)

for subarray in subarrays:
    print(subarray)

if __name__ == "__main__":
    n = [1, 2, 3, 2, 6, 3]
    # solve(n)

    # brute_force(n)

