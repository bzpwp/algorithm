s,m = map(int,input().split())
ls = list(input().split())
lt = list(input().split())
for x in ls:
    if x == lt[0]:
        print("Yes")
        lt.pop(0)
    else:
        print("No")