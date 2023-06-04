h,w = map(int,input().split())
grid = [list(input()) for _ in range(h)]


def check(y,x):
    if y + 4 <= h-1 and grid[y][x] == "s" and grid[y+1][x] == "n" and grid[y+2][x] == "u" and grid[y+3][x] == "k" and grid[y+4][x] == "e":
        return [[y,x],[y+1,x],[y+2,x],[y+3,x],[y+4,x]]
    elif y - 4 >= 0 and grid[y][x] == "s" and grid[y-1][x] == "n" and grid[y-2][x] == "u" and grid[y-3][x] == "k" and grid[y-4][x] == "e":
        return [[y,x],[y-1,x],[y-2,x],[y-3,x],[y-4,x]]
    elif x - 4 >= 0 and grid[y][x] == "s" and grid[y][x-1] == "n" and grid[y][x-2] == "u" and grid[y][x-3] == "k" and grid[y][x-4] == "e":
        return [[y,x],[y,x-1],[y,x-2],[y,x-3],[y,x-4]]
    elif x + 4 <= w-1 and grid[y][x] == "s" and grid[y][x+1] == "n" and grid[y][x+2] == "u" and grid[y][x+3] == "k" and grid[y][x+4] == "e":
        return [[y,x],[y,x+1],[y,x+2],[y,x+3],[y,x+4]]
    elif x + 4 <= w-1 and  y + 4 <= h-1 and grid[y][x] == "s" and grid[y+1][x+1] == "n" and grid[y+2][x+2] == "u" and grid[y+3][x+3] == "k" and grid[y+4][x+4] == "e":
        return [[y,x],[y+1,x+1],[y+2,x+2],[y+3,x+3],[y+4,x+4]]
    elif x + 4 <= w-1 and  y - 4 >= 0 and grid[y][x] == "s" and grid[y-1][x+1] == "n" and grid[y-2][x+2] == "u" and grid[y-3][x+3] == "k" and grid[y-4][x+4] == "e":
        return [[y,x],[y-1,x+1],[y-2,x+2],[y-3,x+3],[y-4,x+4]]
    elif x - 4 >= 0 and  y - 4 >= 0 and grid[y][x] == "s" and grid[y-1][x-1] == "n" and grid[y-2][x-2] == "u" and grid[y-3][x-3] == "k" and grid[y-4][x-4] == "e":
        return [[y,x],[y-1,x-1],[y-2,x-2],[y-3,x-3],[y-4,x-4]]
    elif x - 4 >= 0 and  y + 4 <= h-1 and grid[y][x] == "s" and grid[y+1][x-1] == "n" and grid[y+2][x-2] == "u" and grid[y+3][x-3] == "k" and grid[y+4][x-4] == "e":
        return [[y,x],[y+1,x-1],[y+2,x-2],[y+3,x-3],[y+4,x-4]]
    else:
        return False
    
for i in range(h):
    for j in range(w):
        if grid[i][j] == "s":
            result = check(i,j)
            if result:
                for l in result:
                    x,y = l
                    print(x+1,y+1)
                exit()
