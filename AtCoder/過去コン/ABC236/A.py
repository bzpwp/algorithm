s = input()
a,b = map(int,input().split())
x = s[a-1]
y = s[b-1]
s = list(s)
s[a-1] = y
s[b-1] = x
print("".join(s))