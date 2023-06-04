s = input()
t = input()

x = len(t)

for i in range(len(s)-x+1):
    y = s[i:i+x]
    if y == t:
        print("Yes")
        exit()

print("No")