n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
from collections import deque

def dfs(i,check):
    Q = deque(graph[i])
    q = Q.popleft()
