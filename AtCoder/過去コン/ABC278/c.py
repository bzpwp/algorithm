n,q = map(int,input().split())

from collections import defaultdict

dd = defaultdict(set)
for i in range(q):
    t,a,b = map(int,input().split())
    if t == 1:
        dd[a].add(b)
    elif t == 2:
        try:
            dd[a].remove(b)
        except:
            pass
    else:
        # print(dd)
        if a in dd[b] and b in dd[a]:
            print("Yes")
        else:
            print("No")