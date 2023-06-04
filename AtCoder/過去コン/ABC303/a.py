n = int(input())
s = input()
t = input()

x = 0
for i in range(n):
    if s[i] == t[i] or (s[i] == "1" and t[i] == "l") or (s[i] == "l" and t[i] == "1") or (s[i] == "0" and t[i] == "o") or (s[i] == "o" and t[i] == "0"):
        x += 1
    # print(i,x)

if x == n:
    print("Yes")
else:
    print("No")