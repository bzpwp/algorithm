a = int(input())
b = int(input())
c = int(input())
x = int(input())

total = 0
for i in range(min(a,x//500)+1):
    for j in range(min(b, (x-500*i)//100)+1):
        for k in range(c+1):
            if x-500*i-100*j==50*k:
                total += 1
print(total)
