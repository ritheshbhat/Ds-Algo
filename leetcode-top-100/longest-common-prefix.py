'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''


def longest_prefix(s):
    if len(s) ==0:
        return ""
    if len(s) ==1:
        return s[0]

    s.sort(key=len)
    for i in range(len(s[0])):
        for string in s[1:]:
            if string[i] != s[0][i]:
                return s[0][:i]

    return s[0]

if __name__=="__main__":
    print(longest_prefix(["flower","flow","flamingo"]))