import pandas as pd

# 파일 로딩
titanic_df =pd.read_csv('./data/train.csv')

# DataFrame의 []연산자
print('단일 칼럼 데이터 추출:\n', titanic_df['Pclass'].head(3))
print('\n여러 칼럼의 데이터 추출:\n', titanic_df[['Survived','Pclass']].head(3))
# print('[ ] 안에 숫자 index는 KeyError 오류 발생:\n',titanic_df[0])

print(titanic_df[0:2])

print(titanic_df[titanic_df['Pclass'] == 3].head(3))

# DataFrame ix[]
print('칼럼 위치 기반 인덱싱 데이터 추출:', titanic_df.ix[0, 2])
print('칼럼 명 기반 인덱싱 데이터 추출:', titanic_df.ix[0, 'Pclass'])

data = {'Name':['Chulmin', 'Eunkyung', 'Jinwoong', 'Soobeom'],
        'Year':[2011, 2016, 2015, 2015],
        'Gender':['Male', 'Female', 'Male', 'Male']
        }
data_df = pd.DataFrame(data, index=['one', 'two', 'three', 'four'])
print(data_df)

# iloc[]
print(data_df.iloc[0, 0])

# # 위치기반으로 안하면
# print(data_df.iloc[0, 'Name'])

# loc[]연산자
print(data_df.loc['one','Name'])