import pandas as pd

# 파일 로딩
titanic_df =pd.read_csv('./data/train.csv')

# # sort_values()
# titanic_sorted = titanic_df.sort_values(by=['Name'])
# print(titanic_sorted.head(3))

# # 내림차순
# titanic_sorted = titanic_df.sort_values(by=['Pclass', 'Name'], ascending=False)
# print(titanic_sorted.head(3))

# # Aggregation 함수
# count()
# print(titanic_df.count())

# # mean()
# print(titanic_df[['Age', 'Fare']].mean())

# # groupby()
# titanic_groupby = titanic_df.groupby(by='Pclass')
# print(type(titanic_groupby))


# # 한개 칼럼
# titanic_groupby = titanic_df.groupby('Pclass').count()
# print(titanic_groupby)

# # 여러개 칼럼
# titanic_groupby = titanic_df.groupby('Pclass')[['PassengerId', 'Survived']].count()
# print(titanic_groupby)

# # aggregation 함수 적용
# print(titanic_df.groupby('Pclass')['Age'].agg([max, min]))

# # 딕셔너리 형식
# agg_format={'Age':'max', 'SibSp':'sum', 'Fare':'mean'}
# print(titanic_df.groupby('Pclass').agg(agg_format))

# # isna()
# print(titanic_df.isna().head(3))

# # 결손 데이터 갯수
# print(titanic_df.isna().sum())

# # fillna()
titanic_df['Cabin'] = titanic_df['Cabin'].fillna('C000')
# print(titanic_df.head(3))

titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
print(titanic_df.isna().sum())