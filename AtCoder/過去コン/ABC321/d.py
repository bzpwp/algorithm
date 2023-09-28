n,m,p = map(int,input().split())
la = list(map(int,input().split()))
lb = list(map(int,input().split()))

la.sort()
lb.sort()

import bisect
import itertools
LB = list(itertools.accumulate(lb))

A = 0
for i in la:
    ind = bisect.bisect_left(lb,p-i)
    if ind == m:
        A += LB[-1]
        A += i*m
    elif ind == 0:
        A += p*m
        # A += i*m
    else:
        A += LB[ind-1]
        A += i*ind
        A += p*(m-ind)
print(A)