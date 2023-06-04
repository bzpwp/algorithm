n,q = map(int, input().split())
from collections import deque
s = deque(list(input()))

for i in range(q):
    y,x = map(str,input().split())
    x = int(x)
    if y =="1":
        z = s[-1*x:]
        s = z+s[:n-x]
        # print(s)
    else:
        print(s[x-1])
