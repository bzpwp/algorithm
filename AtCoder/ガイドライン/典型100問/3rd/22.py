n = float(input())

import math
x = (1.5*math.log(n*(math.log(2))/1.5))/math.log(2)

def func(x):
    return x + n/(2**(x/1.5))

if x < 0:
    print(func(0))
else:
    print(func(x))