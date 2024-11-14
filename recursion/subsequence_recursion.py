subsequence = []


def f(arr: list, index: int, cur_sequence: list):
    if index > len(arr) - 1:
        subsequence.append(cur_sequence[::])
        return
    else:
        '''
        line number 13,14 are key.
        at any given index, to form a sub sequence we always have 2 choices, take that element in our sub array or ignore it.
        '''
        cur_sequence.append(arr[index])
        f(arr, index + 1, cur_sequence)
        cur_sequence.pop()
        f(arr, index + 1, cur_sequence) #ignoring the cur_element.


f([3, 1, 2], 0, [])
print("s",subsequence)
