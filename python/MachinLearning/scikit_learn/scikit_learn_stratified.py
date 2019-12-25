import pandas as pd
import numpy as np
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['label'] = iris.target
# print(iris_df['label'].value_counts())

# # 데이터 분포 확인
# kfold = KFold(n_splits = 3)
# n_iter = 0
# for train_index, test_index in kfold.split(iris_df):
#     n_iter += 1
#     label_train = iris_df['label'].iloc[train_index]
#     label_test = iris_df['label'].iloc[test_index]
#     print('## 교차검증:{0}'.format(n_iter))
#     print('학습 레이블 데이터 분포:\n', label_train.value_counts())
#     print('검증 레이블 데이터 분포:\n', label_test.value_counts(), iris_df['label'].value_counts())

# # StratifiedKFold 레이블 생성
# skf = StratifiedKFold(n_splits=3)
# n_iter=0

# for train_index, test_index in skf.split(iris_df, iris_df['label']):
#     n_iter += 1
#     label_train = iris_df['label'].iloc[train_index]
#     label_test = iris_df['label'].iloc[test_index]
#     print('## 교차검증: {0}'.format(n_iter))
#     print('학습 레이블 데이터 분포:\n', label_train.value_counts())
#     print('검증 레이블 데이터 분포:\n', label_test.value_counts())


dt_clf = DecisionTreeClassifier(random_state=156)
features = iris.data
label = iris.target
skfold = StratifiedKFold(n_splits=3)
n_iter=0
cv_accuracy=[]

# StratifiedKFold의 split() 호출시 반드시 레이블 데이터 세트도 추가 입력 필요
for train_index, test_index in skfold.split(features, label):
    #split()으로 반환된 인덱스를 이용해 학습용, 검증용 테스트 데이터 추출
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    # 학습 및 예측
    dt_clf.fit(X_train, y_train)
    pred = dt_clf.predict(X_test)

    # 반복 시마다 정확도 측정
    n_iter += 1
    accuracy = np.round(accuracy_score(y_test, pred), 4)
    train_size = X_train.shape[0]
    test_size = X_test.shape[0]
    print('\n#{0} 교차검증 정확도 :{1}, 학습 데이터 크기: {2}, 검증 데이터 크기: {3}'.format(n_iter, accuracy, train_size, test_size))
    print('#{0} 검증 세트 인덱스:{1}'.format(n_iter, test_index))
    cv_accuracy.append(accuracy)

# 교차 검증별 정확도 및 평균 정확도 계산
print('\n## 교차 검증별 정확도:', np.round(cv_accuracy, 4))
print('## 평균 검증 정확도:', np.mean(cv_accuracy))
