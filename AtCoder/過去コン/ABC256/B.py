n = int(input())
ls = list(map(int,input().split()))
import numpy as np

l = np.array([])
for i in ls:
    l = np.append(l,0)
    l += i

l = list(l)
x = 0
for i in l:
    if i >=4:
        x +=1

print(x)