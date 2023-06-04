n  =int(input())
s = list(input())

from collections import Counter

c = Counter(s)
# print(c)
if c["T"] == 0:
    print("A")
elif c["A"] == 0:
    print("T")
elif c["T"] > c["A"]:
    print("T")
elif c["T"] < c["A"]:
    print("A")
else:
    x = n//2
    a = 0
    b = 0
    for i in range(n):
        if s[i] == "T":
            a += 1
            if a == x:
                print("T")
                exit()
        else:
            b += 1
            if b == x:
                print("A")
                exit()