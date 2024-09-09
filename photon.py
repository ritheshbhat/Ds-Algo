''''
8 characters.
At least one lower case
At least one upper case
At lease one number
At lease one special character


input_str = "abcd12!A"

input_str = ''
input_str < 8 invalid.

'''

from typing import List
def check_validity(input_str: str) -> bool:
    if not input_str:
        return False
    if len(input_str) <8:
        return False

    # length is >=8:
    if input_str.capitalize():
        if input_str.isalpha():
            return True
        else:
            return False
    else:
        return False


if __name__=="__main__":
    sequence_of_inputs = ['abcd1@Aa','','a','111','aaaaaaaaa']

    for each_input in sequence_of_inputs:
        print(check_validity(each_input))
