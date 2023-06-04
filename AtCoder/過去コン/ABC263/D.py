n,l,r = map(int, input().split())

ls = list(map(int, input().split()))

import itertools
lsx = itertools.accumulate(ls)
lsy = itertools.accumulate(ls.reverse())

