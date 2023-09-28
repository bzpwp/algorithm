n = int(input())
s1 = input()
s2 = input()
s3 = input()

import bisect
# import copy
x = 10**10
for i in range(10):
    a = [j for j in range(n) if s1[j] == str(i)]
    b = [j for j in range(n) if s2[j] == str(i)]
    c = [j for j in range(n) if s3[j] == str(i)]
    
    if a and b and c:
        # ls = list(set(a+b+c))
        # ls.sort()
        # y = a[0]
        # bind = bisect.bisect_left(b,y)
        # if bind == len(b):
        #     y = b[0] + n
        #     cind = bisect.bisect_left(b,y-n)
        #     if cind == len(c) or c[cind] == y-n:
        #         y = c[0] + n*2
        #         x = min(x,c)
        #     else:
        #         y = c[cind] + n

        for _ in range(3):
            d = a.copy()
            e = b.copy()
            f = c.copy()    
            y = d[0]
            while e[0] <= y:
                item = e.pop(0)
                e.append(item+n)
            y = e[0]
            while f[0] <= y:
                item = f.pop(0)
                f.append(item+n)
            y = f[0]
            x = min(x,y)          
            a,b,c = b,c,a     

        for _ in range(3):
            d = a.copy()
            e = c.copy()
            f = b.copy()    
            y = d[0]
            while e[0] <= y:
                item = e.pop(0)
                e.append(item+n)
            y = e[0]
            while f[0] <= y:
                item = f.pop(0)
                f.append(item+n)
            y = f[0]
            x = min(x,y)          
            a,b,c = b,c,a  


        


if x == 10**10:
    print(-1)
else:
    print(x)