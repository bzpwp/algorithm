n = int(input())
from collections import defaultdict
dd = defaultdict(list)
for i in range(n-1):
    a,b = map(int,input().split())
    dd[a].append(b)
    dd[b].append(a)

visited = set([])
length = ["" for i in range(n)]
u = 0
def dfs(p,check,dist):
    global length, u
    length[p-1] = dist
    if dist >= u:
        u = p
    # dist += 1
    check.add(p)
    for next in dd[p]:
        if next not in check:
            dfs(next, check, dist+1)

dfs(1,visited,0)
visited = set([])
length = ["" for i in range(n)]
dfs(u,visited,0)
print(max(length)+1)