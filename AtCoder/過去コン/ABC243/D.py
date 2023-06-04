n,x = map(int, input().split())
s = input()
from collections import deque
d = deque(s)
for i in range(n):
    c = d.popleft()
    if c=="U":
        x = x//2
    elif c=="L":
        x = 2*x
    else:
        x = 2*x+1
print(x)