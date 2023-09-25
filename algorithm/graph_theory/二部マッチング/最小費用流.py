#https://qiita.com/drken/items/e805e3f514acceb87602

"""
# 最小費用流
# Bellman-Ford Algorithm
https://tjkendev.github.io/procon-library/python/min_cost_flow/primal-dual.html
"""

# 最小費用流(minimum cost flow)
class MinCostFlow:
    def __init__(self, n):
        self.n = n
        self.G = [[] for i in range(n)]

    def addEdge(self, f, t, cap, cost):
        # [to, cap, cost, rev]
        self.G[f].append([t, cap, cost, len(self.G[t])])
        self.G[t].append([f, 0, -cost, len(self.G[f])-1])

    def minCostFlow(self, s, t, f):
        n = self.n
        G = self.G
        prevv = [0]*n; preve = [0]*n
        INF = 10**9+7

        res = 0
        while f:
            dist = [INF]*n
            dist[s] = 0
            update = 1
            while update:
                update = 0
                for v in range(n):
                    if dist[v] == INF:
                        continue
                    gv = G[v]
                    for i in range(len(gv)):
                        to, cap, cost, rev = gv[i]
                        if cap > 0 and dist[v] + cost < dist[to]:
                            dist[to] = dist[v] + cost
                            prevv[to] = v; preve[to] = i
                            update = 1
            if dist[t] == INF:
                return -1

            d = f; v = t
            while v != s:
                d = min(d, G[prevv[v]][preve[v]][1])
                v = prevv[v]
            f -= d
            res += d * dist[t]
            v = t
            while v != s:
                e = G[prevv[v]][preve[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prevv[v]
        return res

"""
# 最小費用流
# Dijkstra’s Algorithm
https://tjkendev.github.io/procon-library/python/min_cost_flow/primal-dual.html
"""

from heapq import heappush, heappop
class MinCostFlow:
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        forward = [to, cap, cost, None]
        backward = forward[3] = [fr, 0, -cost, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def flow(self, s, t, f):
        N = self.N; G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = [0]*N
        prv_v = [0]*N
        prv_e = [None]*N

        d0 = [INF]*N
        dist = [INF]*N

        while f:
            dist[:] = d0
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + H[v]
                for e in G[v]:
                    w, cap, cost, _ = e
                    if cap > 0 and r0 + cost - H[w] < dist[w]:
                        dist[w] = r = r0 + cost - H[w]
                        prv_v[w] = v; prv_e[w] = e
                        heappush(que, (r, w))
            if dist[t] == INF:
                return None

            for i in range(N):
                H[i] += dist[i]

            d = f; v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = prv_e[v]
                e[1] -= d
                e[3][1] += d
                v = prv_v[v]
        return res
    

"""
# 最小費用流
# module
https://qiita.com/SaitoTsutomu/items/41d625df63f1946c7216
"""
# CSVデータ
import pandas as pd, networkx as nx
from ortoolpy import graph_from_table, networkx_draw
tbn = pd.read_csv('data/node0.csv')
tbe = pd.read_csv('data/edge0.csv')
g = graph_from_table(tbn, tbe, directed=True)[0]
result = nx.min_cost_flow(g)
for i, d in result.items():
    for j, f in d.items():
        if f: print((i, j), f)



# pandas.DataFrame
from ortoolpy.optimization import MinCostFlow
MinCostFlow('data/node0.csv','data/edge0.csv')



# 乱数データ
import networkx as nx
g = nx.fast_gnp_random_graph(8, 0.2, 1, True)
g.nodes[1]['demand'] = -2 # 供給
g.nodes[7]['demand'] = 2 # 需要
g.adj[2][7]['capacity'] = 1 # 容量
result = nx.min_cost_flow(g)
for i, d in result.items():
    for j, f in d.items():
        if f: print((i, j), f)