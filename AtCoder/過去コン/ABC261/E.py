from collections import defaultdict
dd = defaultdict(int)
dd[1]=1
dd[2]=0
dd[3]=0
order = [1,2,3]
n,c  = map(int, input().split())
ls = [] 
for i in range(n):
    t,a =  map(int, input().split())
    if t ==1:
        order.remove(1)
        order.append(1)
        x = dd[1]
        y = x&a
        dd[1]=y
        if order[0]==2:
            c = c|dd[2]
            c = c^dd[3]
        else:
            c = c^dd[3]
            c = c|dd[2]
        c = c&y
        print(c)
    elif t == 2:
        order.remove(2)
        order.append(2)
        x = dd[2]
        y = x|a
        dd[2] = y
        if order[0]==1:
            c = c&dd[1]
            c = c^dd[3]
        else:
            c = c^dd[3]
            c = c&dd[1]
        c = c|y
        print(c)
    else:
        order.remove(3)
        order.append(3)
        x = dd[3]
        y = x^a
        dd[3] = y
        if order[0]==1:
            print(c)
            c = c&dd[1]
            print(c)
            c = c|dd[2]
            print(c)
        else:
            c = c|dd[2]
            c = c&dd[1]
        c = c^y
        print(c)