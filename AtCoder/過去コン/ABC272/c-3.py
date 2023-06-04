n = int(input())
ls = list(map(int,input().split()))

if n ==2:
    s = sum(ls)
    if s%2==1:
        print(-1)
    else:
        print(s)
else:
    ls.sort(reverse = True)
    a = ls[0]
    b = ls[1]
    c = ls[2]
    s0 = a+b
    s1 = a+c
    s2 = b+c
    if s0%2==0:
        print(s0)
    else:
        if s1%2==0:
            print(s1)
        else:
            if n == 3:
                print(s2)
            else:
                s3 = 0
                if a % 2==1:
                    for i in range(3,n):
                        if ls[i]%2==1:
                            s3 = a+ls[i]
                            break
                else:
                    for i in range(3,n):
                        if ls[i]%2==0:
                            s3 = a+ls[i]
                            break
                print(max(s2,s3))