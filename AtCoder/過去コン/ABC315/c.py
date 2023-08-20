n = int(input())
from collections import defaultdict

dd = defaultdict(int)
dd2 = defaultdict(list)

for i in range(n):
    a,b = map(int,input().split())
    if dd[a] < b:
        dd[a] = b
    dd2[a].append(b)

if len(dd2) == 1:
    dd2[a].sort()
    print(dd2[a][-1]+dd2[a][-2]//2)
    exit()


x = 0 #max
y = 0 #max2

for i in dd:
    if dd[i] >= x:
        y = x
        x = dd[i]
    elif dd[i] > y:
        y = dd[i]

A = 0

for i in dd2:
    if len(dd2[i]) >=2:
        dd2[i].sort()
        A = max(dd2[i][-1]+dd2[i][-2]//2, A)

# print(x,y,A)
print(max(x+y,A))