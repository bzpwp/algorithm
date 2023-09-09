n = int(input())
dp = [0 for _ in range(10**6+1)]
for i in range(n):
    a,b = map(int,input().split())
    dp[a] += 1
    if b+1 <= 10**6:
        dp[b+1] -= 1

import itertools
dp = list(itertools.accumulate(dp))

print(max(dp))