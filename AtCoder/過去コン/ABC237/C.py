s = input()
tl = len(s)
l = tl//2
fa = 0
fb = 0
if tl == 1:
    print("Yes")
    exit()
elif tl == 2:
    if s[0]==s[1]:
        print("Yes")
        exit()
    print("No")
for a in range(l):
    if s[a] == "a":
        fa += 1
    else:
        break
for a in range(l):
    if s[tl-a-1] == "a":
        fb += 1
    else:
        break
if fa > fb:
    print("No")
else:
    ns = "a"*(fb - fa) + s
    tnl = len(ns)
    nl = tnl//2
    for a in range(nl):
        if ns[a]!=ns[tnl-a-1]:
            print("No")
            exit()
    print("Yes")