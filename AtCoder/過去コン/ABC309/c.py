n,k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

grid.sort(key=lambda x: x[0])
print(grid)
A = 0
for i in range(n):
    A += grid[n-1-i][1]
    if A >= k:
        print(grid[n-1-i][0] + 1)
        exit()
print(1)