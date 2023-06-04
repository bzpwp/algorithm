s = input()
l = len(s)
ab = 0
af = 0
for a in range(l):
    if s[a] == "a":
        af += 1
    else:
        break
for a in range(l):
    if s[l-a-1] == "a":
        ab += 1
    else:
        break
if af > ab:
    print("No")
else:
    ns = "a"*(ab - af) + s
    tnl = len(ns)
    nl = tnl//2
    for a in range(nl):
        if ns[a]!=ns[tnl-a-1]:
            print("No")
            exit()
    print("Yes")