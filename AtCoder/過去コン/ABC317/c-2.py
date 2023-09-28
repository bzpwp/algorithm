n,m = map(int,input().split())

roads = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    roads[a-1][b-1] = max(c,roads[a-1][b-1])
    roads[b-1][a-1] = max(c,roads[b-1][a-1])

A = 0

import itertools

ord = list(itertools.permutations([_ for _ in range(n)]))

for o in ord:
    a = 0
    for i in range(n-1):
        if roads[o[i]][o[i+1]]:
            a += roads[o[i]][o[i+1]]
        else:
            break
    
    A = max(A, a)
print(A)