n,x = map(int, input().split())
ls = []
for i in range(n):
    ls.append(list(map(int,input().split()))[1:])
import itertools
a = list(itertools.product(*ls))
b =0
import math
for l in a:
    if math.prod(l) == x:
        b +=1
print(b)
