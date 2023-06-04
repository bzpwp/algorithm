#bfs
'''
##tree
'''
# Atcoderでよく与えられる形
T_list = [[1,2],[2,3],[3,4],[3,5],[2,7],[7,8],[7,9]]
# defaultdictでtreeを表現
from collections import defaultdict as ddict
tree = ddict(list)
for t in T_list:
    tree[t[0]].append(t[1])
print(tree)

from collections import deque
def bfs(T,i):
    Q = deque([i])
    # print(i)
    while Q:
        q = Q.popleft()
        for c in T[q]:
            print(c)
            Q.append(c)
# 1から探索
bfs(tree,1)


'''
##general graph
'''
import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()] # nは頂点の数、mは辺の数
g = [[] for _ in range(n)] # 隣接リスト

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)

from collections import deque

def bfs(u):
    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d

# 0からの各頂点の距離
d = bfs(0)
print(d)



'''
##grid
'''
from collections import deque
r,c = map(int,input().split())
sy,sx = map(int,input().split())
gy, gx = map(int,input().split())
grid = []
for i in range(r):
    grid.append(list(input()))

d = deque([[sy,sx]])
grid[sy-1][sx-1]=0
while d:
    p = d.popleft()
    y,x = p
    if grid[y][x-1]==".":
        grid[y][x-1]=grid[y-1][x-1]+1
        d.append([y+1,x])
    if grid[y-2][x-1]==".":
        grid[y-2][x-1]=grid[y-1][x-1]+1
        d.append([y-1,x])
    if grid[y-1][x]==".":
        grid[y-1][x]=grid[y-1][x-1]+1
        d.append([y,x+1])
    if grid[y-1][x-2]==".":
        grid[y-1][x-2]=grid[y-1][x-1]+1
        d.append([y,x-1])


print(grid[gy-1][gx-1])