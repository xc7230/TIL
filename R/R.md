# R

- R은 객체지향 프로그래밍 언어 - 데이터, 함수, 차트등 모든 데이터는 객체 형태로 관리

- R은 통계 분석과  data의 시각화를 소프트웨어 환경
- R은 데이터분석에 필요한 최신 알고리즘, 방법론등의 패키지 집합이다.
- R은 data의 시각화를 위한 다양한 그래픽 도구를 제공
- R은 모든 객체는 메모리로 로딩되어 고속으로 처리되고 재사용 가능



## 1. R 기본



### **R패키지 갯수 확인**

```R
available.packages()
```



### **R session은 사용자가 R 프로그램을 시작한 후 R콘솔 시작 ~ 종료까지의 수행된 정보**		

```R
sessioninfo()
```



### **R프로그램 버전, 운영체제 정보, 다국어 지원현황, 기본 설치된 R패키지 정보 출력함**



### **R패키지 설치**

```R
install.packages("stringr")
//update.packages("stringr")
remove.packages("stringr")
```



### **설치된 패기지를 사용하기 위해서 메모리에 로드**

```R
library(stringr)
require(stringr)
```



### **메모리에 로드된 패키지 검색**

```R
search(stringr)
```



### **기본 데이터 셋 보기**

```R
data()
```



### **빈도수 히스토그램**

```R
hist(Nile)
```



### **밀도 기준 히스토그램**

```R
hist(Nile, freq=F)
```



### **분포곡선 그리기**

```R
lines(density(Nile)
```



### **Plots영역에 표시할 그래프 개수 설정**

```R
par(mfrow=c(1,1))
```





### **파일 출력 경로**

```R
pdf("c:/workspceR/sample.pdf")
```



### **정규분포를 따르는 난수 20개 생성해서 히스토그램 생성**

```R
hist(rnorm(20)) 
```



### **출력 파일 닫기**

```R
dev.off()
```



### **변수 선언**

- 첫문자는 영문자로 시작
- 두번째 문자부터는 숫자, _, . 사용가능
- 대소문자 구분
- 예약어 사용불가
- 변수에 저장된 값은 불변



```
x <- 3
id(x)
x <- 'a'
id(x)
```



**R은 변수를 선언 할 떄 자료형(Type)을 선언하지 않습니다**







## **2. 데이터 타입 (Data Type)**

```R
Scalar 변수 - 단일 값(하나의 값)을 저장하는 변수
age <- 30
#age변수는 하나의 값을 저장하고 있는 벡터 타입
벡터(Vector)는 하나 이상의 여러 개의 자료를 저장할 수 있는 1차원의 선형 자료 구조

class(age) 
```



```R
age <- TRUE   #상수객체(TRUE, FALSE)
class(age)
#T변수에 TRUE 저장, F변수에 FALSE 저장
age <-F
class(age)
name <- NA  #결측치
class(name)

sum(10, 20, 30)
[1] 60
sum(10, 20, 30, NA)
[1] NA
sum(10, 20, 30, NA, na.rm=T)
[1] 60

```



### **R Seesion에서 생성한 변수 목록 확인**

```R
ls()
```









## 3. 자료형

### **자료형 확인**

```R
is.numeric(변수)
is.logical(변수)
is.character(변수)
is.na(변수)
is.list(객체)
is.data.frame(객체)
is.array(객체)
is.matrix(객체)
```



### **자료형 형변환**

```R
as.numeric(변수)
as.logical(변수)
as.character(변수)
as.list(객체)
as.data.frame(객체)
as.array(객체)
as.matrix(객체)
as.integer(변수)
as.double(변수)
as.complex(변수)  # 복소수
as.factor(객체)
as.Date(객체)

x<-c("1", "2", "3")
result <- x * 3
#print(result)
result <- as.numeric(x) * 3
#print(result)
result <- as.integer(x) * 3
#print(result)

z<-5.3-3i   #복소수 자료형 생성
class(z)   
Re(z)    #실수부만  반환
Im(z)    #허수부만  반환
is.complex(z)
as.complex(5.3)

#class(변수)는 자료구조의 Type을 반환
#mode(변수)는 자료의 Type을 반환



```



