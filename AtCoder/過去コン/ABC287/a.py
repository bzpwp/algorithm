n = int(input())
a = 0
for i in range(n):
    s = input()
    if s[0]=="F":
        a += 1
if a > n//2:
    print("Yes")
else:
    print("No")