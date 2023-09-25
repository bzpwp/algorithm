a,b,x = map(int,input().split())
import math

e = math.acos(a/math.sqrt(a**2 + b**2)) #角

if x > ((a**2)*b)/2:
    s = a*math.sqrt(a**2 + b**2)
    y = x - ((a**2)*b)/2
    print(y)
    # (s * d)/2 = y
    d = y*2/s #高さ
    print(d)
    
    # f*math.cos(x) = a
    # f*math.sin(e-x) = d
    # f = d/(sin(e)cos(x) - cos(e)sin(x))
    # a/cos(x) = d/(sin(e)cos(x) - cos(e)sin(x))
    # a*(sin(e)cos(x) - cos(e)sin(x)) = d*cos(x)
    # (a*sin(e)-d)cos(x) = a*cos(e)*sin(x)
    # tan(x) = (a*sin(e)-d)/a*cos(e)
    print(math.degrees(math.atan((a*math.sin(e)-d)/a*math.cos(e))))
else:
    # print("a")
    # (x * 2 / b)/a #底辺
    # print(b)
    # print(((x * 2 / b)/a))
    print(math.degrees(math.atan(b/((x * 2 / b)/a))))
