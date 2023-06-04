n,x = map(int, input().split())
s = input()
x = format(x, 'b')
for i in range(n):
    if s[i]=="U":
        x = x[:-1]
    elif s[i]=="L":
        x += "0"
    else:
        x += "1"
print(int(x,2))