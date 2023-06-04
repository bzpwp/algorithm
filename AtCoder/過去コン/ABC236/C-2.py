s,m = map(int,input().split())
ls = list(input().split())
lt = list(input().split())
x = 0
list = list(range(m))
for a in ls:
    for b in list(range(x,m)):
        if lt[b]==a:
            print("Yes")
            x = b
            break
        print("No")