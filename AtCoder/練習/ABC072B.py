s = input()
a = ''
if len(s)%2 ==0:
    for i in range(len(s)//2):
        a += s[2*i]
else:
    for i in range(len(s)//2+1):
        a += s[2*i]
print(a)