n = int(input())
ls = list(map(int,input().split()))

x = []

c = set([])

for i in range(3*n):
    if ls[i] not in c:
        c.add(ls[i])
    else:
        x.append(ls[i])
        c.remove(ls[i])

print(*x)