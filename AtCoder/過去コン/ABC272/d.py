n,m = map(int, input().split())
ls = [[-1]*n for i in range(n)]
ls[0][0]=0

def try_square_root_naive(n):
    m = int(n**.5)
    return m if abs(m*m - n) < 1e-6 else None
import math
ls = []
for i in range(math.floor(math.sqrt(m))):
    if try_square_root_naive(m-i**2)!=None:
        ls.append([i,round(math.sqrt(m-i**2))])

if len(ls)==0:
    for i in ls:
        print(*i)
    else:
        