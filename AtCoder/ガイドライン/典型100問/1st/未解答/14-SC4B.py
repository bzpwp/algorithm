n,k = map(int,input().split())
ls = list(map(int,input().split()))

import itertools

lsc = list(itertools.combinations(list(i for i in range(n)),k))

