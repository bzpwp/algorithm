from collections import deque
r,c = map(int,input().split())
sy,sx = map(int,input().split())
gy, gx = map(int,input().split())
grid = []
for i in range(r):
    grid.append(list(input()))

d = deque([[sy,sx]])
grid[sy-1][sx-1]=0
while d:
    p = d.popleft()
    y,x = p
    if grid[y][x-1]==".":
        grid[y][x-1]=grid[y-1][x-1]+1
        d.append([y+1,x])
    if grid[y-2][x-1]==".":
        grid[y-2][x-1]=grid[y-1][x-1]+1
        d.append([y-1,x])
    if grid[y-1][x]==".":
        grid[y-1][x]=grid[y-1][x-1]+1
        d.append([y,x+1])
    if grid[y-1][x-2]==".":
        grid[y-1][x-2]=grid[y-1][x-1]+1
        d.append([y,x-1])


print(grid[gy-1][gx-1])