import numpy as np

np.random.seed(0)

A = np.random.randint(0,10,(3,3))
print("行列A：\n{}\n".format(A))

A_3 = np.linalg.matrix_power(A,3)

print("行列Aの3乗：\n{}".format(A_3))