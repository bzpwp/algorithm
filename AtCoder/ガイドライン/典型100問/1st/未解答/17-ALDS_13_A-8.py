k = int(input())

import itertools

lsc = list(itertools.combinations(list(range(64)),8-k))

lsc_n = []
for i in lsc:
    ls = []
    for j in i:
        ls.append([j//8,j%8])
    lsc_n.append(ls)


board = [["."]*8 for i in range(8)]
for i in range(k):
    x,y = map(int,input().split())
    board[x-1][y-1]="Q"

# for l in lsc_n:
    