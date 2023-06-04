h,w = map(int, input().split())
grid  = []
for i in range(h):
    grid.append(list(input()))

A = []
# print(grid)
for j in range(w):
    ans = 0
    for k in range(h):
        # print(j,k)
        if grid[k][j]=="#":
            ans += 1
    A.append(ans)

print(*A)