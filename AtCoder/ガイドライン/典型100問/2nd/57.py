
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
# for i in range(e):
#     s,t,d = map(int,input().split())
#     links[s].add((d,t))
#     # links[t].add((d,s)) #双方向で使う
# print(dijkstra(r, links))

n,k = map(int,input().split())
links = [set() for _ in range(n)]

for i in range(k):
    x,*ls = map(int,input().split())
    if x == 1:
        c,d,e = ls
        links[c-1].add((e, d-1))
        links[d-1].add((e, c-1))
    else:
        a,b = ls
        print(dijkstra(a-1, links)[b-1])

        # print(dijkstra(a-1, links)[-1])