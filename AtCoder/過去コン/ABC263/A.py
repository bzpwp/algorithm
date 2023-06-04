ls = list(map(int, input().split()))

s = list(set(ls))


if len(s)!=2:
    print("No")
else:
    a = s[0]
    b = s[1] 
    na = 0
    nb = 0
    for i in ls:
        if i == a:
            na += 1
        else:
            nb += 1
    if na == 3 and nb == 2:
        print("Yes")
    elif na == 2 and nb == 3:
        print("Yes")
    else:
        print("No")