'''70
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


def climbing_stairs(total, temp, final):
    if temp == total:
        final[0]+=1
        return

    if temp<total:
        temp+=1
        climbing_stairs(total,temp,final)
        temp-=1

    if temp < total -1:
        temp+=2
        climbing_stairs(total,temp,final)
        temp-=2


if __name__=="__main__":
    # print(f(5))
    final = [0]
    print(climbing_stairs(5,0,final))
    print(final)
