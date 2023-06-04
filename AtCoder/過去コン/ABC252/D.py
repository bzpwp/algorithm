n=int, input().split()
lsa = list(map(int, input().split()))

import collections
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

c = collections.Counter(lsa)
print(c)
va = list(c.values())
dva = collections.Counter(va)
print(dva)
print(va)
l = len(va)
x = 0

for key, value in dva.items():
    if key > 
    x += x*(key-1)*value


print(combinations_count(len(lsa), 3)-x)
