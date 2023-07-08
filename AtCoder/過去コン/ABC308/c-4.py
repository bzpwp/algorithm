n = int(input())
ls = []
for i in range(n):
    a,b = map(int,input().split())
    ls.append(a/(a+b))
import copy
ori = copy.deepcopy(ls)
ls.sort()
import bisect
from collections import defaultdict
dd = defaultdict(int)
A = [0 for _ in range(n)]
for i in range(n):
    indl = bisect.bisect_left(ls,ori[i])
    indr = bisect.bisect_right(ls,ori[i])
    # print(indl,indr,ls,ori[i])
    if indr-indl == 1:
        A[n-1-indl] = i+1
    else:
        A[n-1-(indr-1-dd[ori[i]])] = i+1
        dd[ori[i]] += 1
        print(dd)

print(*A)