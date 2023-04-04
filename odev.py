


import numpy as np


A = np.array(input().split(), dtype=int)
B = np.array(input().split(), dtype=int)


dot_product = np.dot(A, B)
print(dot_product)


outer_product = np.outer(A, B)
print(outer_product)