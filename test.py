import math
import numpy as np

def get_unique_rows(X):
    X_unique = [list(row) for row in set(tuple(row) for row in X)]
    return X_unique

X = np.random.randint(4, 6, size=(10,3))
print(X)

get_unique_rows(X)