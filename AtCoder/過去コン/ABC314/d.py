n = int(input())
s = list(input())
q = int(input())

ul = None

from collections import defaultdict

dd = defaultdict(int)
for i in range(q):
    t,x,c = input().split()
    if t == "2":
        ul = "lower"
        dd = defaultdict(int)
    elif t == "3":
        ul = "upper"
        dd = defaultdict(int)
    elif t == "1":
        s[int(x)-1]  = c
        dd[int(x)-1] = c

if ul == None:
    print("".join(s))
elif ul == "upper":
    s = [item.upper() for item in s]
    for i in dd:
        s[i] = dd[i]
    print("".join(s))
elif ul == "lower":
    s = [item.lower() for item in s]
    for i in dd:
        s[i] = dd[i]
    print("".join(s))