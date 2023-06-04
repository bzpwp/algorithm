n = int(input())
def func(a,b,c,d,e,f,g,h,i,j): #j = n
    if j == 1:
        return a+b+c+d+e+f+g+h+i
    else:
        newa = a+b
        newb = a+b+c
        newc = d+b+c
        newd = d+e+c
        newe = d+e+f
        newf = g+e+f
        newg = g+h+f
        newh = g+h+i
        newi = h+i
        a = newa
        b = newb
        c = newc
        d = newd
        e = newe
        f = newf
        g = newg
        h = newh
        i = newi
        j -= 1
        func(a,b,c,d,e,f,g,h,i,j)
print((func(1,1,1,1,1,1,1,1,1,n))%998244353)