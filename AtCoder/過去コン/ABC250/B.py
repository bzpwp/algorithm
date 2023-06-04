n,a,b= map(int, input().split())
for i in range(a*n):
    w = ""
    if (i//a)%2 == 0: #白始まり
        if n % 2 == 1:
            for j in range(n//2):
                w += "."*b
                w += "#"*b
            w += "."*b
        else:
            for j in range(n//2):
                w += "."*b
                w += "#"*b
    elif (i//a)%2 == 1: #黒始まり
        if n % 2 == 1:
            for j in range(n//2):
                w += "#"*b
                w += "."*b
            w += "#"*b
        else:
            for j in range(n//2):
                w += "#"*b
                w += "."*b
    print(w)
        