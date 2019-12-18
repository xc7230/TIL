import numpy as np #numpy import
array1 = np.array([1,2,3]) # 1차원 array에 3개 만든다.
print('array1 type:' , type(array1))
print('array1 array 형태:', array1.shape)
array2 = np.array([[1,2,3],
                 [2,3,4]])
print('array2 type:' , type(array2))
print('array2 array 형태:', array2.shape)

array3 = np.array([[1,2,3]])
print('array3 type:' , type(array3))
print('array3 array 형태:', array3.shape)

array4 = np.array([[[1,2,3]]])
print('array4 type:' , type(array4))
print('array4 array 형태:', array4.shape)