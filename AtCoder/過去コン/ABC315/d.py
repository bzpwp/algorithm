h,w = map(int,input().split())
grid = [list(input()) for _ in range(h)]

wls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from collections import defaultdict
dd = defaultdict(int)
for i in range(26):
    dd[wls[i]] = i+1

for i in range(h):
    for j in range(w):
        grid[i][j] = dd[grid[i][j]]

import numpy as np

grid = np.array(grid)
# print(grid)
def remove_identical_rows_columns(matrix):
    while True:
        # 各行で要素がすべて同じかつ長さが2以上かどうかをチェック
        rows_to_remove = []
        for i, row in enumerate(matrix):
            if len(row) >= 2 and np.all(row == row[0]):
                rows_to_remove.append(i)
        
        # 各列で要素がすべて同じかつ長さが2以上かどうかをチェック
        columns_to_remove = []
        for j in range(matrix.shape[1]):
            column = matrix[:, j]
            if len(column) >= 2 and np.all(column == column[0]):
                columns_to_remove.append(j)
        # 削除すべき行と列がなければ終了
        if not rows_to_remove and not columns_to_remove:
            break
        
        # 行と列を削除
        if rows_to_remove:
            matrix = np.delete(matrix, rows_to_remove, axis=0)
        if columns_to_remove:
            matrix = np.delete(matrix, columns_to_remove, axis=1)
    
    return matrix

        
        # matrix = remove_identical_rows_columns(matrix)
    
    return matrix

matrix = remove_identical_rows_columns(grid)

# print(matrix)
print(matrix.size)