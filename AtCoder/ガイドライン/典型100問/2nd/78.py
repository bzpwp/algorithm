m,n = map(int,input().split())
k = int(input())
grid = [input() for _ in range(m)]
research = [list(map(int,input().split())) for _ in range(k)]

jl = [[0 for _ in range(n+1)] for __ in range(m+1)]
ol = [[0 for _ in range(n+1)] for __ in range(m+1)]
il = [[0 for _ in range(n+1)] for __ in range(m+1)]

for i in range(m):
    for j in range(n):
        if grid[i][j] == "J":
            jl[i+1][j+1] = 1
        elif grid[i][j] == "O":
            ol[i+1][j+1] = 1
        elif grid[i][j] == "I":
            il[i+1][j+1] = 1

import itertools
jl = [list(itertools.accumulate(i)) for i in jl]
ol = [list(itertools.accumulate(i)) for i in ol]
il = [list(itertools.accumulate(i)) for i in il]
# for i in jl:
#     print(i)
for i in range(2,m+1):
    for j in range(1,n+1):
        jl[i][j] += jl[i-1][j]
        ol[i][j] += ol[i-1][j]
        il[i][j] += il[i-1][j]

# for i in jl:
#     print(i)
for cor in research:
    ymin,xmin,ymax,xmax = cor
    print(jl[ymax][xmax]-jl[ymin-1][xmax]-jl[ymax][xmin-1]+jl[ymin-1][xmin-1], 
          ol[ymax][xmax]-ol[ymin-1][xmax]-ol[ymax][xmin-1]+ol[ymin-1][xmin-1], 
          il[ymax][xmax]-il[ymin-1][xmax]-il[ymax][xmin-1]+il[ymin-1][xmin-1])