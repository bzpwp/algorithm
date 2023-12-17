h,w = map(int,input().split())
grid_a = [list(map(int,input().split())) for _ in range(h)]
grid_b = [list(map(int,input().split())) for _ in range(h)]

answer = 10**10
import copy
import itertools
changes_r = list(itertools.combinations(list(range(h)),2))
changes_g = list(itertools.combinations(list(range(w)),2))

# print(changes_r)
# print(changes_g)

# for i in range(8,9):
for i in range(2**len(changes_r)):
    how_many = 0
    A = copy.deepcopy(grid_a)
    for k in range(len(changes_r)):
        if (i >> k) & 1:
            # print(i>>k)
            how_many += 1
            x,y = changes_r[k]
            # print(x,y,"row")
            A[x],A[y] = A[y],A[x]
    # print(A)
    for j in range(2**len(changes_g)):
        A2 = copy.deepcopy(A)
        how_many2 = copy.copy(how_many)
        for k in range(len(changes_g)):
            if (j >> k) & 1:
                how_many2 += 1
                x,y = changes_g[k]
                for row in A2:
                    row[x],row[y] = row[y],row[x]
        # print(A)
        if A2 == grid_b:
            answer = min(answer,how_many2)
        if how_many2 == 4:
            print(i,j)


if answer == 10**10:
    print(-1)
else:
    print(answer)