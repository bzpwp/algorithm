n,k = map(int,input().split())
s = input()

t = ""
count = 0
for i in s:
    if i == "o" and k > 0:
        t += "o"
        k -= 1
    else:
        t += "x"
print(t)