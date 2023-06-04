h,w = map(int, input().split())
ls = [input() for _ in range(h)]

x = 101
y = 101
for i in range(h):
    for j in range(w):
        if ls[i][j]=="o":
            if x==101:
                x = i
                y = j
            else:
                x = abs(x-i)
                y = abs(y-j)

print(x+y)q