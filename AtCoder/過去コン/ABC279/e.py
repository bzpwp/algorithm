n,m = map(int,input().split())
lsa = list(map(int,input().split()))

ls = list(range(1,n+1))

grid = [ls]

for i in lsa:
    ls = ls.copy()
    ls[i-1], ls[i] = ls[i], ls[i-1]
    grid.append(ls)
    # print(grid)

A = grid[-1]

for i in range(m):
    # print(grid[i])
    print(A.index(grid[i+1][grid[i].index(1)])+1)