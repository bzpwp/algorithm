n,k = map(int,input().split())
ls = list(map(int,input().split()))

ans = 0
x = ls.pop()
turn = True
for i in range(10**4):
    if ls == [] and x > n:
        print(ans)
        exit()
    else:
        if n >= x:
            n -= x
            if turn:
                ans += x
                turn = False
            else:
                turn = True
        else:
            x = ls.pop()