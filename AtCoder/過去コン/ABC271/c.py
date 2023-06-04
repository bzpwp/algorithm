n = int(input())
ls = list(map(int, input().split()))
ls.sort()
from collections import deque
d = deque(ls)
for i in range(3*10**5+1):
    if len(d)==0:
        print(i)
        exit()
    else:
        if d[0]!=i+1:
            if len(d)==1:
                print(i)
                exit()
            else:
                for j in range(2):
                    d.pop()
        else:
            d.popleft()