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
def func(a):
    if a not in dd:
        if math.floor(a/2) in dd and math.ceil(a/2) in dd:
            dd[a]=dd[math.floor(a/2)]*dd[math.ceil(a/2)]
            return
        else:
            func(math.ceil(a/2))
            func(math.floor(a/2))
func(x)
if x <= 4:
    print(x)
else:
    print(dd[x]%998244353)