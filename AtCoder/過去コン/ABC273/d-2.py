h,w,rs,cs = map(int, input().split())
grid1 = [[0]*w for _ in range(h)]
grid2 = [[0]*h for _ in range(w)]
n = int(input())
for i in range(n):
    r,c =  map(int, input().split())
    grid1[r-1][c-1]=1
    grid2[c-1][r-1]=1

import itertools
for i in range(h):
    l = grid1[i]
    l = list(itertools.accumulate(l))
    grid1[i]=l
for i in range(w):
    l = grid2[i]
    l = list(itertools.accumulate(l))
    grid2[i]=l

import bisect
q = int(input())
for i in range(q):
    d,l = input().split()
    l = int(l)
    if d == "L":
        ls = grid1[rs-1]
        x = ls[cs-1]
        index = bisect.bisect_left(ls,x)
        if index+1 >=cs-1-l:
            cs = index+2
        else:
            cs = max(1,cs-l)
            