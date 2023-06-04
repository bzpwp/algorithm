h,w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

for i in range(h):
    ls = grid[i]
    for j in range(w-1):
        if ls[j] == "T" and ls[j+1] == "T":
            grid[i][j] = "P"
            grid[i][j+1] = "C"

for k in grid:
    print("".join(k))