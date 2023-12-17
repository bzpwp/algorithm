n = int(input())

x = 1
while x**x <=n:
    if x **x ==n:
        print(x)
        exit()
    else:
        x += 1
print(-1)