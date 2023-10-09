n = int(input())
ls = [list(map(int,input().split())) for i in range(n)]
ls.sort()
sizes = [ls[i][0] for i in range(n)]
A = 0

def devide(x,y):
    global A
    # a = 0
    dust = []
    if y%2 == 1:
        y -= 1
        A += 1
    while y >= 1:
        if y%2 == 1:
            dust.append(x)
        y //= 2
        # a += y
        x *= 2
    # return a, dust
    return dust

import bisect
# for i in range(10):
while ls:
    s,c = ls.pop(0)
    _ = sizes.pop(0)
    # a,dust = devide(s,c)
    dust = devide(s,c)
    # A += a
    for d in dust:
        ind = bisect.bisect_left(sizes,d)
        if ind == len(sizes):
            sizes.append(d)
            ls.append([d,1])
        else:
            if d == sizes[ind]:
                ls[ind][1] += 1
            else:
                ls = ls[:ind]+[[d,1]]+ls[ind:]
                sizes = sizes[:ind]+[d]+sizes[ind:]
print(A)