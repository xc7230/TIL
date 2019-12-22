import pandas as pd

# 파일 로딩
titanic_df = pd.read_csv('./data/train.csv')

# # boolean indexing
# titanic_boolean = titanic_df[titanic_df['Age']>60]
# print(type(titanic_boolean)

# []연산자
print(titanic_df[titanic_df['Age']>60][['Name', 'Age']].head(3))

# loc[] 연산자
print(titanic_df.loc[titanic_df['Age']>60, ['Name', 'Age']].head(3))

# 조건문
print(titanic_df[(titanic_df['Age']>60) & (titanic_df['Pclass']==1) & (titanic_df['Sex']=='female')])

# 개별 조건 결합
cond1 = titanic_df['Age'] > 60
cond2 = titanic_df['Pclass']==1
cond3 = titanic_df['Sex']=='female'
print(titanic_df[cond1 & cond2 & cond3])