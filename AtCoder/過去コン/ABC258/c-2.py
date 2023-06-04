n,q = map(int, input().split())
from collections import deque
s = deque(list(input()))

for i in range(q):
    y,x = map(str,input().split())
    x = int(x)
    if y =="1":
        for j in range(x):
            z = s.pop()
            s.appendleft(z)
    else:
        print(s[x-1])
