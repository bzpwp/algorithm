a,b,c,x,y=map(int,input().split())
s = a*x + b*y
if 2*c < a:
    if x > y:
        s = 2*c*x
    elif 2*c < b:
        s = 2*c*max(x,y)
    else:
        s = 2*c*x + (y-x)*b
elif 2*c < b:
    if x > y:
        s = 2*c*y + (x-y)*a
    elif 2*c < a:
        s = 2*c*max(x,y)
    else:
        s = 2*c*x
elif 2*c < a + b:
    s -= min(x,y)*(a+b)
    s += min(x,y)*2*c
    if x > y:
        if a > 2*c:
            s -= (x-y)*a
            s += (x-y)*2*c
    if x < y:
        if b > 2*c:
            s -= (x-y)*a
            s += (x-y)*2*c
print(s)