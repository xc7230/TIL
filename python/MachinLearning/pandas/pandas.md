# Pandas

## Dataframe

### read_csv()

칼럼을 콤마(',')로 구분한 파일 포맷

```python
read_csv('파일명', sep='\t') #sep은 구분 문자 탭으로 구분해서 나눈다. 없으면 자동으로 ','로 설정
```



### data불러오기

```python
import pandas as pd

titanic_df = pd.read_csv(r'./data/train.csv')
print(titanic_df.head(3))
print('titanic 변수 type:', type(titanic_df))
print(titanic_df)
```

```bash
titanic 변수 type: <class 'pandas.core.frame.DataFrame'>
```



### data 크기

```python
print('DataFrame 크기:', titanic_df.shape)
```

```bash
DataFrame 크기: (891, 12)
```



### info()

```python
titanic_df.info()
```

```bash
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Name           891 non-null object
Sex            891 non-null object
Age            714 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Cabin          204 non-null object
Embarked       889 non-null object
dtypes: float64(2), int64(5), object(5)
memory usage: 66.2+ KB
```

info() 메서드를 통해서 총 데이터 건수와 데이터 타입, Null 건수를 알 수 있다.



### describe()

```python
print(titanic_df.describe())
```

```bash
       PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200
```

개략적인 데이터 분포도를 확인할 수 있다.



### value_counts()

```python
value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
```

```bash
3    491
1    216
2    184
Name: Pclass, dtype: int64
```

min이 1, 25 ~ 75%가 2, max가 3으로 이루어져 있다. 많은 건수 순서로 정렬되어 값을 반환한다.



```python
titanic_pclass = titanic_df['Pclass']
print(type(titanic_pclass))
print(titanic_pclass.head())
```

```bash
<class 'pandas.core.series.Series'>
0    3
1    1
2    3
3    1
4    3
Name: Pclass, dtype: int64
```

Dataframed의 []연산자 내부에 칼럼명을 입력하면 해당 칼럼에 해당하는 Series 객체를 반환한다.



![image-20191220133457406](pandas.assets/image-20191220133457406.png)



```python
value_counts = titanic_df['Pclass'].value_counts()
print(type(value_counts))
print(value_counts)
```

```bash
<class 'pandas.core.series.Series'>
3    491
1    216
2    184
Name: Pclass, dtype: int64
```



### ndarray를 DataFrame으로 바꾸기

```python
col_name1 = ['col1']
list1 = [1, 2, 3]
array1 = np.array(list1)
print('array1 shape:', array1.shape)
# 리스트를 이용해 DataFrame 생성.
df_list1 = pd.DataFrame(list1, columns=col_name1)
print('1차원 리스트로 만든 DataFrame:\n', df_list1)
# 넘파이 ndarray를 이용해 DataFrame 생성.
df_array1 = pd.DataFrame(array1, columns=col_name1)
print('1차원 ndarray로 만든 DataFrame:\n', df_array1)
```

```bash
array1 shape: (3,)
1차원 리스트로 만든 DataFrame:
    col1
0     1
1     2
2     3
1차원 ndarray로 만든 DataFrame:
    col1
0     1
1     2
2     3
```



### 2차원 리스트를 DataFrame으로 바꾸기

```python
# 3개의 칼럼명이 필요함
col_name2 = ['col1', 'col2', 'col3']

# 2행x3열 형태의 리스트와 ndarray 생성한 뒤 이를 DataFrame으로 변환
list2 = [[1, 2, 3],
        [11, 12, 13]]
array2 = np.array(list2)
print('array2 shape:', array2.shape)
df_list2 = pd.DataFrame(list2, columns=col_name2)
print('2차원 리스트로 만든 DataFrame:\n', df_list2)
df_array2 = pd.DataFrame(array2, columns=col_name2)
print('2차원 ndarray로 만든 DataFrame:\n', df_array2)
```

```bash
array2 shape: (2, 3)
2차원 리스트로 만든 DataFrame:
    col1  col2  col3
0     1     2     3
1    11    12    13
2차원 ndarray로 만든 DataFrame:
    col1  col2  col3
0     1     2     3
1    11    12    13
```



### 딕셔너리를 DataFrame으로 바꾸기

```python
# Key는 문자열 칼럼명으로 매핑, Value는 리스트 형(또는 ndarray) 칼럼 데이터로 매핑
dict = {'col1':[1, 11], 'col2':[2, 22], 'col3':[3, 33]}
df_dict = pd.DataFrame(dict)
print('딕셔너리로 만든 DataFrame:\n', df_dict)
```

```bash
딕셔너리로 만든 DataFrame:
    col1  col2  col3
0     1     2     3
1    11    22    33
```



### DataFrame을 ndarray로 바꾸기

```python
# DataFrame을 ndarray로 변환
array3 = df_dict.values
print('df_dict.values 타입:', type(array3), 'df_dict.values shape:', array3.shape)
print(array3)
```

```bash
df_dict.values 타입: <class 'numpy.ndarray'> df_dict.values shape: (2, 3)
[[ 1  2  3]
 [11 22 33]]
```



### DataFrame을 list로 바꾸기

```python
# DataFrame을 리스트로 변환
list3 = df_dict.values.tolist()
print('df_dict.values.tolist() 타입:', type(list3))
print(list3)
```

```bash
df_dict.values.tolist() 타입: <class 'list'>
[[1, 2, 3], [11, 22, 33]]
```



### DataFrame을 딕셔너리로 바꾸기

```python
# DataFrame을 딕셔너리로 변환
dict3 = df_dict.to_dict('list')
print('\n df_dict.to_dict() 타입:', type(dict3))
print(dict3)
```

```bash
 df_dict.to_dict() 타입: <class 'dict'>
{'col1': [1, 11], 'col2': [2, 22], 'col3': [3, 33]}
```



### DataFrame을 칼럼 데이터 세트 생성

```python
titanic_df['Age_0'] = 0
print('칼럼 데이터 생성:\n', titanic_df.head(3))
titanic_df['Age_by_10'] = titanic_df['Age']*10
titanic_df['Family_No'] = titanic_df['SibSp'] + titanic_df['Parch']+1
print('새로운 칼럼생성:\n', titanic_df.head(3))
titanic_df['Age_by_10'] = titanic_df['Age_by_10']+100
print('기존 칼럼 값 일괄적으로 계산:\n', titanic_df.head(3))
```

```bash
칼럼 데이터 생성:
    PassengerId  Survived  Pclass                                               Name  ...     Fare  Cabin  Embarked  Age_0
0            1         0       3                            Braund, Mr. Owen Harris  ...   7.2500    NaN         S      0
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  ...  71.2833    C85         C      0
2            3         1       3                             Heikkinen, Miss. Laina  ...   7.9250    NaN         S      0

[3 rows x 13 columns]
새로운 칼럼생성:
    PassengerId  Survived  Pclass                                               Name  ... Embarked  Age_0  Age_by_10  Family_No
0            1         0       3                            Braund, Mr. Owen Harris  ...        S      0      220.0          2
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  ...        C      0      380.0          2
2            3         1       3                             Heikkinen, Miss. Laina  ...        S      0      260.0          1

[3 rows x 15 columns]
기존 칼럼 값 일괄적으로 계산:
    PassengerId  Survived  Pclass                                               Name  ... Embarked  Age_0  Age_by_10  Family_No
0            1         0       3                            Braund, Mr. Owen Harris  ...        S      0      320.0          2
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  ...        C      0      480.0          2
2            3         1       3                             Heikkinen, Miss. Laina  ...        S      0      360.0          1

[3 rows x 15 columns]
```

