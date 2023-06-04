n = int(input())
ls = [int(input()) for _ in range(n)]

x = 10**18
for i in range(2**n):
    y = []
    z = []
    for j in range(n):
        if (i>>j)&1:
            y.append(ls[j])
        else:
            z.append(ls[j])
    x = min(x,max(sum(y),sum(z)))

print(x)