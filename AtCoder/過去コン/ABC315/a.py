s = input()

a = ""

for i in s:
    if i not in ["a","i","u","e","o"]:
        a += i
print(a)