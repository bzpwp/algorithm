n = int(input())
import math
x = math.floor(math.sqrt(n))
s = 0
while True:
    if n%x == 0:
        y = n//x
        break
    else:
        x -=1
while True:
    if y//10==0:
        s+=1
        break
    else:
        y = y//10
        s+=1
print(s)