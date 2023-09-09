h,w,k,v = map(int,input().split())

grid = [[0 for __ in range(w+1)]] + [[0] + list(map(int,input().split())) for _ in range(h)]

for i in range(h):
    for j in range(w):
        grid[i+1][j+1] += k

