n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

import itertools
c = list(itertools.permutations(list(range(1,n+1)),n))

for i in range(len(c)):
    if c[i]==p:
        a = i
    if c[i]==q:
        b = i
print(abs(a-b))