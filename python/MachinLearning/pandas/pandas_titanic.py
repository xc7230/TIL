import pandas as pd
import numpy as np

titanic_df = pd.read_csv(r'./data/train.csv')
# # print(titanic_df.head(3))
# print('titanic 변수 type:', type(titanic_df))
# # print(titanic_df)
# print('DataFrame 크기:', titanic_df.shape)

# # info()
# titanic_df.info()

# # describe()
# print(titanic_df.describe())

# # value_counts()
# value_counts = titanic_df['Pclass'].value_counts()
# print(value_counts)

# titanic_pclass = titanic_df['Pclass']
# print(type(titanic_pclass))
# print(titanic_pclass.head())

# value_counts = titanic_df['Pclass'].value_counts()
# print(type(value_counts))
# print(value_counts)

# col_name1 = ['col1']
# list1 = [1, 2, 3]
# array1 = np.array(list1)
# print('array1 shape:', array1.shape)
# # 리스트를 이용해 DataFrame 생성.
# df_list1 = pd.DataFrame(list1, columns=col_name1)
# print('1차원 리스트로 만든 DataFrame:\n', df_list1)
# # 넘파이 ndarray를 이용해 DataFrame 생성.
# df_array1 = pd.DataFrame(array1, columns=col_name1)
# print('1차원 ndarray로 만든 DataFrame:\n', df_array1)

# # 3개의 칼럼명이 필요함
# col_name2 = ['col1', 'col2', 'col3']

# # 2행x3열 형태의 리스트와 ndarray 생성한 뒤 이를 DataFrame으로 변환
# list2 = [[1, 2, 3],
#         [11, 12, 13]]
# array2 = np.array(list2)
# print('array2 shape:', array2.shape)
# df_list2 = pd.DataFrame(list2, columns=col_name2)
# print('2차원 리스트로 만든 DataFrame:\n', df_list2)
# df_array2 = pd.DataFrame(array2, columns=col_name2)
# print('2차원 ndarray로 만든 DataFrame:\n', df_array2)

# # Key는 문자열 칼럼명으로 매핑, Value는 리스트 형(또는 ndarray) 칼럼 데이터로 매핑
# dict = {'col1':[1, 11], 'col2':[2, 22], 'col3':[3, 33]}
# df_dict = pd.DataFrame(dict)
# print('딕셔너리로 만든 DataFrame:\n', df_dict)

# # DataFrame을 ndarray로 변환
# array3 = df_dict.values
# print('df_dict.values 타입:', type(array3), 'df_dict.values shape:', array3.shape)
# print(array3)

# # DataFrame을 리스트로 변환
# list3 = df_dict.values.tolist()
# print('df_dict.values.tolist() 타입:', type(list3))
# print(list3)

# # DataFrame을 딕셔너리로 변환
# dict3 = df_dict.to_dict('list')
# print('\n df_dict.to_dict() 타입:', type(dict3))
# print(dict3)

titanic_df['Age_0'] = 0
print('칼럼 데이터 생성:\n', titanic_df.head(3))
titanic_df['Age_by_10'] = titanic_df['Age']*10
titanic_df['Family_No'] = titanic_df['SibSp'] + titanic_df['Parch']+1
print('새로운 칼럼생성:\n', titanic_df.head(3))
titanic_df['Age_by_10'] = titanic_df['Age_by_10']+100
print('기존 칼럼 값 일괄적으로 계산:\n', titanic_df.head(3))
