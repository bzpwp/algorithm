t = int(input())

from collections import defaultdict

for i in range(t):
    n,m =  map(int,input().split())
    lc = list(map(int,input().split()))
    dd = defaultdict(list)
    for j in range(m):
        u,v = map(int,input().split())
        dd[u].append(v)
        dd[v].append(u)
    dp = [[-1 for _ in range(n)] for __ in range(n)]
    for a in dd[1]:
        dp[0][a-1] = lc[a-1]
    for a in range(n):
        for b in range(b):
            if dp[a][b] >= 0:
                for c in dd[b+1]:
                    if lc[c-1] != dp[a][b]:
                        dp[a+1][c-1] = lc[c-1]
    dp2 = [[-1 for _ in range(n)] for __ in range(n)]
    for a in dd[n]:
        dp2[0][a-1] = lc[a-1]
    for a in range(n):
        for b in range(b):
            if dp2[a][b] >= 0:
                for c in dd[b+1]:
                    if lc[c-1] != dp2[a][b]:
                        dp2[a+1][c-1] = lc[c-1]
    a = 10**6
    for a in range(n):
        if dp[a][-1] == 0 and dp2[a][-1] == 1:
            a = a+1
        elif dp[a][-1] == 1 and dp2[a][-1] == 0:
            print(a+1)
