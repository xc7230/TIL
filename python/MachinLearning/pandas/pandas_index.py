import pandas as pd

# 파일 로딩
titanic_df =pd.read_csv('./data/train.csv')

# Index 객체 추출
indexes = titanic_df.index
print(indexes)

# Index 객체를 실제 값 array로 변환
print('Index 객체 array값:\n', indexes.values)

# 단일 값 반환 및 슬라이싱
print(type(indexes.values))
print(indexes.values.shape)
print(indexes[:5].values)
print(indexes.values[:5])
print(indexes[6])

# Series 객체
series_fair = titanic_df['Fare']
print('Fare Series max 값:', series_fair.max())
print('Fare Series sum 값:', series_fair.sum())
print('sum() Fair Series:', sum(series_fair))
print('Fair Series + 3:\n', (series_fair + 3).head(3))

# reset_index()
titanic_reset_df = titanic_df.reset_index(inplace = False)
print(titanic_reset_df.head(3))

# index칼럼을 2개 만들면
print('### before reset_index ###')
value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
print('value_counts 객체 변수 타입:', type(value_counts))
new_value_counts = value_counts.reset_index(inplace = False)
print('### After reset_index ###')
print(new_value_counts)
print('new_value_counts 객체 변수 타입:', type(new_value_counts))