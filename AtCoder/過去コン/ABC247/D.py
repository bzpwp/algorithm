q = int(input())
from collections import deque
l = deque([])
for i in range(q):
    q = input()
    if q[0] == "1":
        a,x,c = map(int, q.split())
        for a in range(c):
            l.append(x)
    else:
        a,c = map(int, q.split())
        x = 0
        for b in range(c):
            x += l.popleft()
        print(x)