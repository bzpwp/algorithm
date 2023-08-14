n,k = map(int,input().split())

from collections import defaultdict, deque
taxi = defaultdict(list)
for i in range(n):
    taxi[i] = list(map(int,input().split()))
print(taxi)
dd = defaultdict(list)
for i in range(k):
    a,b = map(int,input().split())
    dd[a-1].append(b-1)
    dd[b-1].append(a-1)

links = [set() for _ in range(n)]

def bfs(u):
    global links
    r = taxi[u][1]
    cost = taxi[u][0]
    q = deque([u])
    dist = [None]*n
    dist[u] = 0
    while q:
        p = q.popleft()
        for i in dd[p]:
            if dist[i] is None:
                if dist[p]+1 <= r:
                    dist[i] =  dist[p]+1
                    q.append(i)
                    links[u].add((cost, i))

for i in range(n):
    bfs(i)

#Dijkstra
from heapq import heappush, heappop, heapify
 
def dijkstra(s, links):
    heap = list(links[s])
    heapify(heap)
    visited = set([s])
    dist = [float('inf')] * len(links) 
    dist[s] = 0
    while heap:
        cost, node = heappop(heap)
        if node in visited:
            continue
        dist[node] = cost
        visited.add(node)
        for cost2, node2 in links[node]:
            if node2 not in visited:
                heappush(heap, (cost + cost2, node2))
    return dist
print(links)
print(dijkstra(0,links))