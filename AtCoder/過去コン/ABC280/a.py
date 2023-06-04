h,w = map(int,input().split())
a = 0
for i in range(h):
    s = input()
    for j in range(w):
        if s[j]=="#":
            a += 1
print(a)