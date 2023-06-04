n = int(input())
lsr = list(map(int, input().split()))
lsc = list(map(int, input().split()))
q = int(input())
lsrc = []
for q in range(q):
    lsrc.append(list(map(int,input().split())))
import itertools
lsr_sel = []
for i in range(n):
    a = list(itertools.combinations(list(range(n)), lsr[i]))
    lsr_sel.append(a)
how_sel = list(itertools.product(*lsr_sel))
for ls in how_sel:
    x = 0
    for a in range(n):
        y = 0
        for b in range(n):
            if a in ls[b]:
                y += 1
        if y == lsc[a]:
            x += 1
    if x == n:
        s = ""
        for c in range(q):
            if lsrc[c][1]-1 in ls[lsrc[c][0]-1]:
                s += "#"
            else:
                s +="."
        print(s)