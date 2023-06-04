s = input()
q = int(input())
from collections import deque
for a in range(q):
    t,k = map(int, input().split())
    orit = t
    move = deque([])
    while t>=1:
        if k%2==1:
            k += 1
            k = k/2
            move.append(True)
        else:
            k = k/2
            move.append(False)
        t -=1
    c = s[int(k-1)]
    for a in range(orit):
        if move.pop():
            if c == "A":
                c = "B"
            elif c == "B":
                c = "C"
            else:
                c = "A"
        else:
            if c == "A":
                c = "C"
            elif c == "B":
                c = "A"
            else:
                c = "B"
    print(c)

