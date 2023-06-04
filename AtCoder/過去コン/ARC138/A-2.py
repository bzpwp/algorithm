n,k = map(int, input().split())
ls = list(map(int, input().split()))
m = min(ls[:k])
a = ls.index(m)
b = k
x = 5*10**5
if m >= max(ls[k:]):
    print(-1)
else:
    while a <= n:
        m = min(ls[a:k])
        for a in ls[b:n]:
            if m < a:
                x = min(x,b-