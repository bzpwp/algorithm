n = int(input())
s = input()
import copy

x = s[0]
for i in range(1,len(s)):
    y = s[i]
    if y == x:
        print("No")
        exit()
    else:
        x = copy.copy(y)

print("Yes")