n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int,input().split())))

import itertools
# import math

lsc = itertools.permutations(ls,2)


x = 0
for l in lsc:
    # print(l)
    x1 = l[0][0]
    y1 = l[0][1]
    x2 = l[1][0]
    y2 = l[1][1]
    vecx = x1 - x2
    vecy = y1 - y2
    if [x1 - vecy, y1 + vecx] in ls:
        if [x2 - vecy, y2 + vecx] in ls:
            x = max(x, (x1-x2)**2+(y1-y2)**2)
            x = round(x)
            # if x == 3:
            #     print(l)
    elif [x1 +vecy, y1 - vecx] in ls:
        if [x2 +vecy, y2 - vecx] in ls:
            x = max(x, (x1-x2)**2+(y1-y2)**2)
            x = round(x)
            # if x == 3:
            #     print(l)

print(x)
