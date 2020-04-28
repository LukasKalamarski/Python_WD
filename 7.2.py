import numpy as np
a = np.array( [[2,3,4, 6], [3, 6, 9, 7], [2,5,6,1], [1, 1, 2, 9]] )
b = np.array( [[2,3, 6], [ 6, 9, 7], [2,5,1], [ 1, 2, 9]] )
print(a.min(axis=1))
print(a.min(axis=0))
print(b.min(axis=1))
print(b.min(axis=0))