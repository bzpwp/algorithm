n,k = map(int, input().split())
ls = list(map(int,input().split()))
x = 0
import itertools
import operator
for i in range(n):
    y = ls[i:n]
    l = list(itertools.accumulate(y))
    x += l.count(k)
print(x)