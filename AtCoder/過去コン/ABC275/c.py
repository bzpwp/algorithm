grid = []
for i in range(9):
    grid.append(list(input()))

ans = 0
for i in range(9):
    for j in range(8):
        if grid[i][j]=="#":
            for k in range(j+1,9):
                if grid[i][k]=="#":
                    d = k-j
                    if i+k-j <= 8 and grid[i+k-j][j]=="#" and grid[i+k-j][k]=="#":
                        print(i,j,k)
                        ans += 1
print(ans)