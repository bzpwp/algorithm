s = list(input())

a = ""
for i in s:
    if i == "0":
        a += "1"
    else:
        a += "0"
print(a)