v,e = map(int,input().split())

N = v
G = [[] for i in range(N)]

for i in range(e):
    s,t,w = map(int,input().split())
    G[s].append((t,w))
    G[t].append((s,w))

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
print(ans)