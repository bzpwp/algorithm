N  = int(input())
field = [list(["."]*2001) for _ in range(2001)] # 庭
for i in range(N):
    x,y = map(int,input().split())
    field[x+1000][y+1000]="w"

move = [[-1,-1],[-1,0],[0,-1],[0,1],[1,0],[1,1]]
def dfs(x, y):
    field[x][y] = '.'
    
    for dx,dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 2001 and 0 <= ny < 2001 and field[nx][ny] == 'w':
            dfs(nx, ny)
    return

res = 0
for i in range(2001):
    for j in range(2001):
        if field[i][j] == 'w':
            dfs(i, j)
            res += 1
print(res)