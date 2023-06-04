n = int(input())
lsn = list(map(int,input().split()))
q = int(input())
lsq = list(map(int,input().split()))

lsn.sort()

ans = 0
import bisect
for i in lsq:
    index = bisect.bisect_left(lsn,i)
    if index == n:
        continue
    elif lsn[index]==i:
        ans += 1

print(ans)