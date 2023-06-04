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
    s = a+b
    c = ls[2]
    d = b+c
    if s%2==0:
        print(s)
    else:
        if n == 3:
            if a%2==1:
                if c%2==1:
                    print(a+c)
                else:
                    print(d)
            else:
                if c%2==1:
                    print(d)
                else:
                    print(a+c)
        else:
            if a%2==1:
                