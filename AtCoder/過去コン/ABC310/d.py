n,t,m = map(int,input().split())
from collections import defaultdict
dd = defaultdict(set)
for i in range(m):
    a,b = map(int,input().split())
    dd[b].add(a)
print(dd)
A = [0 for _ in range(t+1)]
for i in range(1,t+1):
    x = 1
    for j in range(1, n+1):
        if t-len(dd[j])<=0:
            x = 0
        x *= t-len(dd[j])
        print(x)
    print("---")
    A[i] = x - A[i-1]
import math
print(A[-2]//math.factorial(t))
print(A)