'''
1次元
'''
# coding: utf-8

# 座標圧縮したい数列
A = [8, 100, 33, 33, 33, 12, 6, 1211]

# 集合型にすることで重複を除去し、
# 小さい順にソートする
B = sorted(set(A))

# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v: i for i, v in enumerate(B) }

# 答え
print(list(map(lambda v: D[v], A)))

'''
2次元
'''
def compress(C1, C2):
    vals = []
    N = len(C1)
    
    for i in range(N):
        for d in range(2):  # その位置と、一つ隣を確保(隣を確保しないと空白が埋まってしまうことがある)
            tc1 = C1[i] + d
            tc2 = C2[i] + d
            vals.append(tc1)
            vals.append(tc2)
    
    # ソート
    vals.sort()
    
    # 隣り合う重複を削除
    vals = list(set(vals))
    vals.sort()
    
    for i in range(N):
        C1[i] = vals.index(C1[i])
        C2[i] = vals.index(C2[i])
    
    return vals

