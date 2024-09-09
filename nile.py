'''



given a list of integers, return the indexes of the first occurrence of a pair whose sum is equal to the given target sum

eg:
inputList = [1, 0, -3, 4, 5, 7, 8, 99, 87,50]
tgtSum = [1]
return either [0, 1]/[2, 3]



'''



def two_sum(current_index, input_arr, target):
    holder = {}
    result = []
    for index in range(current_index+1,len(input_arr)):
        diff = target - input_arr[index]

        if diff in holder:
            for each_val in holder[diff]:
                result.append([index, each_val])
        else:
            for i,v in enumerate(input_arr):
                if v == input_arr[index]:
                    if not holder.get(input_arr[index]):

                        holder[input_arr[index]] = [i]
                    else:
                        holder[input_arr[index]].append(i)

    return result



def three_sum(input_arr, target):
    res = []
    for i in range(len(input_arr)-2):
        remaining_target = target - input_arr[i]

        two_sum_result = two_sum(i, input_arr, remaining_target)

        for each_result in two_sum_result:
            each_result.insert(0,i)
            if each_result not in res:
                res.append(each_result)
    return res


if __name__ == "__main__":
    input_arr = [0, 2, 4, 5, 2, 7, 8, 9, 10, 11, 15, -5]
    target = 11
    three_sum(input_arr, target)


