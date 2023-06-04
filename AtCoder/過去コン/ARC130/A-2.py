n = int(input())
s = input()
wls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x = 0
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
for c in range(wls):
    for i in range(2,len(s)+1):
        y = s.count(c*i)
        if y!=0:
            x += combinations_count(n, r)

