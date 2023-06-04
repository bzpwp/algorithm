n = int(input())
ls = ["1"]
for a in range(17):
    ls.append(str(ls[a])+str(a+2)+str(ls[a]))
x = []
for c in ls[n-1]:
    x.append(int(c))
print(*x)