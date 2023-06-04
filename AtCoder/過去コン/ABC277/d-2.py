n,m = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
ans = sum(ls)
from collections import defaultdict

dd = defaultdict(int)
x = 0
if n == 1:
    print(0)
elif ls[0]==0:
    y = 0
    z = True
    a = 0
    for i in range(1,n):
        if ls[i]-ls[i-1]>=2:
            if z:
                z = False
                a = y
            x = max(x,y)
            y = 0
        if i == n-1 and ls[i]==m-1:
            y += m-1
            y += a
            x = max(x,y)
        elif i == n-1:
            y += ls[i]
            x = max(x,y)
        else:
            y += ls[i]
    print(ans-x)

else:
    y = ls[0]
    for i in range(1,n):
        if ls[i]-ls[i-1]>=2:
            x = max(x,y)
            y = 0
        if i == n-1:
            y += ls[i]
            x = max(x,y)
        else:
            y += ls[i]
    print(ans-x)