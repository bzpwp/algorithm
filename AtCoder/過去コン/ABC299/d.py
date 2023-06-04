n = int(input())
x = n//2
y = 1
z = n
while True:
    print("?",x)
    a = int(input())
    if z-y == 1:
        print("!",y)
        exit()
    elif a == 0:
        y = x
        x = (y+z)//2
    else:
        z = x
        x = (y+z)//2