x = int(input())
from collections import defaultdict
import math
import sys
sys.setrecursionlimit(1000000000)
start = 5
dd=defaultdict()
dd[1]=1
dd[2]=2
dd[3]=3
dd[4]=4
while start<=x:
    dd[start]=dd[math.floor(start/2)]*dd[math.ceil(start/2)]
    start+=1
print(dd[x]%998244353)