n,m = map(int,input().split())

la = list(map(int,input().split()))
lb = list(map(int,input().split()))

import bisect

la.sort()
lb.sort()

s = 0
ind = bisect.bisect_left(lb,la[s])
while m - ind > s+1:
    s += 1
    if s >= n:
        print(lb[m-n-1]+1)
        exit()
    else:
        ind = bisect.bisect_left(lb,la[s])

if ind == m:
    print(lb[-1]+1)
else:
    print(la[s])