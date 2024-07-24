import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a.shape)

b = [1, 4]

print(np.where(a[:, 0]==1)[0][0])
nearest_coords = np.array([a[np.where(a[:, 0]==idx)[0][0], 1:] for idx in b])
print(nearest_coords)