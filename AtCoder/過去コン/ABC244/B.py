n = int(input())
t = input()
from collections import deque
d = deque(t)
l = ["e",0,0]
for a in range(n):
    c = d.popleft()
    if c == "S":
        if l[0] == "e":
            l[1] = l[1] + 1
        elif l[0] == "w":
            l[1] = l[1] - 1
        elif l[0] == "n":
            l[2] = l[2] + 1
        elif l[0] == "s":
            l[2] = l[2] - 1
    if c == "R":
        if l[0] == "e":
            l[0] = "s"
        elif l[0] == "w":
            l[0] = "n"
        elif l[0] == "n":
            l[0] = "e"
        elif l[0] == "s":
            l[0] = "w"
ls = [l[1],l[2]]
print(*ls)