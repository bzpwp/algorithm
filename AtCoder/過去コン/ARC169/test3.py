n = int(input())
al = list(map(int,input().split()))
pl = list(map(int,input().split()))


fibonacci = [[0 for _ in range(n)] for __ in range(n)]
for i in range(n):
    fibonacci[i][i] = 1
# print(fibonacci)
for i in range(n-1):
    fibonacci[i+1][pl[i]-1] += 1

import numpy as np

fibonacci = np.array(fibonacci)
# print(fibonacci)
# fibonacci = np.linalg.matrix_power(fibonacci,2)
A_3 = np.linalg.matrix_power(fibonacci, 10**100)
# print(fibonacci)
print(A_3)
x = 0
for i in range(n):
    x += al[i]*A_3[i][0]
if x < 0:
    print("-")
elif x == 0:
    print(0)
elif x > 0:
    print("+")