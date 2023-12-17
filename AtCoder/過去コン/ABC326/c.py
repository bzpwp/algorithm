n,m = map(int,input().split())
ls = list(map(int,input().split()))

ls.sort()

import bisect

M = 0
for i in range(n):
    x = ls[i]
    ind = bisect.bisect_left(ls,x+m)
    M = max(M, ind-i)
print(M)