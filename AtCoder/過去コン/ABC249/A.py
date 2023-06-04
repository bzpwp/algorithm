a,b,c,d,e,f,x = map(int, input().split())

g = x//(a+c)
h = x%(a+c)
if h < a:
    t = a*b*g+h*b
else:
    t = a*b*(g+1)

i = x//(d+f)
j = x%(d+f)
if j < d:
    u = d*e*i+j*e
else:
    u = e*d*(i+1)


if t == u:
    print("Draw")
elif t > u:
    print("Takahashi")
else:
    print("Aoki")
