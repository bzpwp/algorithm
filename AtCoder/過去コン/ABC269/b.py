a=10
b =1
c=10
d=1
for i in range(10):
    s = input()
    for j in range(10):
        if s[j]=="#":
            a = min(a,i+1)
            c = min(c,j+1)
            b = max(b,i+1)
            d = max(d,j+1)

print(a,b)
print(c,d)