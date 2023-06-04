a,b  = map(int, input().split())

def func(y):
    return b*y + a/(y+1)**(1/2)

x = (a/(2*b))**(2/3)-1

if x <= 0:
    print(func(0))
    exit()

import math

n1 = math.floor(x)
n2 = math.ceil(x)



print(min(func(n1),func(n2)))