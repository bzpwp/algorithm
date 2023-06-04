n,m = map(int, input().split())
import bisect
lsa = list(map(int,input().split()))
lsb = list(map(int,input().split()))
lsc = lsa+lsb
lsc.sort()
A = []
for i in lsa:
    A.append(bisect.bisect_right(lsc,i))
print(*A)
A = []
for i in lsb:
    A.append(bisect.bisect_right(lsc,i))
print(*A)