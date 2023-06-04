n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int,input().split())))

import itertools
import math
A = list(range(n))
x = 0
c = list(itertools.combinations(A, 2))
for l in c:
    y = math.sqrt((ls[l[0]][0]-ls[l[1]][0])**2+(ls[l[0]][1]-ls[l[1]][1])**2)   #距離
    x = max(x,y)
print(x)