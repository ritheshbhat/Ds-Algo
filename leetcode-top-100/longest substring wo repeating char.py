
def solve(s: str):
    start = 0
    sub_array = []
    #length validation.
    if len(s)==0:
        return 0
    if len(s)==1:
        return 1
    sub_array.append(s[0])
    max_length = 0

    for i in range(1,len(s)):
        if s[i] not in sub_array:
            sub_array.append(s[i])
            if len(sub_array) > max_length:
                max_length = len(sub_array)

        else:
            print(sub_array,s[i])
            start =sub_array.index(s[i])+1 #this ensures, we slide the sub array to an index for which s[i] wala same element already existed.
            if len(sub_array)> max_length:
                max_length = len(sub_array)
                print(max_length)
            sub_array = sub_array[start:]
            sub_array.append(s[i])
    return max_length


#using set we can achieve constant lookup time.

'''
   def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        sub_set = set()
        if len(s) == 0:
            return 0
        if len(s)==1:
            return 1
        sub_set.add(s[start])
        max_length = 1
        for i in range(1,len(s)):
            if s[i] not in sub_set:
                sub_set.add(s[i])
                max_length = max(max_length, len(sub_set))
            else:
                sub_set.remove(s[i])
                sub_set.add(s[i])
        return max_length
'''

if __name__=="__main__":
    print(solve("nfpdmpi"))


