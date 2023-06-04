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