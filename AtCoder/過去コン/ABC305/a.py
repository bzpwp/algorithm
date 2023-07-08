n = int(input())
x = n//5

a = n-x*5
b = (x+1)*5-n

if a < b:
    print(x*5)
else:
    print((x+1)*5)