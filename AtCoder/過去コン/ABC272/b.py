n,m = map(int, input().split())
ls = []
for i in range(m):
    l = list(map(int, input().split()))
    ls += [l[1:]]

import itertools

lsc = list(itertools.combinations(list(range(1,n+1)),2))

a = len(ls)

for pair in lsc:
    x = pair[0]
    y = pair[1]
    z = 0
    for l in ls:
        if x in l and y in l:
            z += 1
    if z == 0:
        print("No")
        exit()

print("Yes")