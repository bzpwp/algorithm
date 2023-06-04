n = int(input())
s = input()
A = [0]
x = 0
y = 1
for c in s:
    if c == "L":
        A.insert(x,y)
        y += 1
    else:
        x += 1
        A.insert(x,y)
        y += 1
print(*A)