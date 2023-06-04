a,b,k = map(int, input().split())
x = 0
for i in range(10**9):
    if a >= b:
        print(x)
        exit()
    a = a*k
    x += 1
    