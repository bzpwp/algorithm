n,k = map(int, input().split())
ls = list(map(int, input().split()))
x = 5*10**5
for a in range(k):
    for b in range(k,n):
        if ls[a] < ls[b]:
            x = min(x,b-a)
            break
if x == 5*10**5:
    print(-1)
else:
    print(x)