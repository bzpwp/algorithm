n,m = map(int,input().split())

x = 10**25
import math
y = math.floor(math.sqrt(m))
for a in range(1,y+1):
    b = math.ceil(m/a)
    if b <= n:
        if a*b >= m:
            x = min(x,a*b)
        else:
            if b + 1 <= n:
                if a*(b+1) >= m:
                    x = min(x,a*(b+1))
            else:
                if a + 1 <=n:
                    x = min(x,b*(a+1))
if x != 10**25:
    print(x)
else:
    print(-1)