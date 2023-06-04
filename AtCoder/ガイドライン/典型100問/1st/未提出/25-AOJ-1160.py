w,h = map(int,input().split())
grid = []
for i in range(h):
    grid.append(list(map(int,input().split())))

ans = 0

def dfs(x,y):
    grid[y][x] = 0
    for i in range(-1,2):
        for j in range(-1,2):
            nx = x + i
            ny = y + j
            if ny >= 0 and nx >= 0 and ny <= h-1 and nx <= w-1 and grid[ny][nx]==1:
                dfs(nx,ny)

for k in range(w):
    for l in range(h):
        if grid[l][k] == 1:
            dfs(k,l)
            ans += 1

print(ans)