### **NULL**

NULL은 NULL 객체를 뜻하며, 변수가 초기화되지 않았을 때 사용한다.



### 날짜와 시간

```R
Sys.Date() # 날짜만 보여주는 함수
[1] "2019-09-05"
Sys.time() # 날짜와 시간을 보여주는 함수
[1] "2019-09-05 16:37:51 KST"
date() # 미국식 날짜와 시간을 출력하는 함수
[1] "Thu Sep 05 16:37:51 2019"
as.Date('2017-12-01') # 문자형태의 날짜를 날짜타입으로 변환해주는 함수
[1] "2017-12-01"
as.Date('2017/07/04')
[1] "2017-07-04"
as.Date('04-07-2017') #오류
[1] "0004-07-20"
as.Date('2017-12-01' , format='%d-%m-%Y')
[1] NA
as.Date(10, origin='2017-12-01') #주어진 날짜 기준으로 10일후의 날짜
[1] "2017-12-11"
as.Date(-10, origin='2017-12-01') #주어진 날짜 기준으로 10일 이전 날짜
[1] "2017-11-21"


날짜 format
%d 일자를 숫자로 인식
%m 월 을 숫자로 인식
%b 월을 영어 약어로 인식
%B 월을 전체 이릉으로 인식
%y 년도를 숫자 두 자리로 인식
%Y 년도를 숫자 네 자리로 인식

```





### 날짜 산술 연산

```R
as.Date("2017-07-31")-as.Date("2017-07-04")
Time difference of 27 days

#POSIXt : 날짜를 년, 월, 일 로 표시하는 리스트형 클래스
#POSIXct : 날짜를 연속적인 데이터로 인식해서 1970년을 기준으로 초 단위로 계산
#POSIXct 은 R고급 과정에서 회귀분석 등을 할 때 주로 POSIXct를 많이 사용


```



```R
as.Date("2017-07-04 20:00:00 ")-as.Date("2017-07-04 18:30")
Time difference of 0 days

as.POSIXct("2017-07-04 20:00:00 ")-as.POSIXct("2017-07-04 18:30")
Time difference of 1.5 hours

```



### lubridate 패키지로 날짜와 시간 제어하기

