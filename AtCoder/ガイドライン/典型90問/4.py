h,w = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(h)]

hsum = [sum(i) for i in grid]
wsum = [0 for j in range(w)]
for i in grid:
    for j in range(w):
        wsum[j] += i[j]

for i in range(h):
    print(*[hsum[i]+wsum[j]-grid[i][j] for j in range(w)])

    