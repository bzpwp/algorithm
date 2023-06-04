n = int(input()) 
ls = []
for i in range(n):
    ls.append(list(map(int,input().split())))
so = []
import math
for a in ls:
    for b in ls[ls.index(a)+1:]:
        so.append(math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2))
print(max(so))