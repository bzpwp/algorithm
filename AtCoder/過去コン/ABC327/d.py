n,m = map(int,input().split())
al = list(map(int,input().split()))
bl = list(map(int,input().split()))


G = [[] for _ in range(n)] 

for i in range(m):
    a,b = al[i], bl[i]
    a -= 1
    b -= 1
    if a == b:
        print("No")
        exit()
    G[a].append(b)
    G[b].append(a)

import sys
sys.setrecursionlimit(4100000)

color = [0] * n    # 頂点iの色(1 or -1)
# print(G)
# 頂点を1と-1で塗っていく
def dfs(v, c):
    color[v] = c    # 頂点vをcで塗る
    for i in range(len(G[v])):
        # 隣接している頂点が同じ色ならFalse
        if color[G[v][i]] == c:
            return False
        # 隣接している頂点がまだ塗られていないなら-cで塗る
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            # print(color)
            return False
    # print(color)
    return True

for i in range(m):
    if color[al[i]-1] == 0:
        if not dfs(al[i]-1, 1):
            print("No")
            sys.exit()
print("Yes")