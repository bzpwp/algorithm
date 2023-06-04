n,w = map(int, input().split())
ls = list(map(int, input().split()))

import itertools

l1 = list(itertools.combinations(range(n), 1))
l2 = list(itertools.combinations(range(n), 2))
l3 = list(itertools.combinations(range(n), 3))

lsn = []
for i in l1:
    x = ls[i[0]]
    if x <=w:
        lsn.append(x)
for i in l2:
    x = sum([ls[i[0]],ls[i[1]]])
    if x <=w:
        lsn.append(x)
for i in l3:
    x = sum([ls[i[0]],ls[i[1]],ls[i[2]]])
    if x <=w:
        lsn.append(x)

lsn = set(lsn)

print(len(lsn))
