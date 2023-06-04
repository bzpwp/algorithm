h,w = map(int,input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
for i in range(h):
    for j in range(w):
        if grid[i][j]=="S":
            sy = i
            sx = j
            grid[i][j]=0

from collections import deque
d = deque([sy,sx])
while d:
    y,x = d.popleft()
    if y -1 >= 0 and grid[y-1][x]!="#":
        if grid[y-1][x]!=".":
            print("Yes")
            exit()
        else:
            grid[y-1][x]=0
    if x -1 >= 0 and grid[y][x-1]!="#":
        if grid[y][x-1]!=".":
            print("Yes")
            exit()
        else:
            grid[y][x-1]=0
    if x +1 <= w-1 and grid[y][x+1]!="#":
        if grid[y][x+1]!=".":
            print("Yes")
            exit()
        else:
            grid[y][x+1]=0
    if y +1 <= h-1 and grid[y+1][x]!="#":
        if grid[y+1][x]!=".":
            print("Yes")
            exit()
        else:
            grid[y+1][x]=0
print("No")

