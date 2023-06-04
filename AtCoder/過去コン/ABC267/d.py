n,m = map(int,input().split())
ls = list(map(int,input().split()))
import copy

import heapq

d = copy.deepcopy(ls)
d.reverse()

for i in range(n):
    ls[i]=ls[i]*(-1)
heapq.heapify(ls)

ls = []

for i in range(m):
    x = heapq.heappop(ls)*(-1)
    y = d.index(x)
    d[y]=-10**18
    ls.append([y,x])

ls = sorted(ls, reverse=True, key=lambda x: x[0])

ans = 0
for i in range(m):
    ans += ls[i][1]*(i+1)

print(ans)