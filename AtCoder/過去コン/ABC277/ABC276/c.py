import itertools
n = int(input())
ls = tuple((map(int,input().split())))
l = list(range(1,n+1))

c = list(itertools.permutations(l,n))
print(*list(c[c.index(ls)-1]))