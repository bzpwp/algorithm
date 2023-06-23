""""""
#https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4972778#1
""""""

def list2d(a, b, c): return [[c] * b for i in range(a)]
EPS = 10**-10

def gauss_jordan(A, b):
    """ ガウス・ジョルダン法(連立方程式の解) """

    N = len(A)
    B = list2d(N, N+1, 0)
    for i in range(N):
        for j in range(N):
            B[i][j] = A[i][j]
    for i in range(N):
        B[i][N] = b[i]
    
    for i in range(N):
        pivot = i
        for j in range(i, N):
            if abs(B[j][i]) > abs(B[pivot][i]):
                pivot = j
        B[i], B[pivot] = B[pivot], B[i]

        if abs(B[i][i]) < EPS:
            return []

        for j in range(i+1, N+1):
            B[i][j] /= B[i][i]
        for j in range(N):
            if i != j:
                for k in range(i+1, N+1):
                    B[j][k] -= B[j][i] * B[i][k]
    
    res = [0] * N
    for i in range(N):
        res[i] = B[i][N]
    return res

print(gauss_jordan([[22,3],[3,4]], [2,3]))

# 22x + 3y = 2, 3x + 4y = 3