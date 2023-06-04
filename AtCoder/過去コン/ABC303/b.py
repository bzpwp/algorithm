n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(m)]


x  = 0

for i in range(1,n):
    for j in range(i+1,n+1):
        for k in range(m):
            for l in range(n-1):
                if (grid[k][l] == i and grid[k][l+1] == j) or (grid[k][l] == j and grid[k][l+1] == i):
                    break
            if (grid[k][l] == i and grid[k][l+1] == j) or (grid[k][l] == j and grid[k][l+1] == i):
                    break
        else:
            x += 1
            # print(i,j,k,l)
print(x)