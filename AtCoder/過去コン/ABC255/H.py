n,q  = map(int, input().split())

M = 998244353

import numpy as np
l=np.array(range(1,n+1),dtype="int64")
ls = np.array(range(1,n+1),dtype="int64") #初期

for i in range(q):
    d,l,r = map(int, input().split())
    ls += l*(d-1)
    ls = ls%M
    print(sum(ls[l-1:r]))
    for j in range(l-1,r):
        ls[j]=0