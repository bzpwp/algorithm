n = int(input())
from collections import defaultdict
dd = defaultdict(list)
for i in range(n):
    a,b = map(int,input().split())
    dd[min(a,b)].append(max(a,b))
ans = 1
import sys
sys.setrecursionlimit(10**9) 
from collections import deque
que = deque([[1]])
while que:
    # print(que)
    ls = que.popleft()
    for i in ls:
        ans = max(i,ans)
        # print(i)
        # print(dp)
        # print(dp[i-1])
        
        if dd[i]:
            que.append(dd[i])

print(ans)