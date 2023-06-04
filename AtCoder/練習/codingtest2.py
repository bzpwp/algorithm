a,b = input().split()
x = ""
b += str(0)
if a == "compress":
    c = 1
    d = 0
    e = ""
    while len(b)>2:
        while b[0]==b[1]:
            e = b[0]
            c += 1
            b = b[1:]
            if len(b)<3:
                break
        if c > 1:
            x += str(c)+e
        c = 1
        e = ""
        if len(b)<3:
            break
        while b[0]!=b[1]:
            e += b[0]
            d -= 1
            b = b[1:]
            if len(b)<3:
                break
        if d < 0:
            x += str(d)+e
        d = 0
        e = ""
        if len(b)<3:
            break
    print(x)