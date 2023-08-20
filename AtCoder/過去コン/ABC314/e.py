n,m = map(int,input().split())

dp = [[float("inf") for _ in range(m+1)] for _ in range(n)]

for i in range(n):
    dp[i][0] = 0

from collections import defaultdict
costs = defaultdict(int)
points = defaultdict(list)

for i in range(n):
    c,p,*ls = map(int,input().split())
    costs[i] = c
    points[i] = ls

for i in range(n):
    # cost = costs[i]
    # point = points[i]
    for j in range(m):
        if dp[i][j] != float("inf"):
            for k in range(n):
                cost = costs[k]
                point = points[k]
                for p in point:
                    dp[k][j+p] = min(dp[k][j+p], dp[k][j] + p)