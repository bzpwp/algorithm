a,b = map(int, input().split())

x = str(a)
y = str(b)
z = max(len(x),len(y))-min(len(x),len(y))
j = ""
for i in range(z):
    j += str(0)
if len(x)>len(y):
    y = j + y
else:
    x = j + x
ls = []
for i in range(len(x)):
    ls.append(int(x[i])+int(y[i]))
if max(ls) >= 10:
    print("Hard")
else:
    print("Easy")