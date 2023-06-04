h,w = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(h)]

import itertools

p = list(itertools.combinations([i for i in range(h+w-2)], h-1))

A = 0
for v in p:
    l = set([grid[0][0]])
    x,y = 0,0
    for j in range(h+w-2):
        if j in v:
            y +=1
        else:
            x += 1
        l.add(grid[y][x])
    if len(l)==h+w-1:
        A+=1

print(A)