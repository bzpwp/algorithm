n,d = map(int,input().split())
ls = [list(map(int,input().split())) for _ in range(n)]

import itertools
import math
from collections import defaultdict
c = list(itertools.combinations(list(range(n)),2))
dd = defaultdict(set)
for i in c:
    a,b = i
    if math.sqrt((ls[a][0]-ls[b][0])**2+(ls[a][1]-ls[b][1])**2) <= d:
        dd[a].add(b)
        dd[b].add(a)
    
A = set([0])
from collections import deque
d = deque([0])

while d:
    q = d.popleft()
    for x in dd[q]:
        if x not in A:
            A.add(x)
            d.append(x)
# print(A)
for i in range(n):
    if i not in A:
        print("No")
    else:
        print("Yes")