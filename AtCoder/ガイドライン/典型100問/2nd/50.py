n,m = map(int,input().split())
roads = [[float("inf") for _ in range(n)] for __ in range(n)]
gates = [["" for _ in range(n)] for __ in range(n)]
num = [[0 for _ in range(n)] for __ in range(n)]
for i in range(n):
    roads[i][i] = 0

# from collections import defaultdict
# gates = defaultdict(int)

for i in range(m):
    s,t,d,time = map(int,input().split())
    roads[s-1][t-1] = d
    roads[t-1][s-1] = d
    gates[t-1][s-1] = time
    gates[s-1][t-1] = time


dp = [[float("inf") for _ in range(n)] for _ in range(1 << n)]

for i in range(n):
    dp[1 << i][i] = roads[0][i]
for r in dp:
    print(r)
for i in range(1 << n):
    for to in range(n):
        if not i >> to & 1: continue
        if dp[i][to] == float("inf"): continue
        for to2 in range(n):
            if to2 == to: continue
            if dp[i][to] > gates[to][to2]: continue
            print(to2, to, i)
            if dp[i & to2][to2] == dp[i][to] + roads[to][to2]: num[i & to2][to2] += 1
            elif dp[i & to2][to2] > dp[i][to] + roads[to][to2]: num[i & to2][to2] = 1

print((1 << n) -1)
print(dp[(1 << n) - 1][0], num[0][0])

for r in dp:
    print(r)