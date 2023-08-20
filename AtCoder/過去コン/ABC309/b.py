n = int(input())
grid = [list(input()) for _ in range(n)]
import copy
# print(grid)
r_1 = copy.deepcopy(grid[0])
r_n = copy.deepcopy(grid[-1])
c_1 = []
c_n = []
# print(r_1)
for i in grid:
    c_1.append(i[0])
    c_n.append(i[-1])
grid[0][0] = grid[1][0]
for i in range(1,n):
    # print(i-1)
    grid[0][i] = r_1[i-1]
for i in range(1,n):
    grid[i][-1] = c_n[i-1]
for i in range(0,n-1):
    grid[-1][i] = r_n[i+1]
for i in range(1,n-1):
    grid[i][0] = c_1[i+1]

for i in grid:
    print("".join(i))