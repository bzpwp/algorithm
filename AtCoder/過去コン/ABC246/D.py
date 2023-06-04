n = int(input())
def func(x,y):
    return x**3+(x**2)*y+(y**2)*x+y**3
from collections import deque
d = deque()
for c in range(10**6):
    for g in range(10**6):
        d.append(func(c,g))
ls = list(d)
ls.sort()
import bisect
e = bisect.bisect(ls, n)
if ls[e-1]==n:
    print(n)
else:
    print(ls[e])