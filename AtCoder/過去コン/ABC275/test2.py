n = 3

k = 4

grid = [[0 for _ in range(n+1)]for _ in range(k+1)]
print(grid)
grid[1][1]=1
grid[1][1]=27
print(grid)
grid[1][1]%=10
print(grid)