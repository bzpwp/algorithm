n = int(input())
dp = [[] for _ in range(10**1)]
for i in range(n):
    a,b = map(int,input().split())
    dp[min(a,b)-1].append(max(a,b))
ans = 1
import sys
sys.setrecursionlimit(10**9) 
from collections import deque
que = deque([[1]])
while que:
    ls = que.popleft()
    for i in ls:
        ans = max(i,ans)
        # print(i)
        # print(dp)
        # print(dp[i-1])
        
        if dp[i-1]:
            que.append(dp[i-1])

print(ans)