n,m,k = map(int,input().split())

N = n

G = [[] for i in range(N)]
for i in range(m):
    a,b,c = map(int,input().split())
    G[a-1].append((b-1,c))
    G[b-1].append((a-1,c))

from heapq import heappush, heappop, heapify
used = [0]*N
que = [(c, w) for w, c in G[0]]
used[0] = 1
heapify(que)
 
ans = 0
while que:
    cv, v = heappop(que)
    if used[v]:
        continue
    used[v] = 1
    ans += cv
    for w, c in G[v]:
        if used[w]:
            continue
        heappush(que, (c, w))