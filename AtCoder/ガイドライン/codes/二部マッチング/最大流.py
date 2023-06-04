#https://qiita.com/drken/items/e805e3f514acceb87602
# 最大フロー最小カットも

"""
# 最大流
# Dinic's algorithm
https://tjkendev.github.io/procon-library/python/max_flow/dinic.html
"""
from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    #有向辺
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
    #無向辺
    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

"""
# 最大流
# module
https://qiita.com/SaitoTsutomu/items/80e70da6717acacefa00
"""

# CSVデータ
import pandas as pd, networkx as nx
from ortoolpy import graph_from_table, networkx_draw
tbn = pd.read_csv('data/node0.csv')
tbe = pd.read_csv('data/edge0.csv')
g = graph_from_table(tbn, tbe)[0]
t = nx.maximum_flow(g, 5, 2)
pos = networkx_draw(g)
nx.draw_networkx_edges(g, pos, width=3, edgelist
  =[(k1, k2) for k1, d in t[1].items() for k2, v in d.items() if v])
plt.show()
for i, d in t[1].items():
    for j, f in d.items():
        if f: print((i, j), f)

# pandas.DataFrame
from ortoolpy.optimization import MaximumFlow
MaximumFlow('data/edge0.csv', 5, 2)[1]

# 乱数データ
import networkx as nx, matplotlib.pyplot as plt
from ortoolpy import networkx_draw
g = nx.random_graphs.fast_gnp_random_graph(10, 0.3, 1)
for i, j in g.edges():
    g.adj[i][j]['capacity'] = 1
t = nx.maximum_flow(g, 5, 6)
pos = networkx_draw(g, nx.spring_layout(g))
nx.draw_networkx_edges(g, pos, width=3, edgelist
  =[(k1, k2) for k1, d in t[1].items() for k2, v in d.items() if v])
plt.show()
