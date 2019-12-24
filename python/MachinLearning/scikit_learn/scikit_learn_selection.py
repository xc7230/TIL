import sklearn
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# iris = load_iris()
# dt_clf = DecisionTreeClassifier()
# train_data = iris.data
# train_label = iris.target
# dt_clf.fit(train_data, train_label)

# #학습 데이터 세트로 예측 수행
# pred = dt_clf.predict(train_data)
# print('예측 정확도:', accuracy_score(train_label, pred)) 

# 모델 나누기
dt_clf = DecisionTreeClassifier()
iris_data = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.3, random_state=121)

# 예측 정확도
dt_clf.fit(X_train, y_train)
pred = dt_clf.predict(X_test)
print('예측 정확도: {0: 4f}'.format(accuracy_score(y_test, pred)))