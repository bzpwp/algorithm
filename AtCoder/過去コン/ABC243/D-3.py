n,x = map(int, input().split())
s = input()
x = format(x, 'b')
from collections import deque
d = deque(x)
t = ""
for i in range(n):
    if s[i]=="U":
        t = d.pop()
    elif s[i]=="L":
        d.append("0")
    else:
        d.append("1")
d_string = "".join(list(d))
print(int(d_string,2))