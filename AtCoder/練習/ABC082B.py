s = input()
t = input()
sl = sorted(s)
tl = sorted(t)
tl.reverse()
if sl < tl:
    print("Yes")
else:
    print("No")