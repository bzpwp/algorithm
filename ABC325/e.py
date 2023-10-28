n,a,b,c = map(int,input().split())


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

v,e,r = map(int,input().split())
links = [set() for _ in range(v)]
for i in range(e):
    s,t,d = map(int,input().split())
    links[s].add((d,t))
    links[t].add((d,s)) #双方向で使う
print(dijkstra(r, links))