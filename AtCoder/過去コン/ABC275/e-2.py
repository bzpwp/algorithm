n,m,K = map(int,input().split())
grid = [[0 for _ in range(n+1)]for _ in range(K+1)]
grid[0][0]=1
MOD = 998244353
A = pow(m,-1,MOD)
for i in range(K):
    for j in range(n+1):
        for k in range(1,m+1):
            if grid[i][j]!=0:
                if j + k <= n:
                    grid[i+1][j+k] += pow(grid[i][j],-1,MOD)*A
                    grid[i+1][j+k]%MOD
                else:
                    grid[i+1][2*n-j-k] += pow(grid[i][j],-1,MOD)*A
                    grid[i+1][2*n-j-k]%MOD

# print(grid)
print(grid[K+1][n]%MOD)
