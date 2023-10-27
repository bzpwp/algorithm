k = int(input())
ls = list(list(map(int,input().split())) for _ in range(k))

def move(grid,x,y):
    i = 1
    while x-i>=0 and y-i>=0:
        if grid[x-i][y-i] == "Q":
            # print(x-i,y-i)
            return False, grid
        else:
            # grid[x-i][y-i] = "Q"
            i += 1
    i = 1
    while x+i<=7 and y+i<=7:
        if grid[x+i][y+i] == "Q":
            return False, grid
        else:
            # grid[x+i][y+i] = "Q"
            i += 1
    i = 1
    while x+i<=7 and y-i>=0:
        if grid[x+i][y-i] == "Q":
            return False, grid
        else:
            # grid[x+i][y-i] = "Q"
            i += 1
    i = 1
    while x-i>=0 and y+i<=7:
        if grid[x-i][y+i] == "Q":
            return False, grid
        else:
            # grid[x-i][y+i] = "Q"
            i += 1
    return True, grid


import itertools
order = list(itertools.permutations(list(range(8)),8))
# order = [[6,0,2,7,5,3,1,4]]
for o in order:
    check = [["." for _ in range(8)] for __ in range(8)]
    if all(o[x]==y for x,y in ls):
        for x,y in enumerate(o):
            check[x][y] = "Q"
        # print(check)
        # for c in check:
        #     print(c)
        for x,y in enumerate(o):
            boo, check = move(check, x,y)
            # print(boo,x,y)
            # for c in check:
            #     print(c)
            if not boo:
                break
        if boo:
            for i in check:
                print(*i)
            exit()