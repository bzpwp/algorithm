n,m = map(int,input().split())
s = input()

need = 0
a = m
b = 0

for i in s:
    if i == "0":
        a = m
        b = need
    elif i == "1":
        if a >= 1:
            a -= 1
        else:
            if b >=1:
                b -= 1
            else:
                need += 1
    elif i == "2":
        if b >= 1:
            b -= 1
        else:
            need += 1
print(need)