s = input()
x = len(s)

ans = 0
y = 0
for i in range(x):
    if s[i]=="A" or s[i]=="C" or s[i]=="G" or s[i]=="T":
        ans += 1
    else:
        y = max(y,ans)
        ans = 0
print(y)