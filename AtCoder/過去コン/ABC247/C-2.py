n = int(input())
x = "1"
for a in range(n-1):
    x = x + str(a+2) + x
print(' '.join(x))