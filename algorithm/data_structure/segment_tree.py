'''
# segment tree, RMQ

操作	segfunc	単位元
最小値	min(x, y)	float('inf')
最大値	max(x, y)	-float('inf')
区間和	x + y	0
区間積	x * y	1
最大公約数	math.gcd(x, y)	0
'''

'''
機能追加
https://algo-logic.info/segment-tree/
'''
#segment tree
#https://qiita.com/takayg1/items/c811bd07c21923d7ec69

#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################

#####ide_ele#####
ide_ele = float('inf')
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
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

a = [14, 5, 9, 13, 7, 12, 11, 1, 7, 8]

seg = SegTree(a, segfunc, ide_ele)

print(len(seg.tree))
print(seg.query(0, 8))
print(seg.tree)
seg.update(5, 0)
print(seg.query(0, 8))








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
