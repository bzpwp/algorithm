n,k = map(int, input().split())
ls = list(map(int, input().split()))
x = 5*10**5
c = n
for a in range(k):
    for b in range(k,c):
        if ls[a] < ls[b]:
            x = min(x,b-a)
            c = b
            break
if x == 5*10**5:
    print(-1)
else:
    print(x)