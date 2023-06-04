x,a,d,n = map(int, input().split())

if d == 0:
    print(abs(x-a))

else:
    x1 = (x-a)%d
    if d >= 0:
        if x <= a:
            print(a-x)
        elif x >= a + (n-1)*d:
            print(x - a - (n-1)*d)
        elif x1 == 0:
            print(0)
        else:
            print(min(abs(x1),abs(d-x1)))

    else:
        if x <= a + (n-1)*d:
            print(a + (n-1)*d -x)
        elif x >= a:
            print(x -a)
        elif x1 == 0:
            print(0)
        else:
            print(min(abs(x1),abs(d-x1)))