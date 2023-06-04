n = int(input())

import sys
sys.setrecursionlimit(100000)
from functools import lru_cache

@lru_cache(maxsize=100000)
def saiki(x):
    if x == 0:
        return 1
    else:
        a = x//2
        b = x//3
        return saiki(a)+saiki(b)

print(saiki(n))