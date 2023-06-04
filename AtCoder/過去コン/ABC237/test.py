s = input()
tl = len(s)
l = tl//2
fa = 0
fb = 0
for a in range(l):
    if s[a] == "a":
        fa += 1
    else:
        break
for a in range(l):
    print(tl-a)