n,m = int(input().split())
ls = list(map(int,input().split()))
ans = sum(ls)
from collections import Counter
c = Counter(ls)
A = 0
for i in c:
    x = c[i]*i
    j = (i+1)%m
    x += 