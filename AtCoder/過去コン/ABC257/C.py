n = int(input())
s = input()
w = list(map(int, input().split()))
from collections import deque
import bisect

lsc = []
lsa = []
w = deque(w)
for i in range(n):
    x = w.popleft()
    if s[i]=="0":
        lsc.append(x)
    else:
        lsa.append(x)

lsc.sort()
lsa.sort()
lenc = len(lsc)
lena = len(lsa)


if  lenc== 0 or lena==0:
    print(n)
else:
    x = lsc[-1]
    y = 0
    for i in range(x+2):
        cl = bisect.bisect_left(lsc, i)
        al = bisect.bisect_left(lsa, i)
        y = max(y,lena-al+cl)
    print(y)