n,m = map(int,input().split())
ls = [list(map(int,input().split()))for _ in range(n)]

import itertools
c = itertools.combinations(list(range(m)),2)

A = 0
for j in c:
    a = 0
    for i in range(n):
        a += max(ls[i][j[0]],ls[i][j[1]])
    A = max(A,a)
print(A)