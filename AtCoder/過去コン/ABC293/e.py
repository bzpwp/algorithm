a,x,m = map(int,input().split())

b = 1
appear = set([])
ls = []

while b not in appear:
    c = b
    appear.add(c)
    ls.append(c)
    b = c*a%m

if c == b:
    if x <= len(ls)-1:
        print(sum(ls[:x])%m)
    else:
        print(((x-(len(ls)-1))*c + sum(ls[:-1]))%m)

else:
    if x <= len(ls)-1:
        print(sum(ls[:x])%m)
    else:
        if c == 1:
            d = x%len(ls)
            print(sum(ls[:d])%m)
        else:
            d = x%(len(ls)-1)
            print()