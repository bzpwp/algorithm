'''
隣接リスト
辺の重み無し
'''
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す
print(graph)  # [[2, 3, 5], ..., [1, 3, 4]]

'''
隣接リスト
辺の重み有り
'''
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n):
    u, v, w = map(int, input().split())
    graph[u-1].append([v-1, w])
    graph[v-1].append([u-1, w])  # 有向グラフなら消す
print(graph)  # [[2, 3], [3, 1], [5, 9]], ..., [...]]



#隣接行列
#辺の重み無し
n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1  # 有向グラフなら消す
print(graph)  # [[0, 1, 1, 0, 1], ..., [1, 0, 1, 1, 0]]

#隣接行列
#辺の重み有り
n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w  # 有向グラフなら消す
print(graph)  # [[0, 2, 3, 0, 1], ..., [2, 0, 3, 0, 0]





#隣接リスト to 隣接行列
#重みなし無向
graph_new = [[0]*n for _ in range(n)]  # 隣接行列
for i, g_i in enumerate(graph):
    for j in g_i:
        graph_new[i][j] = 1
print(graph_new)


#隣接行列 to 隣接リスト
#重みなし無向
graph_new = []
for i in range(n):
    tmp_l = []
    for j in range(n):
        if graph[i][j] > 0:
            tmp_l.append(j)
    graph_new.append(tmp_l)
print(graph_new)

#ベルマンフォード
#入力は支点番号、終点番号、辺の重みのMAP,出力は各辺点最小コスト
#負経路無し
INF = float('inf')

V, E = map(int,input().split())    # Vは頂点数、Eは辺数
es = []    # 辺
for _ in range(E):
    # 頂点fromから頂点toへのコストcostの辺
    f, t, c = map(int,input().split())
    es.append([f, t, c])

d = [INF] * V    # 最短距離

# s番目の頂点から各頂点への最短経路を求める
def shortest_path(s):
    d[s] = 0
    while True:
        update = False
        for i in range(E):
            e = es[i]
            if d[e[0]] != INF and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                update = True
        if not update:
            break

shortest_path(0)    # 頂点0を始点とする

print(d)

#ベルマンフォード
#入力は支点番号、終点番号、辺の重みのMAP,出力は検出結果
#負経路有り、検出
INF = float('inf')

V, E = map(int,input().split())    # Vは頂点数、Eは辺数
es = []    # 辺
for _ in range(E):
    # 頂点fromから頂点toへのコストcostの辺
    f, t, c = map(int,input().split())
    es.append([f, t, c])

# trueなら負の閉路が存在する
def find_negative_loop():
    d = [0] * V
    
    for i in range(V):
        for j in range(E):
            e = es[j]
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                
                # n回目にも更新があるなら負の経路が存在する
                if i == V-1:
                    return True
    return False

find_negative_loop()


#ベルマンフォード
#入力は支点番号、終点番号、辺の重みのMAP,出力は各辺点最小コスト,不経路があればINF
INF = float('inf')

V, E = map(int,input().split())    # Vは頂点数、Eは辺数
es = []    # 辺
for _ in range(E):
    # 頂点fromから頂点toへのコストcostの辺
    f, t, c = map(int,input().split())
    es.append([f, t, c])

def bellmanford(s):
    d = [INF] * V
    d[s] = 0
    
    for i in range(V):
        for j in range(E):
            e = es[j]
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                
                # n回目にも更新があるなら負の経路が存在する
                if i == V-1:
                    d[e[1]] = -INF
                    while True:
                        update = False
                        for i in range(len(es)):
                            e = es[i]
                            if d[e[1]] != -INF and d[e[0]] == -INF:
                                d[e[1]] = -INF
                                update = True
                        if not update:
                            break
    return d

D = bellmanford(0)    # 頂点0を始点とする

print(D)










#ダイクストラ
import heapq

def dijkstra(edges, num_node):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, 0])

    while len(node_name) > 0:
        #ヒープから取り出し
        _, min_point = heapq.heappop(node_name)

        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost     #更新
                #ヒープに登録
                heapq.heappush(node_name, [node[min_point] + cost, goal])

    return node

if __name__ == '__main__':
    Edges = [
        [[1, 4], [2, 3]],             # ← 頂点Aからの辺のリスト
        [[2, 1], [3, 1], [4, 5]],   # ← 頂点Bからの辺のリスト
        [[5, 2]],                       # ← 頂点Cからの辺のリスト
        [[4, 3]],                       # ← 頂点Dからの辺のリスト
        [[6, 2]],                       # ← 頂点Eからの辺のリスト
        [[4, 1], [6, 4]],             # ← 頂点Fからの辺のリスト
        []                                # ← 頂点Gからの辺のリスト
        ]

    #今の目的地の数は7つ（0~6: A~G）
    node_num = 7

    opt_node = dijkstra(Edges, node_num)

    #以下は結果を整理するためのコード
    node_name = []
    for i in range(node_num):
        node_name.append(chr(ord('A') + i))    
    result = []
    for i in range(len(opt_node)):
        result.append(f"{node_name[i]} : {opt_node[i]}")
    print(f"'目的地:そこまでの最小コスト'\n\n{result}")





