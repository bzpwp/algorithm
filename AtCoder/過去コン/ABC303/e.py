n = int(input())
from collections import defaultdict

dd = defaultdict(set)

for i in range(n):
    u,v = map(int,input().split())
    dd[u].add(u)
    dd[v].add(v)

A = []
for i in dd:
    if len(dd[i]) == 1:
        x = dd[i].pop()
        A.append(len(dd[x]))
        for j in dd[x]:
            if len(dd[j]) == 2:
                dd[j].remove(i)
                dd[dd[j].pop()].remove(j)
            else:
                del dd[j]
A.sort()
print(*A)