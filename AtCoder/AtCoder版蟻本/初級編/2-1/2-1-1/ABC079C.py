abcd = input()
a = abcd[0]
b = abcd[1]
c = abcd[2]
d = abcd[3]

ls = []
for e in range(2**3):
    l = []
    for f in range(3):
        if (e>>f)&1:
            l.append("+")
        else:
            l.append("-")
    ls.append(l)

for i in ls:
    w = a + i[0] + b + i[1] + c + i[2] + d
    if eval(w) == 7:
        print("".join([w,"=7"]))
        exit()