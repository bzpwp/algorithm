n,m = map(int,input().split())
lsa = []
for i in range(m):
    lsa.append(list(map(int,input().split())))

import itertools

ans = 1

# print("lsa",lsa)

for i in range(2**n):
    ls = []
    for j in range(n):
        if (i >> j)&1:
            ls.append(j+1)
    c =list(itertools.combinations(ls,2))
    # print(i)
    # print(c)
    x = len(c)
    y = 0
    for l in c:
        l = list(l)
        # print(l)
        if l in lsa:
            y += 1
    # print(y)
    if y == x:
        ans = max(ans,len(ls))

print(ans)