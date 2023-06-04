h,w,n = map(int,input().split())
grid = []
for i in range(h):
    grid.append(list(input()))


from collections import deque
import copy

for i in range(w):
    for j in range(h):
        if grid[j][i]=="S":
            sy = j
            sx = i
            
A = 0
d = deque([[sy,sx]])
for i in range(n):
    move = copy.deepcopy(grid)
    s = str(i+1)
    move[sy][sx]=0
    while d:
        y,x = d.popleft()
        if y-1>=0 and move[y-1][x]!="X":
            if move[y-1][x]==s:
                A += move[y][x]+1
                sy = y-1
                sx = x
                d = deque([[y-1,x]])
                break
            elif type(move[y-1][x])==str:
                move[y-1][x]=move[y][x]+1
                d.append([y-1,x])
        if y+1<=h-1 and move[y+1][x]!="X":
            if move[y+1][x]==s:
                A += move[y][x]+1
                sy = y+1
                sx = x
                d = deque([[y+1,x]])
                break
            elif type(move[y+1][x])==str:
                move[y+1][x]=move[y][x]+1
                d.append([y+1,x])
        if x+1<=w-1 and move[y][x+1]!="X":
            if move[y][x+1]==s:
                A += move[y][x]+1
                sy = y
                sx = x+1
                d = deque([[y,x+1]])
                break
            elif type(move[y][x+1])==str:
                move[y][x+1]=move[y][x]+1
                d.append([y,x+1])
        if x-1>=0 and move[y][x-1]!="X":
            if move[y][x-1]==s:
                A += move[y][x]+1
                sy = y
                sx = x-1
                d = deque([[y,x-1]])
                break
            elif type(move[y][x-1])==str:
                move[y][x-1]=move[y][x]+1
                d.append([y,x-1])

print(A)