n,x = map(int,input().split())
ls = list(map(int,input().split()))

S = sum(ls)
M = max(ls)
m = min(ls)

if S - m < x:
    print(-1)
else:
    if S - M >= x:
        print(0)
    else:
        # print("---")
        print(x-(S-M-m))