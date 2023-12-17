h,w = map(int,input().split())
grid_a = [list(map(int,input().split())) for _ in range(h)]
grid_b = [list(map(int,input().split())) for _ in range(h)]

answer = 10**10
import copy

for i in range(2**(h-1)):
    for j in range(2**(w-1)):
        how_many = 0
        A = copy.deepcopy(grid_a)
        for k in range(h-1):
            if (i>>k) & 1:
                how_many += 1
                A[k],A[k+1] = A[k+1],A[k]
        for k in range(w-1):
            if (j>>k) & 1:
                how_many += 1
                for row in A:
                    row[k],row[k+1] = row[k+1],row[k]
        if A == grid_b:
            answer = min(answer,how_many)
    

if answer == 10**10:
    print(-1)
else:
    print(answer)