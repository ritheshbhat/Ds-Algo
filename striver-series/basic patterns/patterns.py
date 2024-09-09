


def uniform_pattern(n):
    print("uniform")
    '''
    *****
    *****
    *****
    *****
    *****

    :param n:
    :return:
    '''
    for i in range(n):
        print(''.join(['*']*n))


def ascending_pattern(n):
    print("ascending Order")
    '''
*
**
***
****
*****
    :param n:
    :return:
    '''
    for i in range(n):
        print(''.join(['*']* (i+1)))


def ascending_numbers(n):
    print("ascending numbers")
    '''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
    '''

    for i in range(n):
        temp = []
        for j in range(i+1):
            temp.append(j+1)
        print(' '.join(map(str,temp)))

def ascending_same_numbers(n):
    print("ascending same numbers")
    '''
    1
22
333
4444
55555
    '''

    for i in range(n):
        print(''.join([str(i+1)]* (i+1)))


def descending_pattern(n):
    print("descending pattern")
    '''
******
*****
****
***
**
*
    :param n: 
    :return: 
    '''
    for i in range(n,-1,-1):
        print(''.join(['*'] * (i+1)))


def christmas_tree(n):
    print('christmas tree ascending')

    for i in range(n):
        spaces = ' ' * (n-i+1)
        print(spaces + ''.join(['*']*(2*i+1)))

    print("Descending")
    for i in range(n,-1,-1):
        spaces = ' ' * (n-i+1)
        print(spaces + ''.join(['*']*(2*i+1)))

    print("combined tree")

    for i in range(n):
        spaces = ' ' * (n - i + 1)
        print(spaces + ''.join(['*'] * (2 * i + 1)))
    for i in range(n, -1, -1):
        spaces = ' ' * (n - i + 1)
        print(spaces + ''.join(['*'] * (2 * i + 1)))


if __name__ == "__main__":
    n = 5
    uniform_pattern(n)

    ascending_pattern(n)

    ascending_numbers(n)

    ascending_same_numbers(n)

    descending_pattern(n)

    christmas_tree(n)