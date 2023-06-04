v,a,b,c = map(int, input().split())

d = v//(a+b+c)
e = v%(a+b+c)
if e == 0:
    print("F")
elif e < a:
    print("F")
elif e-a < b:
    print("M")
else:
    print("T")