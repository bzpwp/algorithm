t = int(input())



for i in range(t):
    n,d,k = map(int,input().split())
    if k == 1:
        print(0)
    else:
        if n == d:
            print(k-1)
        elif n%d == 0:
            # print("---")
            x = n//d #1週当たりの回数
            y = ((k-1)//x) + 1 #何週目か
            z = (k-1)%x #その何番目か
            if z == 0:
                z += x
                y -= 1
            # print(x,y,z)
            print(d*z + y-1)
        else:
            # x = n//d #1週当たりの回数
            # y = (k-1//x) + 1 #何週目か
            # z = (k-1)%x #その何番目か
            # if z == 0:
            #     z += x
            #     y -= 1
            print(d*(k-1)%n)