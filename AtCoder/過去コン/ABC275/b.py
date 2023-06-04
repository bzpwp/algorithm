a,b,c,d,e,f = map(int,input().split())

M = 998244353
a = a%M
b = b%M
c = c%M
d = d%M
e = e%M
f = f%M
x = a*b%M
x = x*c%M
y = d*e%M
y = y*f%M
z = x-y
if z >= 0:
    print(z)
else:
    print(z+M)