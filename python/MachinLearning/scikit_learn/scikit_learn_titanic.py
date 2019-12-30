import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV

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
# sns.barplot(x='Pclass', y='Survived', hue='Sex', data=titanic_df)
# plt.show()

# 입력 age에 따라 구분 값을 반환하는 함수 설정, DataFrame의 apply lambda 식에 사용.
# def get_category(age):
#     cat = ''
#     if age <= -1: cat = 'Unknown'
#     elif age <= 5: cat = 'Baby'
#     elif age <= 12: cat = 'Child'
#     elif age <= 18: cat = 'Teenager'
#     elif age <= 25: cat = 'Student'
#     elif age <= 35: cat = 'Young Adult'
#     elif age <= 60: cat = 'Adult'
#     else : cat = 'Elderly'

#     return cat

# # 막대그래프의 크기 figure를 더 크게 설정
# plt.figure(figsize=(10, 6))

# # X축의 값을 순차적으로 표시하기 위한 설정
# group_names = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Elderly']

# # lambda 식에 위에서 생성한 get_category() 함수를 반환값으로 지정.
# # get_category(X)는 입력값으로 'Age' 칼럼 값을 받아서 해당하는 cat 반환
# titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))
# sns.barplot(x='Age_cat', y='Survived', hue='Sex', data=titanic_df, order=group_names)
# titanic_df.drop('Age_cat', axis=1, inplace=True)
# plt.show()

# 문자열 카테고리를 숫자형으로 변환
# def encode_features(dataDF):
#     features = ['Cabin', 'Sex', 'Embarked']
#     for feature in features:
#         le = preprocessing.LabelEncoder()
#         le = le.fit(dataDF[feature])
#         dataDF[feature] = le.transform(dataDF[feature])

#     return dataDF

# titanic_df = encode_features(titanic_df)
# print(titanic_df.head())

# Null 처리 함수
def fillna(df):
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Cabin'].fillna('N', inplace=True)
    df['Embarked'].fillna('N', inplace=True)
    df['Fare'].fillna(0, inplace=True)
    return df

# 머신러닝 알고리즘에 불필요한 속성 제거
def drop_features(df):
    df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
    return df

# 레이블 인코딩 수행.
def format_features(df):
    df['Cabin'] = df['Cabin'].str[:1]
    features = ['Cabin', 'Sex', 'Embarked']
    for feature in features:
        le = LabelEncoder()
        le = le.fit(df[feature])
        df[feature] = le.transform(df[feature])
    return df

# 앞에서 설정한 데이터 전처리 함수 호출
def transform_features(df):
    df = fillna(df)
    df = drop_features(df)
    df = format_features(df)
    return df

# 원본 데이터를 재로딩하고, 피처 데이터 세트와 레이블 데이터 세트 추출.
titanic_df = pd.read_csv('./data/train.csv')
y_titanic_df = titanic_df['Survived']
X_titanic_df = titanic_df.drop('Survived', axis=1)

X_titanic_df = transform_features(X_titanic_df)

# 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X_titanic_df, y_titanic_df,
                                                    test_size=0.2, random_state=11)

# 예측
# 결정트리, Random Forest, 로지스틱 회귀를 위한 사이킷런 Classifier 클래스 생성
dt_clf = DecisionTreeClassifier(random_state=11)
rf_clf = RandomForestClassifier(random_state=11)
lr_clf = LogisticRegression()

# DecisionTreeClassifier 학습/예측/평가
dt_clf.fit(X_train, y_train)
dt_pred = dt_clf.predict(X_test)
# print('DecisionTreeClassifier 정확도: {0:.4f}'.format(accuracy_score(y_test, dt_pred)))

# RandomForestClassifier 학습/예측/평가
rf_clf.fit(X_train, y_train)
rf_pred = rf_clf.predict(X_test)
# print('RandomForestClassifier 정확도: {0:.4f}'.format(accuracy_score(y_test, rf_pred)))

# LogisticRegression 학습/예측/평가
lr_clf.fit(X_train, y_train)
lr_pred = lr_clf.predict(X_test)
# print('LogisticRegression 정확도: {0:.4f}'.format(accuracy_score(y_test, lr_pred)))

# 모델 평가
def exec_kfold(clf, folds=5):
    # 폴드 세트를 5개인 KFold객체를 생성, 폴드 수만큼 예측결과 저장을 위한 리스트 객체 생성.
    kfold = KFold(n_splits=folds)
    scores = []

    # KFold 교차 검증 수행.
    for iter_count, (train_index, test_index) in enumerate(kfold.split(X_titanic_df)):
        # X_titanic_df 데이터에서 교차 검증별로 학습과 데이터를 가리키는 index생성
        X_train, X_test = X_titanic_df.values[train_index], X_titanic_df.values[test_index]
        y_train, y_test = y_titanic_df.values[train_index], y_titanic_df.values[test_index]
        # Classifier 학습, 예측, 정확도 계산
        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        scores.append(accuracy)
        # print('교차 검증 {0} 정확도: {1:.4f}'.format(iter_count, accuracy))
    # 5개 fold에서의 평균 정확도 계산.
    mean_score = np.mean(scores)
    # print('평균 정확도: {0:.4f}'.format(mean_score))

# exec_kfold 호출
exec_kfold(dt_clf, folds=5)

# 교차 검증
scores = cross_val_score(dt_clf, X_titanic_df, y_titanic_df, cv=5)
for iter_count, accuracy in enumerate(scores):
    print('교차 검증 {0} 정확도: {1:.4f}'.format(iter_count, accuracy))

print('평균 정확도: {0:.4f}'.format(np.mean(scores)))


# GridSearchCV
parameters = {'max_depth':[2, 3, 5, 10],'min_samples_split':[2, 3, 5],'min_samples_leaf':[1, 5, 8]}

grid_dclf = GridSearchCV(dt_clf, param_grid=parameters, scoring='accuracy', cv=5)
grid_dclf.fit(X_train, y_train)

print('GridSearchCV 최적 하이퍼 파라미터:', grid_dclf.best_params_)
print('GridSearchCV 최고 정확도: {0:.4f}'.format(grid_dclf.best_score_))
best_dclf = grid_dclf.best_estimator_

# GridSearchCV의 최적 하이퍼 파라미터로 학습된 Estimator로 예측 및 평가 수행.
dpredictions = best_dclf.predict(X_test)
accuracy = accuracy_score(y_test, dpredictions)
print('테스트 세트에서의 DecisionTreeClassifier 정확도 : {0:.4f}'.format(accuracy))