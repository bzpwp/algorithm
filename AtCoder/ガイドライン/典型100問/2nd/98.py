n = int(input())
ls = list(map(int,input().split()))

A = 1
from collections import defaultdict
dd = defaultdict(int)
dd[-1] = 3
for i in range(n):
    A *= dd[ls[i]-1]
    A %= 1000000007
    dd[ls[i]-1] -= 1
    dd[ls[i]] += 1
print(A)