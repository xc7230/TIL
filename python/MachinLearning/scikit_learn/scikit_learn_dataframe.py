import sklearn
from sklearn.datasets import load_iris

iris_data = load_iris()
print(type(iris_data))

# key
keys = iris_data.keys()
print('붓꽃 데이터 세트의 키들:', keys)

# key value
print('\n feature_names 의 type:', type(iris_data.feature_names))
print(' feature_names 의 shape:', len(iris_data.feature_names))
print(iris_data.feature_names)

print('\n target 의 type:', type(iris_data.target_names))
print(' target_names 의 shape:', len(iris_data.target_names))
print(iris_data.target_names)

print('\n data 의 type:', type(iris_data.data))
print(' data 의 shape:', iris_data.data.shape)
print(iris_data['data'])

print('\n target 의 type:', type(iris_data.target))
print(' target 의 shape:', iris_data.target.shape)
print(iris_data.target)