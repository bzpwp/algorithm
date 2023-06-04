s = input()
A = 0
x = 0
ls = set(["A","C","G","T"])
for i in range(len(s)):
    if s[i] in ls:
        x += 1
    else:
        A = max(A,x)
        x = 0
print(A)