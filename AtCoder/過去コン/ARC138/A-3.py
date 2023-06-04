n,k = map(int, input().split())
ls = list(map(int, input().split()))
a = 0
b = k
x = 5*10**5
while a <= k-1:
    m = min(ls[a:k])
    a += ls[a:k].index(m)
    d = 0
    for c in ls[b:n]:
        if d == n-b:
            if x == 5*10**5:
                print(-1)
                exit()
            else:
                print(x)
                exit()
        elif m < c:
            b += ls[b:n].index(c)
            x = min(x,b-a)
            break
        else:
            d += 1
    a += 1
if x == 5*10**5:
    print(-1)
else:
    print(x)