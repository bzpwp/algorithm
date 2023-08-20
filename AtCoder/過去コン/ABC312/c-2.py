n,m = map(int,input().split())

la = list(map(int,input().split()))
lb = list(map(int,input().split()))

import bisect

la.sort()
lb.sort()

s = 0
ind = bisect.bisect_left(lb,la[s])
if ind == m:
    print(lb[-1]+1)
    exit()

else:
    while s+1 < m-ind:
        s += 1
        if s >= n:
            print(lb[m-n-1])
            exit()
        ind = bisect.bisect_left(lb,la[s])
        
if ind == m:
    print(lb[-1]+1)
else:
    print(la[s])


    