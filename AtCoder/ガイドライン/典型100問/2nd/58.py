n,m,k,s = map(int,input().split())
p,q = map(int,input().split())

z = [int(input())-1 for _ in range(k)]

danger = set(z)

print(danger)

from collections import defaultdict, deque
road = list(list(map(int,input().split())) for _ in range(m))
dd = defaultdict(list)
for i in road:
    a,b = i
    dd[a-1].append(b)
    dd[b-1].append(a)

def bfs(u):
    global danger, s
    queue = deque([u])
    d = [None] * n 
    d[u] = 0 
    while queue:
        v = queue.popleft()
        for i in dd[v]:
            if d[i-1] is None:
                if d[v] + 1 <= s:
                    d[i-1] = d[v] + 1
                    danger.add(i-1)
                    queue.append(i-1)
for i in z:
    bfs(i)

print(danger)



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

# v,e,r = map(int,input().split())
links = [set() for _ in range(n)]
for i in road:
    # s,t,d = map(int,input().split())
    a,b = i
    if a-1 in danger:
        links[b-1].add((q,a-1))
    else:
        links[b-1].add((p,a-1))
    if b-1 in danger:
        links[a-1].add((q,b-1))
    else:
        links[a-1].add((p,b-1))
    # links[t].add((d,s)) #双方向で使う
print(dijkstra(0, links)[-1]-p)
print(dijkstra(0, links))
