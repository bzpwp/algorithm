n = int(input())
from collections import defaultdict

dd = defaultdict(int)
dd2 = defaultdict(list)

for i in range(n):
    c = int(input())
    ls = list(map(int,input().split()))
    for j in ls:
        dd2[j].append(i+1)
    dd[i+1] = c

x = int(input())
A = dd2[x]

# print(dd)
# print(dd2)
C = []

if not dd2[x]:
    print(len(C))
    print(*C)
    exit()

B = min([dd[i] for i in dd2[x]])

for i in dd2[x]:
    if dd[i] == B:
        C.append(i)

C.sort()
print(len(C))
print(*C)