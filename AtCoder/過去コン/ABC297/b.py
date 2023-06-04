s = input()

x = 0
for i in range(8):
    if s[i] == "B":
        x += i
if x%2 == 0:
    print("No")
    exit()

c = False

for i in range(8):
    if s[i] == "R" and not c:
        c = True
    elif s[i] == "R" and c:
        c = False
    elif s[i] == "K":
        if c:
            print("Yes")
        else:
            print("No")