h,w = map(int,input().split())
grid = [list(input()) for _ in range(h)]

minx = 10**18
maxx = 0
miny = 10**18
maxy = 0

for i in range(h):
    for j in range(w):
        # print(i,j)
        if grid[i][j] =="#":
            minx = min(minx, j)
            maxx = max(maxx, j)
            miny = min(miny,i)
            maxy = max(maxy,i)
# print(minx,maxx,miny,maxy)
for i in range(miny, maxy+1):
    for j in range(minx, maxx+1):
        if grid[i][j] == ".":
            print(i+1, j+1)