```R
date<-now() #현재 날짜와 시간 넣기
date
[1] "2019-09-05 16:44:14 KST"
year(date) #년도만 출력
[1] 2019
month(date,label=T) #월을 영문으로 출력
[1] 9
month(date,label=F) #월을 숫자로 출력
[1] 9
day(date)
[1] 5
wday(date, label=T) # 요일을 영문으로 출력
[1] 5
wday(date, label=F) # 요일을 가중치 숫자로 출력 , 일요일 1 시작
[1] 5
date<-date-days(2) #2일전 날짜 출력
date
[1] "2019-09-03 16:44:14 KST"
month(date)<-2 #2개월 더한 날짜 출력
date
[1] "2019-02-03 16:44:14 KST"
date+years(1) #1년 추가
[1] "2020-02-03 16:44:14 KST"
date+months(1) #1개월 추가
[1] "2019-03-03 16:44:14 KST"
date+hours(1) #1시간 추가
[1] "2019-02-03 17:44:14 KST"
date+minutes(1) #1분 추가
[1] "2019-02-03 16:45:14 KST"
date+seconds(1) #1초 추가
[1] "2019-02-03 16:44:15 KST"
date<-hm("22:30") ; date #시간 분 지정
[1] "22H 30M 0S"
date<-hms("22:30:15") ; date #시간 분 초 지정
[1] "22H 30M 15S"


as.Date("2019-Sep-05", format="%y-%b-%d")

#Sys.setlocale(category="LC_ALL", locale="언어_국가")
#현재 로케일 정보 전체 확인
Sys.setlocale(category="LC_ALL", locale="")
[1] "LC_COLLATE=Korean_Korea.949;LC_CTYPE=Korean_Korea.949;LC_MONETARY=Korean_Korea.949;LC_NUMERIC=C;LC_TIME=Korean_Korea.949"
Sys.getlocale()
[1] "LC_COLLATE=Korean_Korea.949;LC_CTYPE=Korean_Korea.949;LC_MONETARY=Korean_Korea.949;LC_NUMERIC=C;LC_TIME=Korean_Korea.949"
Sys.setlocale(category="LC_ALL", locale="Korean_Korea")
[1] "LC_COLLATE=Korean_Korea.949;LC_CTYPE=Korean_Korea.949;LC_MONETARY=Korean_Korea.949;LC_NUMERIC=C;LC_TIME=Korean_Korea.949"
Sys.getlocale()
[1] "LC_COLLATE=Korean_Korea.949;LC_CTYPE=Korean_Korea.949;LC_MONETARY=Korean_Korea.949;LC_NUMERIC=C;LC_TIME=Korean_Korea.949"

Sys.setlocale(category="LC_ALL", locale="English_US") 
[1] "LC_COLLATE=English_United States.1252;LC_CTYPE=English_United States.1252;LC_MONETARY=English_United States.1252;LC_NUMERIC=C;LC_TIME=English_United States.1252"
Sys.getlocale()
[1] "LC_COLLATE=English_United States.1252;LC_CTYPE=English_United States.1252;LC_MONETARY=English_United States.1252;LC_NUMERIC=C;LC_TIME=English_United States.1252"

Sys.setlocale(category="LC_ALL", locale="Japanese_Japan")
[1] "LC_COLLATE=Japanese_Japan.932;LC_CTYPE=Japanese_Japan.932;LC_MONETARY=Japanese_Japan.932;LC_NUMERIC=C;LC_TIME=Japanese_Japan.932"
Sys.getlocale()
[1] "LC_COLLATE=Japanese_Japan.932;LC_CTYPE=Japanese_Japan.932;LC_MONETARY=Japanese_Japan.932;LC_NUMERIC=C;LC_TIME=Japanese_Japan.932"

```



### 변수확인, 삭제

```R
objects( ) # 생성한 모든 변수 확인
 [1] "a"      "age"    "b"      "date"   "name"  
 [6] "result" "T"      "x"      "y"      "z"     
rm(list=ls()) # 모든 변수들을 삭제
rm(var3) # 변수 삭제

```



### 기본 함수, 파라미터 형식 예제

```R
example(seq)

seq> seq(0, 1, length.out = 11)
 [1] 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0

seq> seq(stats::rnorm(20)) # effectively 'along'
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
[17] 17 18 19 20

seq> seq(1, 9, by = 2)     # matches 'end'
[1] 1 3 5 7 9

seq> seq(1, 9, by = pi)    # stays below 'end'
[1] 1.000000 4.141593 7.283185

seq> seq(1, 6, by = 3)
[1] 1 4

seq> seq(1.575, 5.125, by = 0.05)
 [1] 1.575 1.625 1.675 1.725 1.775 1.825 1.875 1.925
 [9] 1.975 2.025 2.075 2.125 2.175 2.225 2.275 2.325
[17] 2.375 2.425 2.475 2.525 2.575 2.625 2.675 2.725
[25] 2.775 2.825 2.875 2.925 2.975 3.025 3.075 3.125
[33] 3.175 3.225 3.275 3.325 3.375 3.425 3.475 3.525
[41] 3.575 3.625 3.675 3.725 3.775 3.825 3.875 3.925
[49] 3.975 4.025 4.075 4.125 4.175 4.225 4.275 4.325
[57] 4.375 4.425 4.475 4.525 4.575 4.625 4.675 4.725
[65] 4.775 4.825 4.875 4.925 4.975 5.025 5.075 5.125

seq> seq(17) # same as 1:17, or even better seq_len(17)
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
[17] 17
#R에서 제공하는 함수의 파라미터 형식 보기
args(max)
function (..., na.rm = FALSE) 
NULL
```



