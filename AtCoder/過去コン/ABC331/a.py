M,D = map(int,input().split())
y,m,d = map(int,input().split())

# x = d + m*D + y*M*D

# print(x//(M*D), (x%(M*D))//D, (x%D)+1)

if d != D:
    print(y,m,d+1)
else:
    if m!=M:
        print(y,m+1,1)
    else:
        print(y+1,1,1)