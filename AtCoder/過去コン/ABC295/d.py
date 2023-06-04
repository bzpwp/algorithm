s = input()
from collections import defaultdict
d = [[0 for _ in range(len(s))] for _ in range(9)]
dd = defaultdict(list)
for i in range(len(s)):
    d[s[i]].append(i)

for a in dd:

    rca