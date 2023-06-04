n,m = map(int,input().split())


x = 10**25
import math
y = math.floor(math.sqrt(m))
for a in range(1,y+1):
    b = math.ceil(m/a)
    if b <= n:
        x = min(a*b,x)
if x == 10**25:
    print(-1)
else:
    print(x)