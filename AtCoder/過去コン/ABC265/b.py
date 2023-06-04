n,m,t  = map(int, input().split())
lsa = list(map(int, input().split()))
from collections import defaultdict
dd = defaultdict(int)
for i in range(m):
    x,y = map(int,input().split())
    dd[x]= y

# print(dd)

for i in range(n-1):
    t += dd[i+1]
    t -= lsa[i]
    if t <= 0:
        print("No")
        exit()
    # print(t)
print("Yes")