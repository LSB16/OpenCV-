import numpy as np

array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]]).astype(np.uint8)

array2 = np.array([0.123,0.456,0.789,1.111]).astype(np.float64)
#print(array1)
#print(array2)
print(list(zip(array1,array2)))

for (a1,a2,a3,a4),b1 in list(zip(array1, array2)):
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(b1)