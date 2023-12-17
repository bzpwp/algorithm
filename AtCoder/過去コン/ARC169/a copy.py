


import sys

def prob_d():
  def v_mul_mat(vec, mat):
    l = len(vec)
    ret = [0] * l
    for i in range(l):
      s = 0
      for j in range(l):
        s ^= vec[j] & mat[j][i]
      ret[i] = s
    return ret

  def mat_mulv(mat, vec):
    l = len(mat)
    ret = [0] * l
    for i in range(l):
      v = mat[i]
      s = 0
      for j in range(l):
        s ^= v[j] & vec[j]
      ret[i] = s
    return ret

  def mat_mulv_sparse(vec, mat):
    ret = [mat[-1][i] & vec[-1] for i in range(len(vec))]
    for i in range(1, len(vec)):
      ret[i] ^= (mat[i-1][i] & vec[i-1])
    return ret

  def mat_exp(mat, ex):
    l = len(mat)
    ret = [0] * l
    ret[0] = 0xFFFFFFFF

    A = [v[:] for v in mat]
    while ex:
      if ex & 1:
        ret = v_mul_mat(ret, A)
      next_A = [None] * l
      next_A[0] = v_mul_mat(A[0], A)
      for i in range(1, l):
        next_A[i] = mat_mulv_sparse(next_A[i-1], mat)
      A = next_A
      ex >>= 1
    ret2 = [None] * l
    ret2[0] = ret
    for i in range(1, l):
      ret2[i] = mat_mulv_sparse(ret2[i-1], mat)
    return ret2

  stdin = sys.stdin
  n = int(input())
  al = list(map(int,input().split()))
  pl = list(map(int,input().split()))


  mat = [[0] * n for _ in range(n)]
  for i in range(n):
    mat[i][i] = 1
  for i in range(n-1):
    mat[i+1][pl[i]-1] += 1
  print(mat)
  mat = mat_exp(mat, 1)
  print(mat)
    # vec = mat_mulv(mat, As)
    # print(vec[0])

prob_d()


# # print(fibonacci)
# fibonacci = matrix_pow(fibonacci, 10**100)
# x = 0
# for i in range(n):
#     x += al[i]*fibonacci[i][0]
# if x < 0:
#     print("-")
# elif x == 0:
#     print(0)
# elif x > 0:
#     print("+")