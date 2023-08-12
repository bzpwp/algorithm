n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]

check = [[[] for _ in range(m)] for __ in range(n)]
total = 0

def move(y,x):
    global grid, check, total
    for m in ["U","D","R","L"]:
        if m not in check[y][x]:
            check[y][x].append(m)
            newy, newx = slip(y,x,m)
            move(newy, newx)

def slip(y,x,m):
    global grid, check, total
    if m == "U":
        if grid[y][x]==".":
            grid[y][x]="+"
            total += 1
        while grid[y-1][x]!= "#":
            y -= 1
            if grid[y][x]==".":
                grid[y][x]="+"
                total += 1
    elif m == "D":
        if grid[y][x]==".":
            grid[y][x]="+"
            total += 1
        while grid[y+1][x]!= "#":
            y += 1
            if grid[y][x]==".":
                grid[y][x]="+"
                total += 1
    elif m == "R":
        if grid[y][x]==".":
            grid[y][x]="+"
            total += 1
        while grid[y][x+1]!= "#":
            x += 1
            if grid[y][x]==".":
                grid[y][x]="+"
                total += 1
    elif m == "L":
        if grid[y][x]==".":
            grid[y][x]="+"
            total += 1
        while grid[y][x-1]!= "#":
            x -= 1
            if grid[y][x]==".":
                grid[y][x]="+"
                total += 1
    return y, x
move(1,1)
print(total)

for i in grid:
    print(i)