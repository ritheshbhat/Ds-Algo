
def solve(string):
    stack = []
    pairs = ("{
    for i in string:
        if i == "(" or "{" or "[":
            stack.append(i)
        else:
            if i


if __name__=="__main__":
    input_str = "()[{}()]"
    solve(input_str)