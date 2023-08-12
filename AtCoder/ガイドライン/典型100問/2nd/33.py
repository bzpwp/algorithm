h,w = map(int,input().split())
grid = [list(input()) for _ in range(h)]

dist = [[0 for _ in range(w)] for __ in range(h)]
dist[0][0] = 1
from collections import deque

q = deque([[0,0]])
mv = [[-1,0],[1,0],[0,-1],[0,1]]
grid[0][0] = "#"
A = 1
while q:
    x,y = q.popleft()
    for i,j in mv:
        if 0<=y+j<h and 0<=x+i<w:
            if grid[y+j][x+i] != "#":
                grid[y+j][x+i] = "#"
                dist[y+j][x+i] = dist[y][x] + 1
                q.append([x+i,y+j])
                A += 1
                # print(x,y)
                # print(x+i,y+j)
                # for k in dist:
                #     print(k)
                # print("----")

x = 0
for i in grid:
    for j in i:
        if j == ".":
            x += 1
print(A-dist[-1][-1]+x)