x = int(input())
from collections import deque
import math
import sys
from xml.sax import xmlreader
sys.setrecursionlimit(1000000000)
ans = 1
def func(a):
    global ans
    if a == 1 or a == 2 or a == 3 or a ==4:
        ans *= a
        return
    else:
        func(math.floor(a/2))
        func(math.ceil(a/2))
func(x)
print(ans%998244353)