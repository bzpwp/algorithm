s = input()
l = len(s)
x = 0
for i in range(2**(l-1)):
    ls = []
    w = ""
    for j in range(l-1):
        if (i>>j)&1:
            ls.append("")
        else:
            ls.append("+")
    for k in range(l-1):
        w += s[k]
        w += ls[k]
    w += s[-1]
    x += eval(w)
print(x)