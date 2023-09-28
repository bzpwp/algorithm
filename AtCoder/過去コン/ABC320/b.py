s = input()

# t = s[::-1]

A = 0
for i in range(len(s)):
    x = i+1
    for j in range(len(s)-x+1):
        t = s[j:j+x]
        if t == t[::-1]:
            A = x
print(A)