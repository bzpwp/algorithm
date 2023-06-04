m = int(input())
n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int,input().split())))

A = 0
def dfs(x,y,gone,ans):
    global A
    gone[y][x]=0
    ans += 1
    move = [[-1,0],[1,0],[0,1],[0,-1]]
    for i in move:
        nx = x + i[0]
        ny = y + i[1]
        if nx >= 0 and ny >= 0 and nx <= m-1 and ny <= n-1 and gone[ny][nx]==1:
            dfs(nx,ny,gone,ans)
        else:
            A = max(A,ans)

import copy

for k in range(n):
    for l in range(m):
        if grid[k][l]==1:
            gone = copy.deepcopy(grid)
            dfs(l,k,gone,0)
# gone = copy.deepcopy(grid)
# dfs(0,0,gone,0)
print(A)