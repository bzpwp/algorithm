n = int(input())
lsr = list(map(int, input().split()))
lsc = list(map(int, input().split()))
q = int(input())
lsrc = []
for q in range(q):
    lsrc.append(list(map(int,input().split())))
import itertools
lsr_sel = []
how_sel = []
for i in range(n):
    a = list(itertools.combinations(list(range(n)), lsr[i]))
    lsr_sel.append(a)
    how_sel.append(len(a))
how_sel2 = []
for i in range(n):
    how_sel2.append(list(range(how_sel[i])))
how_sel3 = list(itertools.product(*how_sel2))
for ls in how_sel3:
    sol = []
    for i in range(n):
        sol.append(lsr_sel[i][ls[i]])
        x = 0
        for j in range(n):
            y = 0
            for k in range(n):
                y += sol[k].count(j)
            if y == lsc[j]:
                x += 1
        if x == n:
            s = 0
            for l in lsrc:
                if l[1]-1 in sol[ls[0]-1]:
                    s+="#"
                else:
                    s+="."
            print(s)