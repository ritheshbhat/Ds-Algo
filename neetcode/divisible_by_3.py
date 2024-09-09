TOTAL_SIZE = 10

def sort_array_using_counts(input_arr, n):
    counts = [0] * TOTAL_SIZE
    for i in range(n):
        counts[input_arr[i]] += 1

    index = 0
    for i in range(TOTAL_SIZE):
        while counts[i] > 0:
            input_arr[index] = i
            index += 1
            counts[i] -= 1

def remove_and_print_result(arr, n, index1, index2=-1):
    for i in range(n - 1, -1, -1):
        if i != index1 and i != index2:
            print(arr[i], end="")

def largest_3_multiple(arr, n):
    s = sum(arr)

    sort_array_using_counts(arr, n)

    if s % 3 == 0: # sum of all digit should be divisible by 3, if the number is divisible by 3
        remove_and_print_result(arr, n, -1)
        return True

    remainder = s % 3

    if remainder == 1:
        remainder_2 = [0] * 2
        remainder_2[0] = -1
        remainder_2[1] = -1

        for i in range(n):
            if arr[i] % 3 == 1:
                remove_and_print_result(arr, n, i)
                return True

            if arr[i] % 3 == 2:
                if remainder_2[0] == -1:
                    remainder_2[0] = i
                elif remainder_2[1] == -1:
                    remainder_2[1] = i

        if remainder_2[0] != -1 and remainder_2[1] != -1:
            remove_and_print_result(arr, n, remainder_2[0], remainder_2[1])
            return True

    elif remainder == 2:
        remainder_1 = [0] * 2
        remainder_1[0] = -1
        remainder_1[1] = -1

        for i in range(n):
            if arr[i] % 3 == 2:
                remove_and_print_result(arr, n, i)
                return True

            if arr[i] % 3 == 1:
                if remainder_1[0] == -1:
                    remainder_1[0] = i
                elif remainder_1[1] == -1:
                    remainder_1[1] = i

        if remainder_1[0] != -1 and remainder_1[1] != -1:
            remove_and_print_result(arr, n, remainder_1[0], remainder_1[1])
            return True
    return False

# Driver code
if __name__ == "__main__":
    arr = [2,9,2,3,3]
    n = len(arr)
    largest_3_multiple(arr, n)

# This code is contributed by
# sanjeev2552
