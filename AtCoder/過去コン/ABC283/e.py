h, w = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(h)]

A = 0


from collections import defaultdict

C = defaultdict(int)

def check(y,x):
    if y == 0:
        if x == 0:
            if grid[y][x] == grid[y][x+1]:
                return 3
            elif grid[y][x] == grid[y+1][x]:
                return 4
            else:
                return 2
        if x == w-1:
            if grid[y][x] == grid[y][x-1]:
                return 3
            elif grid[y][x] == grid[y+1][x]:
                return 4
            else:
                return 2
        else:
            if grid[y][x] == grid[y][x-1] or grid[y][x] == grid[y+1][x]:
                return 3
            elif grid[y][x] == grid[y+1][x]:
                return 4
            else:
                return 2
    elif y == h-1:
        if x == 0:
            if grid[y][x] == grid[y][x+1]:
                return 3
            elif grid[y][x] == grid[y-1][x]:
                return 3
            else:
                return 2
        if x == w-1:
            if grid[y][x] == grid[y][x-1]:
                return 3
            elif grid[y][x] == grid[y-1][x]:
                return 3
            else:
                return 2
        else:
            if grid[y][x] == grid[y][x-1] or grid[y][x] == grid[y][x+1]:
                return 3
            elif grid[y][x] == grid[y-1][x]:
                return 3
            else:
                return 2
    else:
        if x == 0:
            if grid[y][x] == grid[y][x+1] or  grid[y][x] == grid[y-1][x] :
                return 3
            elif grid[y][x] == grid[y+1][x]:
                return 4
            else:
                return 2
        elif x == w-1:
            if grid[y][x] == grid[y][x-1] or grid[y][x] == grid[y-1][x] :
                return 3
            elif grid[y][x] == grid[y+1][x]:
                return 4
            else:
                return 2
        else:
            if grid[y][x] == grid[y][x-1] or grid[y][x] == grid[y-1][x] or grid[y][x] == grid[y][x+1]:
                return 3
            elif grid[y][x] == grid[y+1][x]:
                return 4
            else:
                return 2

C[0] = False

def change(a):
    for i in range(w):
        grid[a][i] = 1- grid[a][i] 

for i in range(h):
    for j in range(w):
        if check(i,j) == 4:
            C[i+1] = True
        elif check(i,j) == 3:
            continue
        else:
            if C[i]:
                print(-1)
                exit()
            else:
                C[i] = True
                change(i)
                A += 1

print(A)