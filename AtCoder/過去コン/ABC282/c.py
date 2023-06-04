n = int(input())
from collections import deque

# s = list(input())
# print(s)
s = deque(list(input()))

check = True
A = ""

for i in range(n):
    c = s.popleft()
    if check:
        if  c=="\"":
            check = False
            A += c
        elif c==",":
            A += "."
        else:
            A += c
    else:
        if  c=="\"":
            check = True
            A += c
        else:
            A += c
    # print(A,check)
print(A)