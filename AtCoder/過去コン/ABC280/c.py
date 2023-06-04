s = input()
t = input()

x = len(s)
for i in range(x):
    if s[i]!=t[i]:
        print(i+1)
        exit()
print(x+1)