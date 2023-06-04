a,b = map(int, input().split())

x = 0

# import math
# y = math.gcd(a, b)

# a //= y
# b //= y

while not (a%b==0 or b%a==0):
    if a > b:
        x += a//b
        a %= b
    else:
        x += b//a
        b %= a




if a >= b:
    x += a//b
    x -= 1
else:
    x += b//a
    x -= 1
print(x)