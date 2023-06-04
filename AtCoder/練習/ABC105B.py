n = int(input())
x = 0
for a in range(n//7+1):
    for b in range(n//4+1):
        if a*7+b*4==n:
            x += 1
if x ==0:
    print("No")
else:
    print("Yes")