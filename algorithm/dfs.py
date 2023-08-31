'''
dfs(grid)
'''
import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

H, W = map(int, input().split())
maze = [list(input()) for h in range(H)]

for h in range(H):
    for w in range(W):
        if maze[h][w] == "s":
            sx, sy = h, w
def dfs(x, y):
    # 範囲外や壁の場合は終了
    if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == '#':
        return

    # ゴールに辿り着ければ終了
    if maze[x][y] == 'g':
        print('Yes')
        exit()

    maze[x][y] = '#' # 確認したルートは壁にしておく

    # 上下左右への移動パターンで再起していく
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

dfs(sx, sy) # スタート位置から深さ優先探索
print('No')



'''
dfs(tree)
'''
## tree
# Atcoderでよく与えられる形
T_list = [[1,2],[2,3],[3,4],[3,5],[2,7],[7,8],[7,9]]
# defaultdictでtreeを表現
from collections import defaultdict as ddict
tree = ddict(list)
for t in T_list:
    tree[t[0]].append(t[1])
print(tree)

from collections import deque
def dfs(T,i,init=True):
    if init==True:
        print(i)
    Q = deque([i])
    q = Q.popleft()
    for c in T[q]:
        print(c)
        dfs(T,c,False)

dfs(tree,1)


'''
#グラフの連結成分数(tree)
グラフ:上で作ったscr_matrixあるいは隣接行列
有向・無向:directed = Trueで有向、Falseで無向
連結条件:connection = 'strong'で両方向に繋がっているときのみ連結、'weak'で片方向で連結でもOK
有向グラフの強連結成分分解はdirected = True, connection = 'strong' でOK
https://kawap23.hatenablog.com/entry/2019/10/06/143159
'''
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
N = int(input())
M = int(input())
edge = np.array([input().split() for _ in range(M)], dtype = np.int64).T
tmp = np.ones(M, dtype = np.int64).T
graph = csr_matrix((tmp, (edge[:] -1)), (N, N))

print (connected_components(graph, directed = True, connection = 'strong'))




'''
#グラフの連結成分数(grid)
'''
# 現在位置 (x, y)
def dfs(x, y):
    # 今いるところを . に置き換える
    field[x][y] = "."

    # 移動する8方向をループ
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            # x, y 方向それぞれに dx, dy 移動した場所を (nx, ny) とする
            nx = x + dx
            ny = y + dy

            # nx と ny が庭の範囲内かどうかと field[nx][ny] が水溜りかどうかを判定
            if 0 <= nx and nx < n and 0 <= ny and ny < m and field[nx][ny] == "W":
                dfs(nx, ny)


n, m = map(int, input().split())
field = [list(input()) for i in range(n)]

res = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == "W":
            # Wが残っているならそこから dfs をはじめる
            dfs(i, j)
            res += 1
print(res)


'''
二部グラフ判定(tree)
'''
# 二部グラフ判定
def dfs(G, v, cur, color):
    color[v] = cur
    for next_v in G[v]:
        # 隣接頂点がすでに色確定していた場合
        if color[next_v] != -1:
            if color[next_v] == cur:
                return False  # 同じ色が隣接したらダメ
            continue

        # 隣接頂点の色を変えて、再帰的に探索 (一回でも false が返ってきたら false)
        if not dfs(G, next_v, 1 - cur, color):
            return False
    return True

def main():
    # 頂点数と辺数
    N, M = map(int, input().split())

    # グラフ入力受け取り
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # 探索
    color = [-1] * N
    is_bipartite = True
    for v in range(N):
        if color[v] != -1:
            continue  # v が探索済みだったらスルー
        if not dfs(G, v, 0, color):
            is_bipartite = False

    if is_bipartite:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()


'''
各頂点の深さ(tree)
'''
def dfs(G, v, p, d, depth):
    depth[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        dfs(G, nv, v, d + 1, depth)

# 仮想的なグラフの例
# G = {0: [1, 2], 1: [0, 3], 2: [0, 4], 3: [1], 4: [2]}
G = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

# ノードの数
N = len(G)

# 各ノードの深さを格納するリスト
depth = [0] * N

# dfsを実行して深さを計算
dfs(G, 0, -1, 0, depth)

# 結果の出力
print(depth)


'''
各頂点の部分木の大きさ(tree)
'''
# 木上の探索
def dfs(G, v, p, d, depth, subtree_size):
    depth[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        dfs(G, nv, v, d + 1, depth, subtree_size)

    # 帰りがけ時に、部分木サイズを求める
    subtree_size[v] = 1  # 自分自身
    for c in G[v]:
        if c == p:
            continue
        subtree_size[v] += subtree_size[c]  # 子のサイズを加える

def main():
    # 頂点数 (木なので辺数は N-1 で確定)
    N = int(input())

    # グラフ入力受け取り
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # 探索
    root = 0  # 仮に頂点 0 を根とする
    depth = [0] * N
    subtree_size = [0] * N
    dfs(G, root, -1, 0, depth, subtree_size)

    # 結果の出力
    for v in range(N):
        print(f"{v}: depth = {depth[v]}, subtree_size = {subtree_size[v]}")

if __name__ == "__main__":
    main()


'''
例題(https://atcoder.jp/contests/abc149/tasks/abc149_f)
'''
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
m = map(int,read().split())
AB = zip(m,m)

MOD = 10 ** 9 + 7

graph = [[] for _ in range(N+1)]
for a,b in AB:
    graph[a].append(b)
    graph[b].append(a)
    
root = 1
parent = [0] * (N+1)
order = []
stack = [root]
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)
# (1/2)^n
x = (MOD + 1) // 2
power = [1] * (N+100)
power_inv = [1] * (N+100)
for i in range(1,N+100):
    power[i] = power[i-1] * 2 % MOD
    power_inv[i] = power_inv[i-1] * x % MOD
# 部分木の大きさ
answer = 0
size = [1] * (N+1)
for v in order[::-1]:
    p = parent[v]
    size[p] += size[v]
    A = [size[w] for w in graph[v] if w != p] # 部分木のサイズ集合
    if v != root:
        A.append(N - 1 - sum(A))
    if len(A) == 1:    
        continue
    prod = 1
    coef = 1
    for x in A:
        prod *= power_inv[x]
        prod %= MOD
        coef += (power[x] - 1)
    E = 1 - prod * coef % MOD
    answer += E
    
answer *= power_inv[1]
answer %= MOD
print(answer)