#ダイクストラ
#経路記録
import heapq

def dijkstra(edges, num_node, Goal):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, [0]])

    while len(node_name) > 0:
        #ヒープから取り出し
        _, min_point = heapq.heappop(node_name)
        last = min_point[-1]
        if last == Goal:
            return min_point, node  #道順とコストを出力させている

        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[last]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[last] + cost < node[goal]:
                node[goal] = node[last] + cost     #更新
                #ヒープに登録
                heapq.heappush(node_name, [node[last] + cost, min_point + [goal]])

    return []

if __name__ == '__main__':
    Edges = [
        [[1, 4], [2, 3]],             # ← 頂点Aからの辺のリスト
        [[2, 1], [3, 1], [4, 5]],   # ← 頂点Bからの辺のリスト
        [[5, 2]],                       # ← 頂点Cからの辺のリスト
        [[4, 3]],                       # ← 頂点Dからの辺のリスト
        [[6, 2]],                       # ← 頂点Eからの辺のリスト
        [[4, 1], [6, 4]],             # ← 頂点Fからの辺のリスト
        []                                # ← 頂点Gからの辺のリスト
        ]

    #今の目的地の数は7つ（0~6: A~G）
    node_num = 7
    Goal = 6    
    opt_root, opt_cost = dijkstra(Edges, node_num, Goal)    #道順とコストを出力させている

    #出力を見やすく整理するための変換用辞書型リストの作成
    root_converter = {}
    cost_converter = {}
    for i in range(node_num):
        root_converter[i] = chr(ord('A') + i)
        cost_converter[i] = opt_cost[i]

    arrow = " → "
    result = ""
    for i in range(len(opt_root)):
        if i > 0:
            result += arrow
        result += f"{root_converter[opt_root[i]]}({cost_converter[opt_root[i]]})"

    print(f"ノード(そこまでのコスト)\n\n{result}")







#ワーシャルフロイド法
def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]= min(d[i][j],d[i][k]+d[k][j])
    return d

# n:頂点数　m:辺の数
n,m = map(int,input().split())


# 隣接行列の定義、初期化
# ①コスト(存在しないときはinf)
d = [[float("inf") for i in range(n)] for i in range(n)]

# ②自分自身へのコストは０
for i in range(n):
    d[i][i] = 0

# コスト入力（何もないときは１，問題によっては入力時に指定される）
cost = 1
for i in range(m):
    a,b = map(int,input().split())
d[a][b] = cost
d[b][a] = cost

# output
print(warshall_floyd(d))







#LCA(segment tree)
#https://tjkendev.github.io/procon-library/python/graph/lca-segment-tree.html
# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)

# Euler Tour の構築
S = []
F = [0]*N
depth = [0]*N
def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in G[v]:
        dfs(w, d+1)
        S.append(v)
dfs(0, 0)

# 存在しない範囲は深さが他よりも大きくなるようにする
INF = (N, None)

# LCAを計算するクエリの前計算
M = 2*N
M0 = 2**(M-1).bit_length()
data = [INF]*(2*M0)
for i, v in enumerate(S):
    data[M0-1+i] = (depth[v], i)
for i in range(M0-2, -1, -1):
    data[i] = min(data[2*i+1], data[2*i+2])

# LCAの計算 (generatorで最小値を求める)
def _query(a, b):
    yield INF
    a += M0; b += M0
    while a < b:
        if b & 1:
            b -= 1
            yield data[b-1]
        if a & 1:
            yield data[a-1]
            a += 1
        a >>= 1; b >>= 1

# LCAの計算 (外から呼び出す関数)
def query(u, v):
    fu = F[u]; fv = F[v]
    if fu > fv:
        fu, fv = fv, fu
    return S[min(_query(fu, fv+1))[1]]



#segment tree
#https://qiita.com/takayg1/items/c811bd07c21923d7ec69
#####segfunc#####
def segfunc(x, y):
    return
#################

#####ide_ele#####
ide_ele =
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res






#UnionFind
from collections import defaultdict

class UnionFind():
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members




#グラフ理論もろもろ
#https://qiita.com/maskot1977/items/e1819b7a1053eb9f7d61#%E3%82%B0%E3%83%A9%E3%83%95%E7%90%86%E8%AB%96%E3%81%AE%E5%9F%BA%E7%A4%8E---basics-of-graph-theory--


#木構造
#https://www.cqpub.co.jp/hanbai/books/18/18781/18781_9syo.pdf