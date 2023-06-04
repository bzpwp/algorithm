ls = []
q = int(input())
from collections import defaultdict
dd = defaultdict(list)
for i in range(q):
    try:
        op, x = input().split()
        x = int(x)
        if op == "ADD":
            ls.append(x)
        elif op == "SAVE":
            dd[x]=ls.copy()
        else:
            ls = dd[x]
    except:
        try:
            ls.pop()
        except:
            print(-1)
            continue
    try:
        print(ls[-1])
    except:
        print(-1)