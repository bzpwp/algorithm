n,k = map(int, input().split())
ls = list(map(int,input().split()))
import itertools
import operator

list(itertools.accumulate(l))
x = 0
for a in range(n):
    for b in range(a,n):
        if sum(ls[a:b+1]) == k:
            x += 1
print(x)