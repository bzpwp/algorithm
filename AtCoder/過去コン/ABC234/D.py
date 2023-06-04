n, k = map(int,input().split())
ls = list(map(int, input().split()))
lsi = list(range(k,n+1))
for i in lsi:
    x = ls[:i]
    x.sort(reverse = True)
    print(x[k-1])