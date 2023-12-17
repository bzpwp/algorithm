n,q = list(map(int,input().split()))
s = input()

ls = []
for i in range(n-1):
    if s[i] == s[i+1]:
        ls.append(1)
    else:
        ls.append(0)

import itertools
acc = list(itertools.accumulate(ls))

x = [0]
x += acc
for i in range(q):
    l,r = map(int,input().split())
    l -= 1
    r -= 1
    print(x[r]-x[l])