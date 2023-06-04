n = int(input())

ls = []
for i in range(n):
    ls.append(list(map(int,input().split())))

    
import math
def length(a,b):
    c = ls[a]
    d = ls[b]
    return math.sqrt((c[0]-d[0])**2+(c[1]-d[1])**2)

import itertools

p = list(itertools.permutations(list(range(n)),n))

s = 0
for l in p:
    for i in range(n-1):
        a = l[i]
        b = l[i+1]
        s += length(a,b)
    
print(s/len(p))