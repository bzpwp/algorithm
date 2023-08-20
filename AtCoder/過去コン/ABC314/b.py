n = int(input())
from collections import defaultdict

dd = defaultdict(list)
dd2 = defaultdict(list)

for i in range(n):
    c = int(input())
    ls = list(map(int,input().split()))
    dd[c].append(i+1)
    dd2[i+1] = ls

x = int(input())

A = []

for i in range(n):
    if x in dd2[i+1]:
        A.append(i+1)
print(A)
y = float("inf")
for i in A:
    y = min(y, len(dd2[i]))

C = dd[y]
C.sort()

print(len(C))
print(*C)