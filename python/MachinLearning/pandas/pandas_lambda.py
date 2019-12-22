import pandas as pd

# 파일 로딩
titanic_df = pd.read_csv('./data/train.csv')

def get_square(a):
    return a**2

print('3의 제곱은:', get_square(3))

# lambda식
lambda_square = lambda x:x**2
print('3의 제곱은:', lambda_square(3))

# map()
a = [1, 2, 3]
squares = map(lambda x: x**2, a)
print(list(squares))

# 데이터 가공
titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x : len(x))
print(titanic_df[['Name', 'Name_len']].head(3))

# 복잡한 데이터 가공
titanic_df['Child_Adult'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else 'Adult')
print(titanic_df[['Age', 'Child_Adult']].head(8))

titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x: 'Child' if x<=15 else ('Adult' if x <= 60 else 'Elderly'))
print(titanic_df['Age_cat'].value_counts())

# lambda에 함수 적용
# 나이에 따라 세분화된 분류를 수행하는 함수 생성
def get_category(age):
    cat=''
    if age <= 5 : cat = 'Baby'
    elif age <= 12 : cat = 'Child'
    elif age <= 18 : cat = 'Teenager'
    elif age <= 25 : cat = 'Student'
    elif age <= 35 : cat = 'Young Adult'
    elif age <= 60 : cat = 'Adult'
    else : cat = 'Elderly'

    return cat

# lambda 식에 위에서 생성한 get_category()함수를 반환값으로 지정.
# get_category(X)는 입력값으로 'Age' 칼럼 값을 받아서 해당하는 cat반환
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))
print(titanic_df[['Age', 'Age_cat']].head()) 