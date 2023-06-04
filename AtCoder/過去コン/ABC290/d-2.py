t = int(input())



for i in range(t):
    n,d,k = map(int,input().split())
    if k == 1:
        print(0)
    else:
        if n == d:
            print(k-1)
        elif n%d == 0:
            x = (k-1)*d
            y = x//n
            z = x%n + y - d
            if z < 0:
                print(z+d)
            else:
                print(z)
        else:
            print(d*(k-1)%n)