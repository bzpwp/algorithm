n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int,input().split())))
import math

def length(c,d):
    return math.sqrt((c[0]-d[0])**2+(c[1]-d[1])**2)


x = 0
for a in range(n-1):
    for b in range(a+1,n):
        x = max(x,length(ls[a],ls[b]))
print(x)