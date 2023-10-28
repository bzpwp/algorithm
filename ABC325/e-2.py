n,a,b,c = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

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
links_car = [set() for _ in range(n)]
links_train = [set() for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        links_car[i].add((grid[i][j]*a,j))
        links_car[j].add((grid[i][j]*a,i)) 
        links_train[i].add((grid[i][j]*b+c,j))
        links_train[j].add((grid[i][j]*b+c,i)) 
car = dijkstra(0, links_car)
trani = dijkstra(n-1, links_train)
# print(car, trani)
x = 10**20
for i in range(n):
    x = min(x, car[i]+trani[i])
print(x)