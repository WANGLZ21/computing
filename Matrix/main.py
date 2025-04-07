import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5]])
B = np.array([[5, 6], [7, 8], [4, 6], [5, 8]])

# 矩阵乘法
result = A@B  # 或使用 @ 运算符（Python 3.5+）
print(result)
# 输出:
# [[19 22]
#  [43 50]]