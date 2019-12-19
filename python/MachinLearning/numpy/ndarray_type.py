import numpy as np

#integer
list1 = [1, 2, 3]
print(type(list1))
array1 = np.array(list1)
print(type(array1))
print(array1, array1.dtype)

#string
list2 = [1, 2, 'test']
array2 = np.array(list2)
print(array2, array2.dtype)

