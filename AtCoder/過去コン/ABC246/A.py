x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

x4 = 0
y4 = 0

if x1 == x2:
    if y3 == y1:
        x4 = x3
        y4 = y2
    else:
        x4 = x3
        y4 = y1
elif x2 == x3:
    if y3 == y1:
        x4 = x1
        y4 = y2
    else:
        x4 = x1
        y4 = y3
else:
    if y1 == y2:
        x4 = x2
        y4 = y3
    else:
        x4 = x2
        y4 = y1
print(x4, y4)