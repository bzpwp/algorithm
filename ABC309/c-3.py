n,k = map(int,input().split())
from collections import defaultdict


dd = defaultdict(int)

for i in range(n):
    a,b = map(int,input().split())
    dd[a] += b
grid = []
for i in dd:
    grid.append([i,dd[i]])
grid.sort(key=lambda x: -x[0])
import itertools
a = []
for i in grid:
    a.append(i[1])
b = list(itertools.accumulate(a))

import bisect
ind = bisect.bisect_left(b,k)
print(grid[ind][0])
