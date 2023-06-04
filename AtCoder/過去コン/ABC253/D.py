n,a,b=map(int, input().split())

x = (1+n)*n/2
c = n//a
d = n//b
e = n//(a*b)

x -= (a+c*a)*c/2
x -= (b+d*b)*d/2
x += (a*b+e*a*b)*e/2

print(int(x))