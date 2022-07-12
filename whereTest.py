import numpy as np

array1 = np.arange(5,15)
print(array1)       # [5 6 7 8 9 10 11 12 13 14]
array2 = np.where(array1 > 10)
print(array2)

array2Da = np.array([[15,8,12],[11,7,3]])
print(np.where(array2Da > 10, array2Da, 10))