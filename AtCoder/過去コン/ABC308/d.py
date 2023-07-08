'''
dfs(grid)
'''
import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

H, W = map(int, input().split())
maze = [list(input()) for h in range(H)]

l = ["s","n","u","k","e"]

sx,sy = 0,0
def dfs(x, y, mv):
    # 範囲外や壁の場合は終了
    if y >= W or y < 0 or x >= H or x < 0 or l[mv%5] != maze[x][y] or maze[x][y] == '#':
        return

    # ゴールに辿り着ければ終了
    if x == H-1 and y == W-1:
        print('Yes')
        exit()

    maze[x][y] = '#' # 確認したルートは壁にしておく

    # 上下左右への移動パターンで再起していく
    dfs(x+1, y, mv+1)
    dfs(x-1, y, mv+1)
    dfs(x, y+1, mv+1)
    dfs(x, y-1, mv+1)

dfs(sx, sy, 0) # スタート位置から深さ優先探索
print('No')


