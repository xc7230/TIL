import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns


# 데이터 불러오기
titanic_df = pd.read_csv('./data/train.csv')
# print(titanic_df.head(3))
# print('\n ### 학습 데이터 정보 ### \n')
# print(titanic_df.info())

# Null값 처리
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)
titanic_df['Cabin'].fillna('N', inplace=True)
titanic_df['Embarked'].fillna('N', inplace=True)
# print('데이터 세트 Null 값 개수 ', titanic_df.isnull().sum().sum())

# 문자열 피처 분포
# print('Sex 값 분포 :\n', titanic_df['Sex'].value_counts())
# print('\n Cabin 값 분포 :\n', titanic_df['Cabin'].value_counts())
# print('\n Embarked 값 분포 :\n', titanic_df['Embarked'].value_counts())

# Cabin문자 추출
titanic_df['Cabin'] = titanic_df['Cabin'].str[:1]
# print(titanic_df['Cabin'].head(3))

# 성별 생존 확률
# print(titanic_df.groupby(['Sex', 'Survived'])['Survived'].count())

# 그래프 확인
# sns.barplot(x='Sex', y='Survived', data=titanic_df)
# plt.show()

# 객실 등급
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=titanic_df)
plt.show()