h,w = map(int,input().split())
grid = [list(input()) for _ in range(h)]



obs = set([">", "v", "<", "^", "#"])
for i in range(h):
    for j in range(w):
        if grid[i][j] == "S":
            sx, sy = j,i
        elif grid[i][j] == "^":
            j -=1
            while j >= 0 and grid[i][j] not in obs:
                grid[i][j] = "!"
                j -= 1
        elif grid[i][j] == "<":
            i -=1
            while i >= 0 and grid[i][j] not in obs:
                grid[i][j] = "!"
                i -=1
        elif grid[i][j] == ">":
            i +=1
            while i <= w-1 and grid[i][j] not in obs:
                grid[i][j] = "!"
                i +=1
        elif grid[i][j] == "v":
            j +=1
            while j <= h-1 and grid[i][j] not in obs:
                grid[i][j] = "!"
                j += 1
obs.add("!")


import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

def dfs(x, y, dist):
    # 範囲外や壁の場合は終了
    if y >= w or y < 0 or x >= h or x < 0 or grid[x][y] in obs:
        return
    dist += 1
    # ゴールに辿り着ければ終了
    if grid[x][y] == 'G':
        print('Yes')
        exit()

    grid[x][y] = '#' # 確認したルートは壁にしておく

    # 上下左右への移動パターンで再起していく
    dfs(x+1, y, dist)
    dfs(x-1, y, dist)
    dfs(x, y+1, dist)
    dfs(x, y-1, dist)

dfs(sx, sy) # スタート位置から深さ優先探索
print(-1)
