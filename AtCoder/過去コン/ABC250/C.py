n,q = map(int, input().split())
ls  = [int(input()) for _ in range(q)]
l = list(range(1,n+1))
from collections import deque
ls.sort()
d = deque(ls)

for i in range(q):
    x = d.popleft()
    if d(0)==