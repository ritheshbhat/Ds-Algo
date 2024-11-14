

def longest_sub_string(s, forbidden):
    max_length = float('-inf')
    sub_str = []
    i = 0
    for j in range(len(s)):
        sub_str.append(s[j])
        for w in forbidden:

            if w in ''.join(sub_str):
                print('here', sub_str, w)
                sub_str.pop(0)
                break
            else:
                if len(sub_str)> max_length:
                    max_length = len(sub_str)

    return max_length


print(longest_sub_string("cbaaabc", forbidden=['aaa', 'cb']))
