import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
G = [[] for _ in range(n)]

for i in range(m):
    a,b,x,y = map(int,input().split())
    a -=1
    b -=1
    G[a].append((b,x,y))
    G[b].append((a,-x,-y))

pos = [(0,0)]*n
visited=[False]*n

def dfs(v,x,y):
    visited[v] = True
    pos[v] = (x,y)
    for p,dx,dy in G[v]:
        if not visited[p]:
            dfs(p,x+dx,y+dy)
dfs(0,0,0)



for i in range(n):
    if visited[i]:
        print(*pos[i])
    else:
        print("undecidable")
