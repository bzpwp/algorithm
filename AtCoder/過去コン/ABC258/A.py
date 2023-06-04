k = int(input())
x = k//60
y = k%60
if y < 10:
    y = str(0)+str(y)
else:
    y = str(y)
print(str(21+x)+":"+y)