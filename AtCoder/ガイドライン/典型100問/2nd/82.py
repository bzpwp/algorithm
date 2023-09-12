n = int(input())
ls = [[list(map(int,i.split(":"))) for i in list(input().split())] for _ in range(n)]
print(ls)

l = []
for i in ls:
    a,b = i
    l.append([a[0]*3600 + a[1]*60 + a[2], b[0]*3600 + b[1]*60 + b[2]])
print(l)

print(24*3600)

c = [0 for _ in range(86401)]
for a,b in l:
    c[a] += 1
    c[b] -= 1
import itertools
c = list(itertools.accumulate(c))
print(max(c))