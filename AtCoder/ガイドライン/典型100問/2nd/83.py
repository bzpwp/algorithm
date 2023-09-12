n,m = map(int,input().split())
pl = list(map(int,input().split()))
from collections import defaultdict
dd = defaultdict(list)
for i in range(n-1):
    a,b,c = map(int,input().split())
    dd[i+1] = [a,b,c]

check = [False for _ in range(n-1)]
import math
for i in range(n-1):
    a,b,c = dd[i+1][0], dd[i+1][1], dd[i+1][2]
    check[i] = math.ceil(c/(a-b))

acc = [0 for _ in range(n)]
for i in range(m-1):
    s,t = pl[i], pl[i+1]
    if s > t:
        s, t = t, s
    acc[s-1] += 1
    acc[t-1] -= 1
import itertools
acc = list(itertools.accumulate(acc))
print(acc)
print(check)
print(dd)
A = 0
for i in range(n-1):
    if acc[i] >= check[i]:
        A += dd[i+1][2]+acc[i]*dd[i+1][1]
    else:
        A += dd[i+1][0]*acc[i]
print(A)