### Factor 형

여러 번 중복으로 나오는 데이터들을 각 값으로 모아서 대표 값을 출력해 주는 형태
stringsAsFactors=FALSE 옵션은 대표값으로 정리하지 않고 중복되는 상태 그대로 사용하게 해 줍
니다.
범주형Categorical 데이터(자료)를 표현하기 위한 데이터 타입
범주형 데이터 - 데이터가 사전에 정해진 특정 유형으로만 분류되는 경우
범주형 데이터는 또 다시 명목형Nominal과 순서형Ordinal으로 구분
명목형 데이터는 값들 간에 크기 비교가 불가능한 경우
순서형 데이터는 대, 중, 소와 같이 값에 순서를 둘 수 있는 경우



```R
gender <- c("man","woman", "woman", "man", "man")
plot(gender)  #차트는 수치 데이터만 가능하므로 오류
Error in plot.window(...) : need finite 'ylim' values
In addition: Warning messages:
1: In xy.coords(x, y, xlabel, ylabel, log) : NAs introduced by coercion
2: In min(x) : no non-missing arguments to min; returning Inf
3: In max(x) : no non-missing arguments to max; returning -Inf

ngender <- as.factor(gender)
class(ngender)
[1] "factor"
mode(ngender)
[1] "numeric"
table(ngender) #빈도수 반환
ngender
  man woman 
    3     2 
plot(ngender)

is.factor(ngender)
[1] TRUE
ngender    #Levels속성에서 범주를 확인 
[1] man   woman woman man   man  
Levels: man woman

ngender    #Levels속성에서 범주를 확인 
[1] man   woman woman man   man  
Levels: man woman
args(factor)  #factor()함수의 매개변수 확인
function (x = character(), levels, labels = levels, exclude = NA, 
    ordered = is.ordered(x), nmax = NA) 
NULL




```

plot(ngender)

![1567671983338](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1567671983338.png)



```R
plot(ogender)
par(mfrow=c(1, 2))
plot(ngender)
plot(ogender)
```

![1567672437487](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1567672437487.png)



### Vector 형

동일한 형태의 데이터를 모아서 함께 저장
1차원 배열과 비슷한 개념, 특정 항목의 요소를 사용하려면 벡터명[색인] 벡터 자체를 연산 할 수 있습니다.
각 벡터의 요소에 names() 함수를 사용해서 이름 지정할 수 있습니다.
seq(), rep() 함수를 사용해서 벡터에 연속적인 데이터 할당 할 수 있습니다.
length() 함수는 벡터의 길이를 리턴합니다.
%in%는 벡터에 특정 문자의 포함 여부를 리턴합니다

```R
c(1:20)
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
[17] 17 18 19 20
1:20
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
[17] 17 18 19 20
c(1,1,2,3,3,3,4,5,5,5,5)
 [1] 1 1 2 3 3 3 4 5 5 5 5
seq(1, 20)
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
[17] 17 18 19 20
seq(1, 20, 2) #2씩 증가하면서 구조 생성
 [1]  1  3  5  7  9 11 13 15 17 19
rep(1:3, 3) 
[1] 1 2 3 1 2 3 1 2 3
rep(1:3, each=3)
[1] 1 1 1 2 2 2 3 3 3
a<-c(1:5)
b<-a+1
c<-a*2
a<-c(1:5)
b<-a+1
c<-a*2
d <- rep(1:3, 3) 
union(a, d) #합집합
[1] 1 2 3 4 5
setdiff(a, d) #차집합
[1] 4 5
intersect(a, d) #교집합
[1] 1 2 3
f <- c(33, -5, "4", 5:9 ) # 자료형이 혼합된 경우, 문자열이 포함된 경우, 문자열로 자동 형변환
class(f)
[1] "character"
mode(f)
[1] "character"
a<-c(1:20)
a[3:10]   #벡터의 요소에 접근
[1]  3  4  5  6  7  8  9 10
a[c(3, 10)]  #벡터의 요소에 접근
[1]  3 10

```





