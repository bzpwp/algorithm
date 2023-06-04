a,b = map(int,input().split())

x = 0
if a>=4 or b>=4:
    x += 4
a = a%4
b = b%4
if a >= 2 or b >= 2:
    x += 2
a = a%2
b = b%2
if a >= 1 or b >= 1:
    x += 1

print(x)