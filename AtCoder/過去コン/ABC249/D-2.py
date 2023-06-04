n = int(input())
ls = list(map(int, input().split()))
from collections import Counter
ls.sort()
c=Counter(ls)
l = list(c.keys())
a = len(l)
x = []
for k in range(a):
    for j in range(k,a):
        for i in range(j,a):
            if l[i]/l[j]==l[k]:
                x.append([i,j,k])
print(x)
y = 0
for b in x:
    d = c[b[0]]*c[b[1]]*c[b[2]]
    print(c)
    print(b[1])
    print(c[b[1]])
    if b[2]<b[1]:
        y += d*2
    else:
        y += d
    
print(y)