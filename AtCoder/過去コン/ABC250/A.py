h, w = map(int, input().split())
r, c = map(int, input().split())
if h == 1 and w == 1:
    print(0)
elif h == 1:
    if c == 1 or c == w:
        print(1)
    else:
        print(2)
elif w == 1:
    if r == 1 or r == h:
        print(1)
    else:
        print(2)
else:
    if (r == 1 and c == 1) or (r == h and c == w) or (r == h and c == 1) or (r == 1 and c == w):
        print(2)
    elif r == 1 or r == h or c == 1 or c == w:
        print(3)
    else:
        print(4)