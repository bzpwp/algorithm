s = input()
a = 0
for i in range(8):
    a +=  int(s[2*i+1])

if a == 0:
    print("Yes")
else:
    print("No")
