s = input()

n = len(s)

wls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

from collections import defaultdict

wdd = defaultdict(int)
for i in range(26):
    wdd[wls[i]]=i

A = 0
for i in range(n-1):
    A += 26**(i+1)

for i in range(n):
    x = wdd[s[i]]
    A += (26**(n-i-1))*x

print(A+1)