# Numpy

머신러닝의 주요 알고리즘은 선형대수와 통계이다. 선형대수는 수학뿐만 아니라 여러곳의 기본적으로 쓰이기떄문에 어려워도 배워보자. Numerical Python을 의미한다.



## 1차원 array

```python
import numpy as np #numpy import
array1 = np.array([1,2,3]) # 1차원 array에 3개 만든다.
print('array1 type:' , type(array1))
print('array1 array 형태:', array1.shape)
```

결과

```python
array1 type: <class 'numpy.ndarray'>
array1 array 형태: (3,)
```

array1은 [데이터]가 한개인 1차원 array이고 (3,)로 1차원 array임을 표현



##  2차원 array

```python
array2 = np.array([[1,2,3],
                 [2,3,4]])
print('array2 type:' , type(array2))
print('array2 array 형태:', array2.shape)
```

결과

```python
array2 type: <class 'numpy.ndarray'>
array2 array 형태: (2, 3)
```

array2는 [[데이터],[데이터]]로 이루어진 2차원 데이터로 2개의 로우와 3개의 칼럼으로 이루어져 있다.





```python
array3 = np.array([[1,2,3]])
print('array3 type:' , type(array3))
print('array3 array 형태:', array3.shape)
```



 결과

```python
array3 type: <class 'numpy.ndarray'>
array3 array 형태: (1, 3)
```

array3는 array1과 다를게 없다. 하지만 [[데이터]]로 2차원 배열로 생성했기때문에 (1,3)으로 표시된다.



## 3차원 array

```python
array4 = np.array([[[1,2,3]]])
print('array4 type:' , type(array4))
print('array4 array 형태:', array4.shape)
```

결과

```python
array4 type: <class 'numpy.ndarray'>
array4 array 형태: (1, 1, 3)
```

array4도 역시 array1과 다를것 없는 데이터지만 3차원으로 ([[[데이터]]]) 만들었기 때문에 (1,1,3)이라는 결과가 나온다.



이렇게 같은 데이터라도 차원이 다르면 오류가 발생할 수 있다. 이 경우 차원을 다루는법을 익혀 오류를 막을 수 있다.