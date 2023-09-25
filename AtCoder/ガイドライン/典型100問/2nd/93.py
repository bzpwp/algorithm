h,w,k = map(int,input().split())
grid_ori = [[int(i) for i in list(input())] for _ in range(h)]

import copy
A = 0

def delete(grid, repeat, score):
    bool = False
    for i in range(h):
        l = grid[i]
        for j in range(w,k-1, -1): #幅
            for m in range(w+1-j): #始点
                if all(i == l[m] for i in l[m:m+j]):
                    score += (l[m]*j)*2**repeat
                    l[m:m+j] = [0]*j
                    bool = True
    return bool, score

def down(grid):
    for i in range(h-1,0,-1):
        for j in range(w):
            # print(i,j)
            if grid[i][j] == 0:
                # print("!",i,j)
                for m in range(i,0,-1):
                    grid[m][j] = grid[m-1][j]
                grid[0][j] = -1

    for j in range(w):
        if grid[0][j] == 0:
            grid[0][j] = -1

def check(grid):
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0:
                return True
    return False

# for a in range(1,h):
for a in range(1,2):
    # for b in range(w):
    for b in range(1,2):
        grid = copy.deepcopy(grid_ori)
        grid[a][b] = 0
        down(grid)
        # print(grid)
        score = 0
        num = 0
        while True:
            bool, score = delete(grid,num,score)
            print(bool)
            print(grid)
            if not bool:
                break
            while check(grid):
                down(grid)
            num += 1
        A = max(A,score)
print(A)