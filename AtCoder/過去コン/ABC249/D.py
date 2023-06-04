n = int(input())
ls = list(map(int, input().split()))
from collections import Counter

c=Counter(ls)
c_sorted = sorted(c.items(), key=lambda x:x[0])
l = []
for m in c_sorted:
    l.append(m[0])
a = len(l)
x = []
for k in range(a):
    for j in range(k,a):
        for i in range(j,a):
            if l[i]/l[j]==l[k]:
                x.append([i,j,k])

y = 0
for b in x:
    d = c_sorted[b[0]][1]*c_sorted[b[1]][1]*c_sorted[b[2]][1]
    if b[2]<b[1]:
        y += d*2
    else:
        y += d
    
print(y)