n,x,y = map(int, input().split())
ls = list(map(int,input().split()))


if n%2 == 0:
    dp1 = [list(False for _ in range(2*10**4+1)) for i in range(n//2+1)]
    dp2 = [list(False for _ in range(2*10**4+1)) for i in range(n//2)]
    dp1[0][10**4]=True
    dp2[0][10**4]=True
    dp2[0][10**4+ls[0]]=True
    for i in range(1,n//2+1):
        move = ls[i*2-1]
        for j in range(2*10**4+1):
            if dp1[i-1][j]:
                target1 = j + move
                target2 = j - move
                dp1[i][target1]=True
                dp1[i][target2]=True
    if n != 2:
        for i in range(1,n//2):
            move = ls[i*2]
            for j in range(2*10**4+1):
                if dp2[i-1][j]:
                    target1 = j + move
                    target2 = j - move
                    dp2[i][target1]=True
                    dp2[i][target2]=True
    if dp1[n//2][x+10**4] and dp2[n//2-1][y+10**4]:
        print("Yes")
    else:
        print("No")