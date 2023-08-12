n = int(input())
from collections import defaultdict, deque

dd = defaultdict(list)

for i in range(n):
    u,k,*v = map(int,input().split())
    dd[u] = v

ls = [0 for _ in range(n)]
arrived = [1] + [0 for _ in range(n-1)]

q = deque([1])
while q:
    point = q.popleft()
    points = dd[point]
    for p in points:
        if not ls[p-1]:
            q.append(p)
            arrived[p-1] = 1
            ls[p-1] = ls[point-1] + 1

for i in range(n):
    print(i+1, ls[i])