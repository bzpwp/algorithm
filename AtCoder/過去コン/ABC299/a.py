n = int(input())
s = input()

c = False

for i in range(n):
    if s[i] == "*" and c:
        print("in")
        exit()
    elif s[i] == "*" and not c:
        print("out")
        exit()
    elif s[i] == "|" and not c:
        c = True
    elif s[i] == "|" and c:
        c = False
