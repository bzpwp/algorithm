from collections import deque

s = deque(list(input()))
n = len(s)

A = 0
while s:
    x = s.pop()
    if x == "0":
        if s[-1] == "0":
            x = s.pop()
            A += 1
        else:
            A += 1
    else:
        A += 1

print(A)