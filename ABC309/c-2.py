n,k = map(int,input().split())
from collections import defaultdict

dd = defaultdict(int)

for i in range(n):
    a,b = map(int,input().split())
    dd[a] += b

grid = []
for i in dd:
    grid.append([i,dd[i]])
grid.sort(key=lambda x: x[0])
# print(grid)
A = 0
for i in range(n):
    A += grid[n-1-i][1]
    if A >= k:
        print(grid[n-1-i][0] + 1)
        exit()
print(1)