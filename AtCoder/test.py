a,b = map(int,input().split())
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