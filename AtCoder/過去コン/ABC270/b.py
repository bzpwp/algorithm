x,y,z= map(int,input().split())

if 0 < x:
    if 0 < y < x:
        if y < z :
            print(-1)
        else:
            if z > 0:
                print(x)
            else:
                print(-z*2+x)
    else:
        print(x)
else:
    if y > 0:
        print(-x)
    else:
        if y < x:
            print(-x)
        else:
            if z < y:
                print(-1)
            else:
                if z < 0:
                    print(-x)
                else:
                    print(z*2-x)