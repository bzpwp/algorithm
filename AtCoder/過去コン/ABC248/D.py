n = int(input())
ls = list(map(int, input().split()))
q = int(input())
import collections
for i in range(q):
    l,r,x = map(int, input().split())
    ls1 = ls[l-1:r]
    c = collections.Counter(ls1)
    print(c[x])