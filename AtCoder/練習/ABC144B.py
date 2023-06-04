n = int(input())
ls = list(range(1,10))
x = []
for a in ls:
    for b in ls:
        x.append(a*b)
if n in x:
    print("Yes")
else:
    print("No")