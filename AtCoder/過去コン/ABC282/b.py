n,m = map(int,input().split())
lss = [input() for _ in range(n)]

import itertools
ls = list(itertools.combinations(list(range(n)),2))
A = 0
for c in ls:
    x,y = c
    s1 = lss[x]
    # print(y)
    s2 = lss[y]
    a = 0
    for i in range(m):
        if s1[i] == "o" or s2[i] == "o":
            a += 1
    if a == m:
        A += 1
print(A)