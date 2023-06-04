n,m = map(int,input().split())
ls = []
for i in range(m):
    c = int(input())
    ls.append(set(list(map(int,input().split()))))
A = 0
ans = set(list(range(1,n+1)))

for i in range(2**m):
    s = set([])
    for j in range(10):
        if (i>>j) & 1:
            s |= ls[j]
    if s == ans:
        A += 1

print(A)