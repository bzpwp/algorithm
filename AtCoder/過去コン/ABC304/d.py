w,h = map(int,input().split())
n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)]
a = int(input())
lsa = list(map(int,input().split()))
b = int(input())
lsb = list(map(int,input().split()))


# lsa.sort()
# lsb.sort()

dp = [[0 for _ in range(a+1)] for _ in range(b+1)]
import bisect
for s in ls:
    x,y   = s
    indx = bisect.bisect_left(lsa,x)
    indy = bisect.bisect_left(lsb,y)
    dp[indy][indx] += 1

m = 10**18
M = 0
for i in range(a+1):
    for j in range(b+1):
        m = min(dp[j][i],m)
        M = max(dp[j][i],M)
print(m,M)
# print(dp)