n,m = map(int,input().split())
from collections import defaultdict
dd = defaultdict(set)
for i in range(m):
    a,b = map(int,input().split())
    dd[a].add(b)
    dd[b].add(a)
# print(dd)

A = 1
for i in range(2**n):
    check = True
    p = []
    for j in range(n):
        if (i>>j)&1:
            p.append(j+1)
    # print(p)
    # if p == [4,5,6,7]:
    #     print(p)
    for j in range(len(p)):
        for k in range(j+1,len(p)):
            if p[k] not in dd[p[j]]:
                check = False
                # if p == [4,5,6,7]:
                #     print(k,j,"---")
                break
        else:
            continue
        break
    if check:
        # print(p)
        A = max(A,len(p))

print(A)