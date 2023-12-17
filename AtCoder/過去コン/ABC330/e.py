n,q = map(int,input().split())
ls = list(map(int,input().split()))

from collections import defaultdict

dd = defaultdict(set)

for i in range(n):
    dd[ls[i]].add(i)

values = list(dd.keys())
values.sort()

for_mex = []


if values[0] != 0:
    # mex = 0
    syugou = [0]
    x = 0
    for i in range(len(values)-1):
        if values[i+1] == x+1:
            if len(syugou) == 1:
                # if syugou[0] != x+1:
                syugou.append(x+1)
            else:
                syugou[1] = x + 1
            x += 1
        else:
            for_mex.append(syugou)
            syugou = [values[i+1]]
            x = values[i+1]
    for_mex.append(syugou)
else:
    # mex = 0
    syugou = [values[0]]
    x = values[0]
    for i in range(len(values)-1):
        if values[i+1] == x+1:
            if len(syugou) == 1:
                # if syugou[0] != x+1:
                syugou.append(x+1)
            else:
                syugou[1] = x + 1
            x += 1
        else:
            for_mex.append(syugou)
            syugou = [values[i+1]]
            x = values[i+1]
    for_mex.append(syugou)




print(for_mex)
if for_mex[0][0]!= 0:
    mex = 0
else:
    mex = for_mex[0][1]+1

for _ in range(q):
    i,x = map(int,input().split())
    dd[ls[i-1]].remove(i-1)
    dd[x].add(i-1)
    if len(dd[ls[i-1]]) == 0 and mex > ls[i-1]:
        mex = ls[i-1]
        print(mex)
    else:
        