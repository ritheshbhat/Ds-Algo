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
    res = []
    for i in range(n - 1, -1, -1):
        if i != index1 and i != index2:
            res.append(arr[i])
    return res


def largest_3_multiple(arr, n):
    s = sum(arr)

    sort_array_using_counts(arr, n)

    if s % 3 == 0: # sum of all digit should be divisible by 3, if the number is divisible by 3
        return remove_and_print_result(arr, n, -1)

    remainder = s % 3

    if remainder == 1:
        remainder_2 = [0] * 2
        remainder_2[0] = -1
        remainder_2[1] = -1

        for i in range(n):
            if arr[i] % 3 == 1:
                return remove_and_print_result(arr, n, i)

            if arr[i] % 3 == 2:
                if remainder_2[0] == -1:
                    remainder_2[0] = i
                elif remainder_2[1] == -1:
                    remainder_2[1] = i

        if remainder_2[0] != -1 and remainder_2[1] != -1:
            return remove_and_print_result(arr, n, remainder_2[0], remainder_2[1])

    elif remainder == 2:
        remainder_1 = [0] * 2
        remainder_1[0] = -1
        remainder_1[1] = -1

        for i in range(n):
            if arr[i] % 3 == 2:
                return remove_and_print_result(arr, n, i)


            if arr[i] % 3 == 1:
                if remainder_1[0] == -1:
                    remainder_1[0] = i
                elif remainder_1[1] == -1:
                    remainder_1[1] = i

        if remainder_1[0] != -1 and remainder_1[1] != -1:
           return  remove_and_print_result(arr, n, remainder_1[0], remainder_1[1])
    return 0





def divisible_by_15(digits):
    largest =  largest_3_multiple(digits, len(digits))
    if largest[-1] == 0:
        return largest

    for i in range(len(largest) - 1, -1, -1):
        if 0 == largest[i]:
            largest.pop(i)
            largest.append(0)
            return largest
        elif 5 == largest[i]:
            largest.pop(i)
            largest.append(5)
            return largest
    else:
        return 0






print(divisible_by_15([2,2,3,1,6,2,1,4,5]))