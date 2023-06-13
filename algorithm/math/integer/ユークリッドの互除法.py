# 最大公約数
import math
x,y = map(int,input().split())
math.gcd(x, y)

# ユークリッドの互除法
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

# 拡張ユークリッドの互除法

def extgcd(a, b):
    d = a
    if b != 0:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
    else:
        x = 1
        y = 0
    return d, x, y

# ax + by = 1

# 入力
a, b = map(int,input().split())

# 拡張ユークリッドの互除法
def extgcd(a, b):
    d = a
    if b != 0:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
    else:
        x = 1
        y = 0
    return d, x, y

d, x, y = extgcd(a, b)

print(d,x,y)
