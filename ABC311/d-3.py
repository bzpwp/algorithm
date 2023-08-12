n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]
check = [[[] for _ in range(m)] for __ in range(n) ]
import sys
sys.setrecursionlimit(10**9)
dist = 0
def move(x, y):
    global grid, dist, check
    for i in ["U","D","R","L"]:
        

        if i not in check[y][x]:
            print(x,y,i,check[y][x])
            x, y = slip(x, y, i)
            check[y][x].append(i)
            move(x, y)

def slip(x, y, dirt):
    global grid, dist
    if dirt == "U":
        while grid[x][y-1] != "#":
            if grid[y][x] != "x":
                grid[y][x] = "x"
                dist += 1
            y -= 1
    elif dirt == "D":
        while grid[x][y+1] != "#":
            if grid[y][x] != "x":
                grid[y][x] = "x"
                dist += 1
            y += 1
    elif dirt == "R":
        while grid[x+1][y] != "#":
            if grid[y][x] != "x":
                grid[y][x] = "x"
                dist += 1
            x += 1
    elif dirt == "L":
        while grid[x-1][y] != "#":
            if grid[y][x] != "x":
                grid[y][x] = "x"
                dist += 1
            x -= 1
    return x, y

move(1, 1)
print(dist)
for i in grid:
    print(i)