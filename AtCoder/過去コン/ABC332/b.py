k,g,m = map(int,input().split())

a = 0
b = 0

def operate(x,y):
    if x == g:
        x = 0
    elif y == 0:
        y = m
    else:
        if g-x>=y:
            x += y
            y = 0
        else:
            y -= g-x
            x = g
    return x,y

for _ in range(k):
    a,b = operate(a,b)
    # print(a,b,_)
print(a,b)