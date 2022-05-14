#Sum of N Numbers using recursion

#TC: 0(N) N operations.
#SC: 0(N) // N recursive calls stores func in stack till base condition is reached.



def sum_of_given_num_using_recursion(num: int):
    if num == 0:
        return 0
    return num + sum_of_given_num_using_recursion(num-1)


def factorial_of_given_num_using_recursion(num: int):
    if num == 0 or num == 1:
        return 1
    return num * factorial_of_given_num_using_recursion(num-1)

def factorial_of_given_num_using_parameterised_recursion(sum: int, num: int):
    if num == 0 or num == 1:
        return sum
    return factorial_of_given_num_using_parameterised_recursion(sum*num, num -1)

if __name__=="__main__":
    print("sum of first 10 num is")
    print(sum_of_given_num_using_recursion(10))
    print("factorial of 10 is")
    print(factorial_of_given_num_using_recursion(10))

    print("factorial of 10 using parameterised recursion")
    print(factorial_of_given_num_using_parameterised_recursion(1, 10))
