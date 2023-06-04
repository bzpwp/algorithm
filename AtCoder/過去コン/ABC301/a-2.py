n  =int(input())
s = list(input())
print(s)

a = 0
b = 0
for i in s:
    if s == "T":
        a += 1
    else:
        b += 1
print(a,b)
if a > b:
    print("T")
else:
    print("A")