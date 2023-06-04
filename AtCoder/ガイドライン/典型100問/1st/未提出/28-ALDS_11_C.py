n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    u,*ls = input().split()
    u = int(u)
    k = int(ls[0])
    if ls[0]!="0":
        for j in range(k):
            y = int(ls[j+1])
            graph[u-1].append(y)

d = [-1]*n
from collections import deque
def bfs(u):
    que = deque([u])
    d[u-1]=0
    while que:
        x = que.popleft()
        for i in graph[x-1]:
            if d[i-1]==-1:
                d[i-1]=d[x-1]+1
                que.append(i)

bfs(1)

print(*d)