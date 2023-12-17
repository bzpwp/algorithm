n = int(input())
r = input()
c = input()

# if r[0]!=c[0]:
#     print("No")
#     exit()

import itertools
from collections import Counter
choices = list(itertools.combinations(list(range(n)),3))

how_to = list(itertools.product(list(range(len(choices))), repeat=n))

# print(choices)
# print(len(how_to))
l = []
for i in range(3):
    l += list(range(n))
checkdict = Counter(l)
for order in how_to: #choicesからの選び方のインデックス
    grid = [["" for i in range(n)] for j in range(n)]
    all = []
    for o in order:
        all+=choices[o]
    count = Counter(all)
    if count != checkdict:
        continue
    #こっから背反
    for k in range(n):
        for x,y,z in choices[order[k]]:
            grid[k][l] = "A"