import sympy as sym
P = float(input())
x = sym.Symbol('x')

def func2(x):
    return x + P/2**(x/1.5)

import scipy.optimize
import math
from math import log, exp

if P < 1.5/log(2):
    print(func2(0))
    exit()

def func_f1(x):
    # return 1-(p*math.log(2))/1.5*(2**(x/1.5))
    return 1 - log(2) / 1.5 * P * exp(-log(2) / 1.5 * x)

result1 = scipy.optimize.bisect(func_f1, -1, P)

print(func2(result1))