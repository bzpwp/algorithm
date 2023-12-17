n = int(input())
ls = list(map(int,input().split()))

import copy
ls2 = copy.copy(ls)

ls2.sort()
import itertools
acc = list(itertools.accumulate(ls2))
# print(ls2)
# print(acc)
A = []
import bisect
for i in ls:
    ind = bisect.bisect_right(ls2,i)
    if ind == n:
        A.append(0)
    else:
        A.append(acc[-1]-acc[ind-1])
        # print(acc[-1]-acc[ind-1])
print(*A)