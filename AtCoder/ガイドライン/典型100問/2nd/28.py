n = int(input())

from collections import defaultdict

dd = defaultdict(list)
for i in range(n):
    u,k,*v = map(int(input().split()))
    dd[u] = v



