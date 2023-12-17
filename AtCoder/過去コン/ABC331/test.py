
from sortedcontainers import SortedSet, SortedList, SortedDict
S = SortedList([3])

from collections import defaultdict
dd = defaultdict(list)

dd[1] = S
dd[1].discard(3)
print(S)
print(dd)
if dd[1]:
    print("aa")
if dd[2]:
    print("bb")