n = int(input())
slist = set([])
tlist = set([])
from collections import defaultdict
dd = defaultdict(str)

for i in range(n):
    s,t = input().split()
    dd[t]=s
    slist.add(s)
    tlist.add(t)
    
for i in tlist:
    if i not in slist:
        slist.remove(dd[i])

if s == set([]):
    print("Yes")
else:
    print("No")