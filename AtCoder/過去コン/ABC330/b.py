n,l,r = map(int,input().split())
ls = list(map(int,input().split()))

for i in ls:
    if i <= l:
        print(l)
    elif i >= r:
        print(r)
    else:
        print(i)