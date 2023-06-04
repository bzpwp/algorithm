from collections import deque
from re import S
n = int(input())
s = input()
d = deque()
dc = deque()
df = deque()
db = deque()
d.append(0)
y = 0
for c in s:
    if c == "L":
        db.appendleft(y)
        y += 1
    else:
        df.append(y)
        y += 1
dc.append(y)
s = df + dc + db
print(*s)