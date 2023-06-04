n,k,x = map(int, input().split())
ls = list(map(int, input().split()))
from collections import deque
d = deque() #枚数
e = deque() #残り
for i in ls:
    d.append(i//x)
    e.append(i%x)
lse = list(e)
lse.sort(reverse = True)
f = deque(lse)
if sum(d)>=k:
    print(sum(ls)-k*x)
elif k-sum(d) >= n:
    print(0)
else:
    for i in range(k-sum(d)):
        f.popleft()
    print(sum(f))