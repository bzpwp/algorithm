n = int(input())
l = len(str(n)) #桁数
s = len(str(n))
x = 0
while l >= 1:
    y = 10**(l-1)
    x += sum(range(y, 9*y)
    l -= 1
x -= sum(range(n+1,10**s))
print(x%998244353)