n,m = map(int,input().split())
from collections import defaultdict
dd = defaultdict(list)
for i in range(1,m+1):
    k,*s = map(int,input().split())
    dd[i] = s
pl = list(map(int,input().split()))

x = 0
for i in range(2**n):
    ls = [j+1 for j in range(n) if i>>j & 1]
    dl = []
    for j in range(m):
        A = 0
        for k in ls:
            if k in dd[j+1]:
                A += 1
        dl.append(A%2)
    
    if dl == pl:
        x += 1
print(x)


