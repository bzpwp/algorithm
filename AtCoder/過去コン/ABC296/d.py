n,m = map(int,input().split())

if n**2 < m:
    print(-1)
    exit()

x = 10**25
import math
y = math.floor(math.sqrt(m))
for a in range(1,y+1):
    b = math.ceil(m/a)
    if b <= n and a*b >= m:
        x = min(a*b,x)
    elif b+1 <= n and a*(b+1) >= m:
        x = min(a*(b+1),x)
    elif a+1 <= n:
        x = min((a+1)*b,x)
print(x)