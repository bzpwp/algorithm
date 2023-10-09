ls = [1,2,3,4,6,7]

import bisect
ind = bisect.bisect_left(ls,5)
print(ind)
print(ls)

print(ls[:ind])
print(ls[ind:])