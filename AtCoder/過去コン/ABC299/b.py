n,t = map(int,input().split())
lsc = list(map(int, input().split()))
lsr = list(map(int, input().split()))

from collections import defaultdict

dd = defaultdict(list)
for i in range(n):
    dd[lsc[i]].append(i)
x = 0
w = 0
if dd[t] != []:
    for i in dd[t]:
        if x < lsr[i]:
            w = i
            x = lsr[i]
    print(w+1)
else:
    for i in dd[lsc[0]]:
        if x < lsr[i]:
            w = i
            x = lsr[i]
    print(w+1)