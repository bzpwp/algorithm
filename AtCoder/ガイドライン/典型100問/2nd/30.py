h,w,n = map(int,input().split())

ori = [list(input()) for _ in range(h)]
dist = [[0 for _ in range(w)] for __ in range(h)]

import copy

grid = copy.deepcopy(ori)

A = 0
mx = [-1,1]
my = [-1,1]
for i in range(h):
    for j in range(w):
        if ori[i][j] == "S":
            sx,sy = j,i
from collections import deque
dd = deque([[sy,sx]])
for i in range(n):
    while dd:
        y,x = dd.popleft()
        for j in my:
            for k in mx:
                if h-1 >= y+j >= 0 and w-1 >= x+k >= 0 and grid[y+j][x+k] != "X":
                    dd.append([y+j, x+k])
                    dist[y+j][x+k] = dist[y][x] + 1
                    if dist[y+j][x+k] == i+1:
                        A += dist[y+j][x+k]
                        break
                    grid[y+j][x+k] = "X"
    print(dist)
    dist = [[0 for _ in range(w)] for __ in range(h)]
    grid = copy.deepcopy(ori)

print(A)
        