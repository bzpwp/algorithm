l,r = map(int, input().split())
m = int(input())
ls1 = list(map(int,input().split()))

if 1 in ls1:
    print(0)
else:
    ls3 = []
    for i in ls1:
        if l%i==0:
            if l//i == 0:
                a = 1
            else:
                a = l//i
        else:
            a = l//i+1
        b = r//i
        ls3.extend([i*j for j in range(a,b+1)])
    print(r-l-len(list(set(ls3)))+1)