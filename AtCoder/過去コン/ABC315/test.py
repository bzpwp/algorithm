import numpy as np

def extract_unique_subarrays(matrix):
    unique_rows = np.unique(matrix, axis=0)
    unique_columns = np.unique(matrix, axis=1)

    unique_rows_indices = np.where(np.isin(matrix, unique_rows))
    unique_columns_indices = np.where(np.isin(matrix, unique_columns))

    unique_indices = np.intersect1d(unique_rows_indices[0], unique_columns_indices[0])
    
    result = matrix[unique_indices]

    return result

# 例として二次元配列を作成
matrix = np.array([
    [1, 2, 2],
    [4, 4, 4],
    [1, 8, 9]
])

print("Original matrix:")
print(matrix)

# 同じ要素を持つ行と列を削除
result = extract_unique_subarrays(matrix)

print("\nMatrix after extracting rows and columns with unique elements:")
print(result)
