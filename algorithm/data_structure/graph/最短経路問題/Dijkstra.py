# 単一始点最短経路問題

# 重みは非負



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
    # links[t].add((d,s)) #双方向で使う
print(dijkstra(r, links))


# 経路復元
from heapq import heappush, heappop, heapify
 
 
def trace(s, t, ancestors):
    route = [t]
    c = t
    while True:
        a = ancestors[c]
        assert a is not None, 'Failed to trace'
        route.append(a)
        if a == s:
            break
        c = ancestors[c]
    route.reverse()
    return route
 
 
def dijkstra(s, links):
    heap = [(*l, s) for l in links[s]]
    heapify(heap)
    visited = set([s])
    dist = [float('inf')] * len(links) 
    routes = [float('inf')] * len(links) 
    dist[s] = 0
    routes[s] = [s]
    ancestors = [None] * len(links)
    while heap:
        cost, node, ancestor = heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        ancestors[node] = ancestor
        dist[node] =cost
        routes[node] = trace(s, node, ancestors)
        for cost2, node2 in links[node]:
            if node2 not in visited:
                heappush(heap, (cost + cost2, node2, node))
    return dist, routes


v,e,r = map(int,input().split())
links = [set() for _ in range(v)]
for i in range(e):
    s,t,d = map(int,input().split())
    links[s].add((d,t))
    # links[t].add((d,s)) #双方向で使う
print(dijkstra(r, links))



