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
from functools import lru_cache
@lru_cache
def func(a):
    dd[a]=dd[math.floor(a/2)]*dd[math.ceil(a/2)]
print(dd[x]%998244353)