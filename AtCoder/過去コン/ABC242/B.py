s = input()
x = []
for c in s:
    x.append(c)
x.sort()
y = ""
for a in x:
    y+=a
print(y)