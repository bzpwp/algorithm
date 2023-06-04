n,m  = map(int, input().split())

import itertools

x = list(itertools.combinations(range(1,m+1), n))

for l in x:
    print(*l)