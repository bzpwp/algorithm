n,t = map(int,input().split())
ls = list(map(int,input().split()))

import itertools

l = list(itertools.accumulate(ls))
t %= l[-1]
import bisect

ind = bisect.bisect_left(l,t)
# print(l,t)
# print(ind)

if ind == 0:
    print(1, t)
else:
    print(ind+1, t-l[ind-1])