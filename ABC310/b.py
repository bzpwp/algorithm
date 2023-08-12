n,m = map(int,input().split())

from collections import defaultdict

P = defaultdict(int)
F = defaultdict(set)

for i in range(n):
    p,c,*f = map(int,input().split())
    P[i] = p
    F[i] = set(f)

for i in range(n-1):
    for j in range(i+1, n):
        if P[i] >= P[j]:
            if F[i].issubset(F[j]):
                if P[i] > P[j] or len(F[j])-len(F[i])>=1:
                    print("Yes")
                    exit()
        elif P[j] >= P[i]:
            if F[j].issubset(F[i]):
                if P[j] > P[i] or len(F[i])-len(F[j])>=1:
                    print("Yes")
                    exit()
print("No")