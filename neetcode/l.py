def largest(digits):
    res = []
    for d in digits:
        if d >= 10:
            tmp = str(d)
            for i in tmp:
                res.append(int(i))
        else:
            res.append(int(d))

    res.sort(reverse=True)
    print(res)

largest([1,1,2,3,70])