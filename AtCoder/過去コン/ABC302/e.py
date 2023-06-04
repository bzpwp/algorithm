n,q = map(int,input().split())

from collections import defaultdict

dd = defaultdict(set)

for i in range(q):
    x, *y = input()
    if x == "1":
        u,v = int(y[1]), int(y[3])
        dd[u].add(v)
        dd[v].add(u)
        # print("--a",len(dd),dd)
        print(n-len(dd))
    
    else:
        v = int(y[1])
        for j in dd[v]:
            z = dd[j]
            z.remove(v)
            if len(z) == 0:
                del dd[j]
            else:
                dd[j] = z
        del dd[v]
        # print(dd)
        print(n-len(dd))