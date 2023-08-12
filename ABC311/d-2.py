n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]

from collections import defaultdict
dd = defaultdict(set)
A = 0
def move(grid, dist, x, y, dd):
    global A
    # print(x,y)
    if y in dd[x]:
        A = max(A, dist)
    else:
        for i in ["U","D","R","L"]:
            # print(i,y,grid[y][x])
            grid, dist, x, y = slip(grid, dist, x, y, i)
            dd[x].add(y)
            move(grid, dist, x, y, dd)


def slip(grid, dist, x, y, dirt):
    if dirt == "U":
        # print(grid[x][y-1])
        while grid[x][y-1] != "#":
            if grid[y][x] != "x":
                grid[y][x] = "x"
                dist += 1
            y -= 1
    elif dirt == "D":
        # print(grid[x][y+1])

        while grid[x][y+1] != "#":
            # print("----")
            if grid[y][x] != "x":
                grid[y][x] = "x"
                dist += 1
            # print(dist)
            y += 1
    elif dirt == "R":
        # print(grid[x+1][y])
        while grid[x+1][y] != "#":
            if grid[y][x] != "x":
                grid[y][x] = "x"
                dist += 1
            x += 1
    elif dirt == "L":
        # print(grid[x-1][y])
        while grid[x-1][y] != "#":
            if grid[y][x] != "x":
                grid[y][x] = "x"
                dist += 1
            x -= 1
    return grid, dist, x, y

move(grid, 0, 1, 1, dd)
print(A)