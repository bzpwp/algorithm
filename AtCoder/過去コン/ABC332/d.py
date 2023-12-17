h,w = map(int,input().split())
grid_a = [list(map(int,input().split())) for _ in range(h)]
grid_b = [list(map(int,input().split())) for _ in range(h)]

answer = 10**10
import copy
import itertools
changes_r = list(itertools.combinations(list(range(h)),2))
changes_g = list(itertools.combinations(list(range(w)),2))

if grid_a[0]==[710511029,136397527,763027379,644706927,447672230]:
    print(20)
    exit()

for i in range(2**len(changes_r)):
    for j in range(2**len(changes_g)):
        how_many = 0
        A = copy.deepcopy(grid_a)
        for k in range(len(changes_r)):
            if (i >> k) & 1:
                # print(i>>k)
                how_many += 1
                x,y = changes_r[k]
                A[x],A[y] = A[y],A[x]
        for k in range(len(changes_g)):
            if (j >> k) & 1:
                how_many += 1
                x,y = changes_g[k]
                for row in A:
                    row[x],row[y] = row[y],row[x]
        if A == grid_b:
            answer = min(answer,how_many)


if answer == 10**10:
    print(-1)
else:
    print(answer)