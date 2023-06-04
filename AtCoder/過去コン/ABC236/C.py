s,m = map(int,input().split())
ls = list(input().split())
lt = list(input().split())
x = 0
for c in ls:
    if c in lt[x:]:
        print("Yes")
        x = lt.index(c)
    else:
        print("No")