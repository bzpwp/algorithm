n,q = map(int, input().split())
lsa = list(map(int, input().split()))
lsa.sort()
from itertools import accumulate
import bisect

lsa_s = list(accumulate(lsa))

# print(lsa)
# print(lsa_s)

for i in range(q):
    x = int(input())
    l = bisect.bisect_left(lsa, x)
    r = bisect.bisect_right(lsa, x)
    # print(l,r)
    if l == 0:
        print(lsa_s[n-1]-n*x)
    elif r == n:
        print(n*x-lsa_s[n-1])
    else:
        print(x*l-lsa_s[l-1]+lsa_s[n-1]-lsa_s[r-1]-x*(n-r))