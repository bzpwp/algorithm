n,m = map(int,input().split())
ls = list(map(int,input().split()))

import itertools
acc = list(itertools.accumulate(ls))
acc.insert(0,0)

x = 0
for i in range(m):
    x += (i+1)*ls[i]

ans = -10**18
ans = max(ans,x)
for i in range(m,n):
    y = m*ls[i]-acc[i]+acc[i-m]
    x += y
    if y > 0:
        ans = max(ans,x)
    
print(ans)