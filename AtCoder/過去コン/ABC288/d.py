n,k = map(int,input().split())
import numpy as np
ls = np.array(list(map(int,input().split())))
q = int(input())
for i in range(q):
    l,r = map(int,input().split())
    nl = ls[l:r+1]
    for j in nl:
        add = [-j]*k