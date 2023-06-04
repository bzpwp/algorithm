n = int(input())
s = input()
A = 0
for i in range(1000):
    x = "0"*(3-len(str(i))) + str(i)
    order = 0
    for j in s:
        if j == x[order]:
            order += 1
            if order == 3:
                A += 1
                break
print(A)