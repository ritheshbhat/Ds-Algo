'''
find no. of diff ways you can climb a staris of N height.
you can jump either 1 step or 2 step at a time.
'''


def f(idx):
    if idx <=2:
        return idx
    return f(idx-1)+ f(idx-2)


if __name__=="__main__":
    print(f(5))