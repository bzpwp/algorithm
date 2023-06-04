n = int(input())
ls = list(map(int,input().split()))

if len(ls)==1:
    if ls[0]%2==1:
        print(-1)
    else:
        print(ls[0])
if len(ls)==2:
    s = sum(ls)
    if s%2==1:
        print(-1)
    else:
        print(s)
else:
    ls.sort(reverse = True)
    a = ls[0]
    b = ls[1]
    if a%2==1:
        if b%2==1:
            print(a+b)
        else:
            c = ls[2]
            if c % 2==1:
                print(a+c)
            else:
                d = b+c
                if len(ls)==3:
                    print(d)
                else:
                    e = False
                    for i in range(3,n-1):
                        if ls[i]%2==1:
                            a += ls[i]
                            e = True
                            break
                    if e:
                        print(max(a,d))
                    else:
                        print(d)
    else:
        if b%2==0:
            print(a+b)
        else:
            c = ls[2]
            if c %2 ==0:
                print(a+c)
            else:
                d = b+c
                if len(ls)==3:
                    print(d)
                else:
                    e = False
                    for i in range(3,n-1):
                        if ls[i]%2==0:
                            a += ls[i]
                            e = True
                            break
                    if e:
                        print(max(a,d))
                    else:
                        print(d)
