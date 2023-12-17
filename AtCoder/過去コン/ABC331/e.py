n,m,l = map(int,input().split())
al = list(map(int,input().split()))
bl = list(map(int,input().split()))

from collections import defaultdict
dd = defaultdict(list)


from sortedcontainers import SortedList
S = SortedList(list(i for i in range(1,m+1)))

for i in range(1,n+1):
    dd[i] = S.copy()



bl2 = [[bl[i], i+1] for i in range(m)]
bl2.sort()
change_ind = defaultdict(int)
for i in range(m):
    change_ind[bl2[i][1]] = i+1
# print(bl2)
# print(change_ind)


for _ in range(l):
    c,d = map(int,input().split())
    dd[c].discard(change_ind[d])

# print(dd)
x = 0
for i in range(1,n+1):
    if dd[i]:
        x = max(al[i-1]+bl2[dd[i][-1]-1][0], x)
print(x)