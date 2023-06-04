n = int(input())
x = 1
y = 0 #桁数
z = 0
a = 10
while x<=n:
    if a<=x:
        y += 1
        a = 10**(y+1)
    z += x-10**y+1
    x += 1
print(z%998244353)