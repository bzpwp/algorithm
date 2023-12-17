h,w = map(int,input().split())
field = [list(input()) for _ in range(h)]
import sys
sys.setrecursionlimit(10**9) # 再起回数の設定



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
            if 0 <= nx and nx < h and 0 <= ny and ny < w and field[nx][ny] == "#":
                dfs(nx, ny)



res = 0
for i in range(h):
    for j in range(w):
        if field[i][j] == "#":
            # Wが残っているならそこから dfs をはじめる
            dfs(i, j)
            res += 1
print(res)