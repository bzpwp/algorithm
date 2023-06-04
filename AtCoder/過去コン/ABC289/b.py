n,m = map(int,input().split())
la = list(map(int,input().split()))

import copy
A = []
i = 0
last = 0
point = 0
while len(A) < n:
    last = copy.copy(i)
    i += 1
    while i in la:
        i += 1
    point = copy.copy(i)
    while point > last:
        A.append(point)
        point -= 1



print(*A)