h,m = map(int,input().split())

for i in range(1440):
    if h <= 9:
        if h >= 0 and h <= 5:
            print(h,m)
            exit()
    elif h >= 10 and h < 20:
        if h - 10 <= 5:
            print(h,m)
            exit()
    else:
        if m//10 < 4:
            print(h,m)
            exit()
    m += 1
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    