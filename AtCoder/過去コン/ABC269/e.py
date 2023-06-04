n = int(input())
ls = [True,True]
print("?",1,n//2,1,n)
a = 1
b = n
c = 1
d = n
ans = []
while ls[0]:
    t = int(input())
    if a ==b:
        if t==0:
            ans.append(a+1)
        else:
            ans.append(a)
        ls[0]=False
    if t <= b-a:
        a = b+1
        b += b-a+1
    elif t > b-a:
        b = (a+b)//2
    print("?",a,b,c,d)

while ls[1]:
    t = int(input())
    if c ==d:
        if t==0:
            print(ans[0],c+1)
            exit()
        else:
            print(ans[0],c)
            exit()
        ls[0]=False
    if t <= d-c:
        c = d+1
        d += d-c+1
    elif t > d-c:
        d = (c+d)//2
    print("?",a,b,c,d)