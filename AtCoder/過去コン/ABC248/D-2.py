n = int(input())
ls = list(map(int, input().split()))
q = int(input())
import collections
import copy
ls1 = []
c = collections.Counter()
for i in ls:
    c[i] += 1
    d = copy.copy(c)
    ls1.append(d)
    print(ls1)
for i in range(q):
    l,r,x = map(int, input().split())
    if l == 1:
        print(ls1[r-1][x])
    else:
        print(ls1[r-1][x]-ls1[l-2][x])