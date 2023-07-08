n,m = map(int,input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int,input().split()))

from collections import defaultdict

dd = defaultdict(int)

for i in range(m):
    dd[D[i]] = P[i+1]
# print(dd)
x = 0
for i in range(n):
    if C[i] not in dd:
        x += P[0]
    else:
        x += dd[C[i]]
print(x)