# R 자료형

- 벡터를 여러 개 합친 형태, 2차원으로 데이터를 저장합니다.
- 동일한 데이터 유형만 저장
- rbind()로 행을 추가할 수 있다
- cbind()로 컬럼을 추가할 수 있다.
- 컬럼 이름을 지정, 조회하려면 colnames() 사용
- 행이름 지정, 조회하려면 rownames() 사용



## Matrix

- 기본적으로 열기준 2차원 데이터 저장

```R
M <- matrix(c(3: 14))
print(M)
      [,1]
 [1,]    3
 [2,]    4
 [3,]    5
 [4,]    6
 [5,]    7
 [6,]    8
 [7,]    9
 [8,]   10
 [9,]   11
[10,]   12
[11,]   13
[12,]   14
str(M)
 int [1:12, 1] 3 4 5 6 7 8 9 10 11 12 ...
 
M1 <- matrix(c(3:14), nrow=3)
print(M1)
     [,1] [,2] [,3] [,4]
[1,]    3    6    9   12
[2,]    4    7   10   13
[3,]    5    8   11   14
str(M1)
 int [1:3, 1:4] 3 4 5 6 7 8 9 10 11 12 ...
M2 <- matrix(c(3:14), nrow=4 , byrow = TRUE)
print(M2)
     [,1] [,2] [,3]
[1,]    3    4    5
[2,]    6    7    8
[3,]    9   10   11
[4,]   12   13   14
str(M2)
 int [1:4, 1:3] 3 6 9 12 4 7 10 13 5 8 ...

x1 <- c(5, 40, 50:52)
x2 <- c(30, 5, 6:8)
M3 <- rbind(x1, x2)  #행결합
print(M3)
   [,1] [,2] [,3] [,4] [,5]
x1    5   40   50   51   52
x2   30    5    6    7    8
str(M3)
 num [1:2, 1:5] 5 30 40 5 50 6 51 7 52 8
 - attr(*, "dimnames")=List of 2
  ..$ : chr [1:2] "x1" "x2"
  ..$ : NULL
 
M4 <- cbind(x1, x2)  #열결합
print(M4)
     x1 x2
[1,]  5 30
[2,] 40  5
[3,] 50  6
[4,] 51  7
[5,] 52  8
str(M4)
 num [1:5, 1:2] 5 40 50 51 52 30 5 6 7 8
 - attr(*, "dimnames")=List of 2
  ..$ : NULL
  ..$ : chr [1:2] "x1" "x2"

M <- matrix(10: 20, 2)
Warning message:
In matrix(10:20, 2) :
  data length [11] is not a sub-multiple or multiple of the number of rows [2]
print(M)
     [,1] [,2] [,3] [,4] [,5] [,6]
[1,]   10   12   14   16   18   20
[2,]   11   13   15   17   19   10

rownames <- c("row1", "row2", "row3", "row4")
colnames <- c("col1", "col2", "col3")
 
M5 <- matrix(c(3:14), nrow = 4, byrow = TRUE, dimnames = list(rownames, colnames))
print(M5)
     col1 col2 col3
row1    3    4    5
row2    6    7    8
row3    9   10   11
row4   12   13   14
str(M5)
 int [1:4, 1:3] 3 6 9 12 4 7 10 13 5 8 ...
 - attr(*, "dimnames")=List of 2
  ..$ : chr [1:4] "row1" "row2" "row3" "row4"
  ..$ : chr [1:3] "col1" "col2" "col3"
 
P1 <-cbind(M5, c(13,14,15,16)) #cbind()는  컬럼을 추가
print(P1)  #4행 4열
     col1 col2 col3   
row1    3    4    5 13
row2    6    7    8 14
row3    9   10   11 15
row4   12   13   14 16
 
P2 <-rbind(M5, c(13,14,15))  #rbind() 는 행을 추가
print(P2) #5행 3열
     col1 col2 col3
row1    3    4    5
row2    6    7    8
row3    9   10   11
row4   12   13   14
       13   14   15
 
print(M5+P1)  # 열 개수가 다름 error 발생
Error in M5 + P1 : non-conformable arrays
print(M5+P2)  # 행 개수가 다름 error 발생
Error in M5 + P2 : non-conformable arrays


# Matrix 요소에 접근 - 변수[첨자, 첨자]
# 특정 행이나 특정 열만 접근하는 경우 변수명[행첨자, ], 변수명[, 열첨자] 형식으로 지정
print(M5[1,3])
[1] 5
print(M5[2,])  #2행 전체 요소에 접근
col1 col2 col3 
   6    7    8 
print(M5[,3])   #3열 전체 요소에 접근
row1 row2 row3 row4 
   5    8   11   14 
print(M5["row1",])  #1행 전체 요소에 접근
col1 col2 col3 
   3    4    5 
print(M5[,"col3"])   #3열 전체 요소에 접근
row1 row2 row3 row4 
   5    8   11   14 



# Matrix 연산
matrix1 <- matrix(c(3, 9, -1, 4, 2, 6), nrow = 2)
matrix2 <- matrix(c(5, 2, 0, 9, 3, 4), nrow = 2)
result <- matrix1 + matrix2
cat("Result of addition","\n")
Result of addition 
print(result)
     [,1] [,2] [,3]
[1,]    8   -1    5
[2,]   11   13   10

result <- matrix1 + 10
print(result)
     [,1] [,2] [,3]
[1,]   13    9   12
[2,]   19   14   16
print(length(result))  #전체 원소 개수 반환
[1] 6
print(nrow(result))  #행 수 반환
[1] 2
print(ncol(result))  #열 수 반환
[1] 3

#base패키지의 apply함수 apply(행렬객체, margin(1:행, 2:열), function)
f <- function(x) {  #사용자 정의 함수 
 x*c(1,2,3)
}
result <- apply(matrix1, 1, f)
print(result)
     [,1] [,2]
[1,]    3    9
[2,]   -2    8
[3,]    6   18
 
result <- apply(matrix(1:9, ncol=3), 2, f)
print(result)
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    4   10   16
[3,]    9   18   27


 m1 <- matrix(c(1:9), ncol = 3, byrow = TRUE)
> print(m1)
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
[3,]    7    8    9
> print(t(m1))
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9

m2 <- matrix(rep(1:3, times=3), nrow = 3)
print(m2)
     [,1] [,2] [,3]
[1,]    1    1    1
[2,]    2    2    2
[3,]    3    3    3
print(t(m2))
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    1    2    3
[3,]    1    2    3


m3<-m1[, -c(1, 3)]   #matrix에서 하나의 열을 남겨놓고, 모든 열을 제거하고, 벡터가 됨
print(m3)
[1] 2 5 8
str(m3)
int [1:3] 2 5 8
 
m3<-m1[, -c(1, 3), drop=FALSE]    #벡터로 변환되지 않도록 matrix의 구조 유지하도록 drop옵션
print(m3)
     [,1]
[1,]    2
[2,]    5
[3,]    8
str(m3)
 int [1:3, 1] 2 5 8
 
rownames(M5) 
NULL
colnames(M5) 
NULL
#문> 행이름과 열이름을 제거
rownames(M5) <- NULL
colnames(M5) <- NULL
print(M5)
     [,1] [,2] [,3]
[1,]    3    4    5
[2,]    6    7    8
[3,]    9   10   11
[4,]   12   13   14
str(M5)
 int [1:4, 1:3] 3 6 9 12 4 7 10 13 5 8 ...
 - attr(*, "dimnames")=List of 2
  ..$ : NULL
  ..$ : NULL






```













## apply(data객체, margin,  function)

```R
rs1 <- apply(array2, c(1), sum)
print(result)
, , Matrix1

COL1 COL2 COL3
ROW1    5   10   13
ROW2    9   11   14
ROW3    3   12   15

, , Matrix2
 COL1 COL2 COL3
ROW1    5   10   13
ROW2    9   11   14
ROW3    3   12   15
```







## Array 

#######################################################
Array - 동일한 자료형을 갖는 다차원 배열 구조
array() - 행, 열, 면의 3차원 배열 형태의 객체를 생성
첨자로 접근
다른 자료구조에 비해 상대적으로 활용도가 낮음
#######################################################

```R
m4 <- matrix(c(1,2,3,4,5,4,3,2,1), ncol=3)
result <- solve(m4)  #역행렬 결과 리턴
print(result)
       [,1] [,2]   [,3]
[1,]  0.375   -1  0.875
[2,] -0.500    1 -0.500
[3,]  0.875   -1  0.375

print(m4 %*% result)
              [,1]          [,2]          [,3]
[1,]  1.000000e+00 -4.440892e-16  0.000000e+00
[2,]  2.220446e-16  1.000000e+00 -1.110223e-16
[3,] -1.110223e-16 -4.440892e-16  1.000000e+00
```



List 

##########################################################################
List - 서로 다른 자료구조(벡터, 행렬, 리스트, 데이터프레임 등)을 객체로 구성
키(key)와 값(value)의 한쌍으로 저장
c언어의 구조체, python의 dict 자료구조, java의 map컬렉션 구조와 유사
key를 통해 value 접근
value에 저장되는 자료구조는 벡터, 행렬, 리스트, 데이터프레임 등 대부분의 R객체 저장 가능
함수 내에서 여러 값을 하나의 키로 묶어서 반환하는 경우 유용
list(key1=value1, key2=value2, ...)
##################################################################

```R
emp1 <- list(name='kim', address='seoul', age=30, hiredate=as.Date('2017/01/02'))
> print(emp1)
$name
[1] "kim"

$address
[1] "seoul"

$age
[1] 30

$hiredate
[1] "2017-01-02"

> str(emp1)
List of 4
 $ name    : chr "kim"
 $ address : chr "seoul"
 $ age     : num 30
 $ hiredate: Date[1:1], format: "2017-01-02"
> 
> list_data <- list("Red", "Green", c(21,32,11), TRUE, 51.23, 119.1)
> print(list_data)
[[1]]
[1] "Red"

[[2]]
[1] "Green"

[[3]]
[1] 21 32 11

[[4]]
[1] TRUE

[[5]]
[1] 51.23

[[6]]
[1] 119.1

> str(list_data)
List of 6
 $ : chr "Red"
 $ : chr "Green"
 $ : num [1:3] 21 32 11
 $ : logi TRUE
 $ : num 51.2
 $ : num 119
> 
> #list의 요소 접근
> print(emp1[1:2])  #색인으로 데이터 값 access
$name
[1] "kim"

$address
[1] "seoul"

> print(emp1$age)  #key로 데이터 값 access
[1] 30
> 
> #문] 아래 list_data리스트의 요소중에서 k3에 저장된 세번째 요소만 출력
> list_data <- list(k1="Red", k2="Green", k3=c(21,32,11), 
+                   k4=TRUE, k5=51.23, k6=119.1)
> print(list_data$k3[3])
[1] 11
> 
> tracemem(emp1)
[1] "<000000001F8DDF60>"
> emp1$deptno <- 10 #리스트 객체에 새로운 data 추가
tracemem[0x000000001f8ddf60 -> 0x000000001f8d2180]: 
> str(emp1)
List of 5
 $ name    : chr "kim"
 $ address : chr "seoul"
 $ age     : num 30
 $ hiredate: Date[1:1], format: "2017-01-02"
 $ deptno  : num 10
> tracemem(emp1)
[1] "<000000001DCC5CE8>"
> 
> emp1$age <- NULL      #리스트의 요소를 제거
tracemem[0x000000001dcc5ce8 -> 0x000000001d9bcd08]: 
> str(emp1)
List of 4
 $ name    : chr "kim"
 $ address : chr "seoul"
 $ hiredate: Date[1:1], format: "2017-01-02"
 $ deptno  : num 10


# 리스트내에 값의 타입을 리스트 저장 가능 
> lst2 <- list(cost=list(val=c(100, 150, 200)) , 
+              price=list(val=c(200,250,300)))
> str(lst2)
List of 2
 $ cost :List of 1
  ..$ val: num [1:3] 100 150 200
 $ price:List of 1
  ..$ val: num [1:3] 200 250 300
> print(lst2)
$cost
$cost$val
[1] 100 150 200


$price
$price$val
[1] 200 250 300


> 
> 
> #cost 키의 두번째 요소를 출력
> print(lst2$cost$val[2]) 
[1] 150
> #price 키의 세번째 요소를 출력
> print(lst2$price$val[3])
[1] 300
> 
> lst <- list()
> str(lst)
 list()
> lst[[1]]<-0.5    #list에 키없이 첫번째 data저장
> lst[[2]]<-c("a","c", "f")   #list에 키없이 두번째 data저장
> str(lst)
List of 2
 $ : num 0.5
 $ : chr [1:3] "a" "c" "f"
> lst[["price"]] <- c(100,200,300)
> str(lst)
List of 3
 $      : num 0.5
 $      : chr [1:3] "a" "c" "f"
 $ price: num [1:3] 100 200 300
> 
> 
> #unlist 함수 : 기본적인 통계 함수들은 벡터에서는 동작하지만 리스트에는 동작하지 않는 경우,
> #리스트 구조를 제거하고, 벡터로 만들어주는 함수
> 
> vec_emp1<-unlist(emp1)  #서로 다른 데이터 타입의 값들이 chracter로 변환되어 named 벡터로 생성됨
> str(vec_emp1)
 Named chr [1:4] "kim" "seoul" "17168" "10"
 - attr(*, "names")= chr [1:4] "name" "address" "hiredate" "deptno"
> 
> 
> #문> 
> exam1<- list(1,0, 2,0, -3, 4, -5, 6, 7, -8, 9, 10)
> #exam1로부터 음수를 제거한 리스트 출력
> 
> 
> #exam1로부터 0를 제거한 리스트 출력


#exam1로부터 음수를 제거한 리스트 출력
> tracemem(exam1)
[1] "<000000001EEAD8A8>"
> exam1[exam1<0]<-NULL
tracemem[0x000000001eead8a8 -> 0x000000001dbf51b8]: 
> print(exam1)
[[1]]
[1] 1

[[2]]
[1] 2

[[3]]
[1] 4

[[4]]
[1] 6

[[5]]
[1] 7

[[6]]
[1] 9

[[7]]
[1] 10

> tracemem(exam1)
[1] "<000000001DBF51B8>"
> #exam1로부터 0를 제거한 리스트 출력
> tracemem(exam1)
[1] "<000000001DBF51B8>"
> exam1[exam1==0]<-NULL
tracemem[0x000000001dbf51b8 -> 0x000000001dbf5378]: 
> print(exam1)
[[1]]
[1] 1

[[2]]
[1] 2

[[3]]
[1] 4

[[4]]
[1] 6

[[5]]
[1] 7

[[6]]
[1] 9

[[7]]
[1] 10

> tracemem(exam1)
[1] "<000000001DBF5378>"
> 
> 
> #lapply 함수는 데이터 객체에 함수를 적용한 결과를 list형태로 반환
> a<- list(c(1:5))
> b<- list(6:10)
> result <-lapply(c(a, b), max) 
> print(result)
[[1]]
[1] 5

[[2]]
[1] 10

> str(result)
List of 2
 $ : int 5
 $ : int 10
> 
> 
> #sapply 함수는 데이터 객체에 함수를 적용한 결과를 벡터 형식로 반환
> result <- sapply(c(a, b), max)
> print(result)
[1]  5 10
> str(result)
 int [1:2] 5 10
> 
> 
> #다차원(중첩) 리스트 - 리스트 자료구조에 다른 리스트가 중첩된 자료구조
> multi_list <- list(c1 = list(1, 2, 3),
+                    c2 = list(10, 20, 30),
+                    c3 = list(100, 200, 300))
>                    print(multi_list)
$c1
$c1[[1]]
[1] 1

$c1[[2]]
[1] 2

$c1[[3]]
[1] 3


$c2
$c2[[1]]
[1] 10

$c2[[2]]
[1] 20

$c2[[3]]
[1] 30


$c3
$c3[[1]]
[1] 100

$c3[[2]]
[1] 200

$c3[[3]]
[1] 300


>                    
>                    #다차원 리스트를 열단위로 바인딩
>                    do.call(cbind, multi_list)
     c1 c2 c3 
[1,] 1  10 100
[2,] 2  20 200
[3,] 3  30 300





```



## DataFrame

###########################################################
DataFrame - 데이터베이스의 테이블 구조와 유사
R에서 가장 많이 사용하는 자료구조
컬럼 단위로 서로 다른 데이터의 저장이 가능
리스트와 벡터의 혼합형으로 컬럼은 리스트, 컬럼 내의 데이터는 벡터 자료구조를 갖는다
DataFrame 생성함수 - data.frame(), read.table(), read.csv()
txt, excel, csv 파일로부터 DataFrame 생성
data.frame(컬럼1=자료, 컬럼2=자료, ...컬럼n=자료)
########################################################### 

- 여러 개의 벡터 객체를 이용하여 데이터프레임을 생성할 수 있다. 
- 이때 모든 컬럼은 길이가 같아야 한다. 컬럼의 길이가 서로 다르면 오류가 발생한다.

```R
d1<- data.frame(no=c(1,2,3,4,5), 
+                 name=c('kim', 'park', 'lee', 'song', 'hong'),
+                 gender=c('F', 'W', 'M', 'W', 'M') )
> str(d1)
'data.frame':	5 obs. of  3 variables:
 $ no    : num  1 2 3 4 5
 $ name  : Factor w/ 5 levels "hong","kim","lee",..: 2 4 3 5 1
 $ gender: Factor w/ 3 levels "F","M","W": 1 3 2 3 2
> print(d1)
  no name gender
1  1  kim      F
2  2 park      W
3  3  lee      M
4  4 song      W
5  5 hong      M
> 
> no<-c(1,2,3)
> name<-c("hong", "lee", "kim")
> pay <-c(150, 250, 300)
> vemp <- data.frame(NO=no, Name=name, Pay=pay)  #컬럼명 지정
> str(vemp)
'data.frame':	3 obs. of  3 variables:
 $ NO  : num  1 2 3
 $ Name: Factor w/ 3 levels "hong","kim","lee": 1 3 2
 $ Pay : num  150 250 300
> print(vemp)
  NO Name Pay
1  1 hong 150
2  2  lee 250
3  3  kim 300
> 
> 
> sales1 <- matrix(c(1, 'Apple', 500, 5, 
+                    2, 'Peach', 200, 2, 
+                    3, 'Banana', 100, 4, 
+                    4, 'Grape', 50, 7) , nrow=4, byrow=T)
> str(sales1)
 chr [1:4, 1:4] "1" "2" "3" "4" "Apple" "Peach" ...
> df1 <- data.frame(sales1)
> str(df1)  #각 컬럼의 데이터 타입은?  컬럼이름은?
'data.frame':	4 obs. of  4 variables:
 $ X1: Factor w/ 4 levels "1","2","3","4": 1 2 3 4
 $ X2: Factor w/ 4 levels "Apple","Banana",..: 1 4 2 3
 $ X3: Factor w/ 4 levels "100","200","50",..: 4 2 1 3
 $ X4: Factor w/ 4 levels "2","4","5","7": 3 1 2 4
> 
> 
> df1 <- data.frame(sales1, stringsAsFactors=FALSE)
> str(df1)
'data.frame':	4 obs. of  4 variables:
 $ X1: chr  "1" "2" "3" "4"
 $ X2: chr  "Apple" "Peach" "Banana" "Grape"
 $ X3: chr  "500" "200" "100" "50"
 $ X4: chr  "5" "2" "4" "7"
> names(df1) <- c('No', 'Fruit', 'Price', 'Qty')
> str(df1) 
'data.frame':	4 obs. of  4 variables:
 $ No   : chr  "1" "2" "3" "4"
 $ Fruit: chr  "Apple" "Peach" "Banana" "Grape"
 $ Price: chr  "500" "200" "100" "50"
 $ Qty  : chr  "5" "2" "4" "7"
> 
> #as.numeric()함수는 numeric변환
> df1$Qty <- as.numeric(df1$Qty)
> df1$Price <- as.numeric(df1$Price)
> str(df1) 
'data.frame':	4 obs. of  4 variables:
 $ No   : chr  "1" "2" "3" "4"
 $ Fruit: chr  "Apple" "Peach" "Banana" "Grape"
 $ Price: num  500 200 100 50
 $ Qty  : num  5 2 4 7
> 
> 
> #data.frame 객체의 요소에 접근 : 변수명$컬럼명 형식으로 요소 접근, 결과는 벡터로 반환
> print(d1$name) #컬럼이름으로 data.frame 의 특정 컬럼 데이터 모두 access
[1] kim  park lee  song hong
Levels: hong kim lee park song
> 
> #데이터프레임에 새로운 열 추가
> d1$age <- c(30,31,32,33,34)  
> str(d1)
'data.frame':	5 obs. of  4 variables:
 $ no    : num  1 2 3 4 5
 $ name  : Factor w/ 5 levels "hong","kim","lee",..: 2 4 3 5 1
 $ gender: Factor w/ 3 levels "F","M","W": 1 3 2 3 2
 $ age   : num  30 31 32 33 34
> 
> 
> #조건에 맞는 데이터만 추출 subset(데이터프레임 객체, 조건) : 조건에 만족하는 행을 추출하여 독립된 객체를 생성
> # df1 데이터 프레임에서 수량이 5보다 큰 추출 출력
> subset.df1 <- subset(df1, (Qty>5)) 
> print(subset.df1)
  No Fruit Price Qty
4  4 Grape    50   7
> str(subset.df1)
'data.frame':	1 obs. of  4 variables:
 $ No   : chr "4"
 $ Fruit: chr "Grape"
 $ Price: num 50
 $ Qty  : num 7
> 
> # 문)df1 데이터 프레임에서 가격이 150보다 작은 데이터들 출력
> result <- subset(df1, Price<150)
> print(result)
  No  Fruit Price Qty
3  3 Banana   100   4
4  4  Grape    50   7
> str(result)
'data.frame':	2 obs. of  4 variables:
 $ No   : chr  "3" "4"
 $ Fruit: chr  "Banana" "Grape"
 $ Price: num  100 50
 $ Qty  : num  4 7
> 
> # 문)df1 데이터 프레임에서 과일명이 바나나인것만  data.frame 구조로  출력
> print(subset(df1, Fruit=='Banana')) 
  No  Fruit Price Qty
3  3 Banana   100   4
> 
> df2<-data.frame(x=c(1:5), 
+                 y=seq(2, 10, 2), 
+                 z=c('a', 'b', 'c', 'd', 'e'))
> #문) df2 데이터프레임객체의 x컬럼의 값이 2이상이고  y컬럼은 6이하인 데이터들로 구성된 데이터프레임 부분집합 생성
> xand <- subset(df2, x>=2 & y<=6)
> 
> 
> #문> df2 데이터프레임객체의 x컬럼의 값이 2이상 또는  y컬럼은 6이하인 데이터들로 구성된 데이터프레임 부분집합 생성
> xor <- subset(df2, x>=2 | y<=6)
> 
> 
> #데이터 프레임에서 특정 컬럼만 추출해서 새로운 형태의 데이터프레임 생성
> df5 <- subset(df1, select=c( Fruit, Price, Qty))
> str(df5)
'data.frame':	4 obs. of  3 variables:
 $ Fruit: chr  "Apple" "Peach" "Banana" "Grape"
 $ Price: num  500 200 100 50
 $ Qty  : num  5 2 4 7
> print(df5)
   Fruit Price Qty
1  Apple   500   5
2  Peach   200   2
3 Banana   100   4
4  Grape    50   7
> 
> df6 <- subset(df1, select=-No)
> str(df6)
'data.frame':	4 obs. of  3 variables:
 $ Fruit: chr  "Apple" "Peach" "Banana" "Grape"
 $ Price: num  500 200 100 50
 $ Qty  : num  5 2 4 7
> print(df6) 
   Fruit Price Qty
1  Apple   500   5
2  Peach   200   2
3 Banana   100   4
4  Grape    50   7
> 
> 
> 
> emp.data <- data.frame(
+   emp_id = c (1:5), 
+   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
+   salary = c(623.3,515.2,611.0,729.0,843.25), 
+   
+   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
+                          "2015-03-27")),
+   stringsAsFactors = FALSE
+ )
> print(emp.data) 
  emp_id emp_name salary start_date
1      1     Rick 623.30 2012-01-01
2      2      Dan 515.20 2013-09-23
3      3 Michelle 611.00 2014-11-15
4      4     Ryan 729.00 2014-05-11
5      5     Gary 843.25 2015-03-27
> str(emp.data)
'data.frame':	5 obs. of  4 variables:
 $ emp_id    : int  1 2 3 4 5
 $ emp_name  : chr  "Rick" "Dan" "Michelle" "Ryan" ...
 $ salary    : num  623 515 611 729 843
 $ start_date: Date, format: "2012-01-01" ...
> #문> emp.data객체에서  3행, 5행의 2열과 4열의 데이터만 추출해서 출력
result <- emp.data[c(3,5),c(2,4)]
> print(result)
  emp_name start_date
3 Michelle 2014-11-15
5     Gary 2015-03-27


#summary()는 데이터프레임 객체의 데이터를 대상으로 최소값, 최대값, 중위수, 평균, 사분위수 값을 요약하여 반환
> summary(df2)
       x           y      z    
 Min.   :1   Min.   : 2   a:1  
 1st Qu.:2   1st Qu.: 4   b:1  
 Median :3   Median : 6   c:1  
 Mean   :3   Mean   : 6   d:1  
 3rd Qu.:4   3rd Qu.: 8   e:1  
 Max.   :5   Max.   :10        
> 
> apply(df2[, c(1,2)], 2, sum) 
 x  y 
15 30 
> 
> 
> df4 <- data.frame(name=c('apple', 'banana', 'cherry'), 
+                   price=c(300, 200, 100))
> df5 <- data.frame(name=c('apple', 'cherry', 'berry'), 
+                   qty=c(10, 20, 30))
> 
> #두 데이터프레임 객체의 요소를 병합  
> result1<- merge(df4, df5) 
> #첫번째 열 데이터 기준으로 일치하는 데이터의 열 결합
> print(result1) 
    name price qty
1  apple   300  10
2 cherry   100  20
> str(result1)
'data.frame':	2 obs. of  3 variables:
 $ name : Factor w/ 3 levels "apple","banana",..: 1 3
 $ price: num  300 100
 $ qty  : num  10 20
> 
> result2<- merge(df4, df5, all=T) 
> ##첫번째 열 데이터 기준으로 모든 데이터의 열 결합,  Data가 없으면 NA로 채움
> print(result2)
    name price qty
1  apple   300  10
2 banana   200  NA
3 cherry   100  20
4  berry    NA  30
> str(result2)
'data.frame':	4 obs. of  3 variables:
 $ name : Factor w/ 4 levels "apple","banana",..: 1 2 3 4
 $ price: num  300 200 100 NA
 $ qty  : num  10 NA 20 30
> 
> 
> str(mtcars)
'data.frame':	32 obs. of  11 variables:
 $ mpg : num  21 21 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 ...
 $ cyl : num  6 6 4 6 8 6 8 4 4 6 ...
 $ disp: num  160 160 108 258 360 ...
 $ hp  : num  110 110 93 110 175 105 245 62 95 123 ...
 $ drat: num  3.9 3.9 3.85 3.08 3.15 2.76 3.21 3.69 3.92 3.92 ...
 $ wt  : num  2.62 2.88 2.32 3.21 3.44 ...
 $ qsec: num  16.5 17 18.6 19.4 17 ...
 $ vs  : num  0 0 1 1 0 1 0 1 1 1 ...
 $ am  : num  1 1 1 0 0 0 0 0 0 0 ...
 $ gear: num  4 4 4 3 3 3 3 4 4 4 ...
 $ carb: num  4 4 1 1 2 1 4 2 2 4 ...
> head(mtcars) # 1~6행만 출력해줌
                   mpg cyl disp  hp drat    wt  qsec
Mazda RX4         21.0   6  160 110 3.90 2.620 16.46
Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02
Datsun 710        22.8   4  108  93 3.85 2.320 18.61
Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44
Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02
Valiant           18.1   6  225 105 2.76 3.460 20.22
                  vs am gear carb
Mazda RX4          0  1    4    4
Mazda RX4 Wag      0  1    4    4
Datsun 710         1  1    4    1
Hornet 4 Drive     1  0    3    1
Hornet Sportabout  0  0    3    2
Valiant            1  0    3    1
> head(mtcars, 20)
                     mpg cyl  disp  hp drat    wt
Mazda RX4           21.0   6 160.0 110 3.90 2.620
Mazda RX4 Wag       21.0   6 160.0 110 3.90 2.875
Datsun 710          22.8   4 108.0  93 3.85 2.320
Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215
Hornet Sportabout   18.7   8 360.0 175 3.15 3.440
Valiant             18.1   6 225.0 105 2.76 3.460
Duster 360          14.3   8 360.0 245 3.21 3.570
Merc 240D           24.4   4 146.7  62 3.69 3.190
Merc 230            22.8   4 140.8  95 3.92 3.150
Merc 280            19.2   6 167.6 123 3.92 3.440
Merc 280C           17.8   6 167.6 123 3.92 3.440
Merc 450SE          16.4   8 275.8 180 3.07 4.070
Merc 450SL          17.3   8 275.8 180 3.07 3.730
Merc 450SLC         15.2   8 275.8 180 3.07 3.780
Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250
Lincoln Continental 10.4   8 460.0 215 3.00 5.424
Chrysler Imperial   14.7   8 440.0 230 3.23 5.345
Fiat 128            32.4   4  78.7  66 4.08 2.200
Honda Civic         30.4   4  75.7  52 4.93 1.615
Toyota Corolla      33.9   4  71.1  65 4.22 1.835
                     qsec vs am gear carb
Mazda RX4           16.46  0  1    4    4
Mazda RX4 Wag       17.02  0  1    4    4
Datsun 710          18.61  1  1    4    1
Hornet 4 Drive      19.44  1  0    3    1
Hornet Sportabout   17.02  0  0    3    2
Valiant             20.22  1  0    3    1
Duster 360          15.84  0  0    3    4
Merc 240D           20.00  1  0    4    2
Merc 230            22.90  1  0    4    2
Merc 280            18.30  1  0    4    4
Merc 280C           18.90  1  0    4    4
Merc 450SE          17.40  0  0    3    3
Merc 450SL          17.60  0  0    3    3
Merc 450SLC         18.00  0  0    3    3
Cadillac Fleetwood  17.98  0  0    3    4
Lincoln Continental 17.82  0  0    3    4
Chrysler Imperial   17.42  0  0    3    4
Fiat 128            19.47  1  1    4    1
Honda Civic         18.52  1  1    4    2
Toyota Corolla      19.90  1  1    4    1
> tail(mtcars) #last-5 ~ last행까지 출력해줌
                mpg cyl  disp  hp drat    wt qsec vs
Porsche 914-2  26.0   4 120.3  91 4.43 2.140 16.7  0
Lotus Europa   30.4   4  95.1 113 3.77 1.513 16.9  1
Ford Pantera L 15.8   8 351.0 264 4.22 3.170 14.5  0
Ferrari Dino   19.7   6 145.0 175 3.62 2.770 15.5  0
Maserati Bora  15.0   8 301.0 335 3.54 3.570 14.6  0
Volvo 142E     21.4   4 121.0 109 4.11 2.780 18.6  1
               am gear carb
Porsche 914-2   1    5    2
Lotus Europa    1    5    2
Ford Pantera L  1    5    4
Ferrari Dino    1    5    6
Maserati Bora   1    5    8
Volvo 142E      1    4    2
> data(mtcars)
> View(mtcars)
> summary(mtcars) #컬럼단위로 최소값, 1/4분위값, 중앙값, 평균, 3/4분위값, 최대값등 기초 통계값을 리턴
      mpg             cyl             disp      
 Min.   :10.40   Min.   :4.000   Min.   : 71.1  
 1st Qu.:15.43   1st Qu.:4.000   1st Qu.:120.8  
 Median :19.20   Median :6.000   Median :196.3  
 Mean   :20.09   Mean   :6.188   Mean   :230.7  
 3rd Qu.:22.80   3rd Qu.:8.000   3rd Qu.:326.0  
 Max.   :33.90   Max.   :8.000   Max.   :472.0  
       hp             drat             wt       
 Min.   : 52.0   Min.   :2.760   Min.   :1.513  
 1st Qu.: 96.5   1st Qu.:3.080   1st Qu.:2.581  
 Median :123.0   Median :3.695   Median :3.325  
 Mean   :146.7   Mean   :3.597   Mean   :3.217  
 3rd Qu.:180.0   3rd Qu.:3.920   3rd Qu.:3.610  
 Max.   :335.0   Max.   :4.930   Max.   :5.424  
      qsec             vs               am        
 Min.   :14.50   Min.   :0.0000   Min.   :0.0000  
 1st Qu.:16.89   1st Qu.:0.0000   1st Qu.:0.0000  
 Median :17.71   Median :0.0000   Median :0.0000  
 Mean   :17.85   Mean   :0.4375   Mean   :0.4062  
 3rd Qu.:18.90   3rd Qu.:1.0000   3rd Qu.:1.0000  
 Max.   :22.90   Max.   :1.0000   Max.   :1.0000  
      gear            carb      
 Min.   :3.000   Min.   :1.000  
 1st Qu.:3.000   1st Qu.:2.000  
 Median :4.000   Median :2.000  
 Mean   :3.688   Mean   :2.812  
 3rd Qu.:4.000   3rd Qu.:4.000  
 Max.   :5.000   Max.   :8.000  
> summary(emp.data)
     emp_id    emp_name             salary     
 Min.   :1   Length:5           Min.   :515.2  
 1st Qu.:2   Class :character   1st Qu.:611.0  
 Median :3   Mode  :character   Median :623.3  
 Mean   :3                      Mean   :664.4  
 3rd Qu.:4                      3rd Qu.:729.0  
 Max.   :5                      Max.   :843.2  
   start_date        
 Min.   :2012-01-01  
 1st Qu.:2013-09-23  
 Median :2014-05-11  
 Mean   :2014-01-14  
 3rd Qu.:2014-11-15  
 Max.   :2015-03-27  
```







## stringr

#####################################
#문자열 처리와 관련된 패키지 stringr
#####################################



- 텍스트 자료나 SNS에서 가공 처리된 빅데이터를 처리하기 위해서는  필요한 문자열을 적절하게 자르고 , 교체하고 추출하는 작업을 수행할 수 있어야 합니다.


```R
> install.packages("stringr")
> library(stringr)
> #str_length()
> #str_c() , str_join()
> #str_sub(), str_split()
> #str_replace()
> #str_extract() 정규표현식을 사용하여 문자열 추출
> #str_extract_all() 정규표현식을 사용하여 문자열 추
> #str_locate() 특정 문자열 패턴의 첫번째 위치 찾기
> #str_locatet_all()
> #.....
> 
> fruits <- c('apple', 'banana', 'pineapple', 'berry', 'APPLE')
> #패턴을 포함한 요소에서 패턴 출현 회수 리턴
> print(str_count(fruits, "a"))  
[1] 1 3 1 0 0
> 
> #문자열 결합 기본 R 함수
> rs1<-paste('hello', '~R') 
> print(rs1)
[1] "hello ~R"
> 
> print(str_c('hello', '~R'))
[1] "hello~R"
> print(str_c(fruits, " name is ", fruits))
[1] "apple name is apple"        
[2] "banana name is banana"      
[3] "pineapple name is pineapple"
[4] "berry name is berry"        
[5] "APPLE name is APPLE"        
> print(str_c(fruits,  collapse=" "))
[1] "apple banana pineapple berry APPLE"
> print(str_c(fruits,  collapse="-"))
[1] "apple-banana-pineapple-berry-APPLE"


#dataset객체의 요소별로 'A'포함여부를 추적, 
print(str_detect(fruits, 'A')) 
#정규표현식의 형식문자^는 시작을 의미합니다.
print(str_detect(fruits, '^a')) 
#정규표현식의 형식문자$는 끝을 의미합니다.
print(str_detect(fruits, 'a$'))
print(str_detect(fruits, '^[aA]'))    
print(str_detect(fruits, '[^a]'))  #not의 의미

print(str_sub(fruits, start=1, end=3))  #부분 추출
print(str_sub(fruits, start=6, end=9))
print(str_sub(fruits, start=-5))

str_length("  apple   banana  ")  
str_length(str_trim("  apple   banana  "))  #앞뒤 공백 제거 trim() 함수

# dataset객체의 요소 문자열을 길이를 벡터로 리턴
print(str_length(fruits)) 
print(str_dup(fruits, 3))

print(str_replace(fruits, 'p', '**'))
print(str_replace_all(fruits, 'p', '**'))

fruits2 <- str_c(fruits, collapse="/")
print(fruits2)
str(fruits2)

result2<- str_split(fruits2, "/")
print(result2)
str(result2)

str_extract("홍길동35이순신45유관순25", "[1-9]{2}")
str_extract_all("홍길동35이순신45유관순25", "[1-9]{2}")
str_extract_all("honggil305koreaseoul1004you25jeju-hanlasan2005", "[a-z]{3, }")
str_extract_all("honggil305koreaseoul1004you25jeju-hanlasan2005", "[a-z]{3, 5}")

str1 <- "korea123456-1234567seoul"
#문) str1객체에 저장된 문자열로부터 주민번호만 추출
str_extract_all(str1, "[0-9]{6}-[1234][0-9]{6}")

str2 <- "홍길동1357,이순신,유관순1012"
#문) str2객체에 저장된 문자열로부터 7글자 이상의 단어만 추출
str_extract_all(str2, "\\w{7, }")

#str_to_upper()
#str_to_lower()


```





## 데이터 입출력



### scan() 

- 키보드로부터 데이터 입력 받기 위해 사용
- 입력할 데이터가 없으면 엔터키만 누르면 종료됨
- 문자열로 입력받으려면 what=character() 옵션 사용



```R
#키보드로 숫자 입력하기
num <- scan()
1: 1
2: 2
3: 3
4: 
Read 3 items

#합계
> sum(num)
[1] 6

#키보드 문자 입력하기
> name <- scan(what=character())
1: name
2: name
3: 
Read 2 items
> name
[1] "name" "name"

#edit() - 데이터 입력을 돕기 위해 표 형식의 데이터 편집기 제공
df = data.frame() #빈 데이터프레임 생성
df = edit(df) # 데이터 편집기
학번 이름 국어 영어 수학
1 홍길동 80 80 80
2 이순신 95 90 95
3 강감찬 95 95 100
4 유관순 85 85 85
5 김유신 95 90 95


print(df)

#파일 유형(text,  csv, xml, html, json, db, excel, bigdata저장소(hdfs, nosql) 읽어오기
#c:/workspaceR 디렉토리 아래 data디렉토리 생성 후 샘플 파일 
#다운로드 받아서 압축 풀어 파일들을 저장해주세요

> print(list.files(recursive = T));
 [1] "datafile-I/emp.csv"          
 [2] "datafile-I/emp.txt"          
 [3] "datafile-I/emp2.csv"         
 [4] "datafile-I/excel.csv"        
 [5] "datafile-I/finviz.csv"       
 [6] "datafile-I/stdf.csv"         
 [7] "datafile-I/stock.csv"        
 [8] "datafile-I/student.txt"      
 [9] "datafile-I/student1.txt"     
[10] "datafile-I/student2.txt"     
[11] "datafile-I/student3.txt"     
[12] "datafile-I/student4.txt"     
[13] "datafile-I/studentexcel.xlsx"
[14] "datafile-I/studentx.xlsx"    
[15] "datafile-I/test.csv"         
[16] "emp.csv"                     
[17] "emp.txt"                     
[18] "emp2.csv"                    
[19] "excel.csv"                   
[20] "finviz.csv"                  
[21] "stdf.csv"                    
[22] "stock.csv"                   
[23] "student.txt"                 
[24] "student1.txt"                
[25] "student2.txt"                
[26] "student3.txt"                
[27] "student4.txt"                
[28] "studentexcel.xlsx"           
[29] "studentx.xlsx"               
[30] "test.csv"                    
> print(list.files(all.files = T));
 [1] "."                 ".."               
 [3] ".RData"            ".Rhistory"        
 [5] "datafile-I"        "emp.csv"          
 [7] "emp.txt"           "emp2.csv"         
 [9] "excel.csv"         "finviz.csv"       
[11] "stdf.csv"          "stock.csv"        
[13] "student.txt"       "student1.txt"     
[15] "student2.txt"      "student3.txt"     
[17] "student4.txt"      "studentexcel.xlsx"
[19] "studentx.xlsx"     "test.csv"         


```





### read.csv()

#csv 형식의 data가 지정된 파일로부터 data를 읽어서 R실행 환경으로로딩

```R


data1 <- read.csv("./emp.csv")
> # data1 <- read.csv("c:/workspace/emp.csv")
> print(data1)
   no   name pay
1 101 홍길동 150
2 102 이순신 450
3 103 강감찬 500
4 104 유관순 350
5 105 김유신 400
> str(data1)  #data.frame객체로 리턴
'data.frame':	5 obs. of  3 variables:
 $ no  : int  101 102 103 104 105
 $ name: Factor w/ 5 levels "강감찬","김유신",..: 5 4 1 3 2
 $ pay : int  150 450 500 350 400
> 
> #사원 데이터에서 최대 급여를 출력
> max_sal <- max(data1$pay)
> print(max_sal)
[1] 500
> 
> #최대 급여를 받는 레코드(행)만 추출
> person1 <- subset(data1, pay == max(pay))
> print(person1)
   no   name pay
3 103 강감찬 500


#문) emp3.csv파일의 데이터를 data.frame객체에 저장한 후에
IT부서에서 급여가 600이상인 사원 추출
 person2 <- subset(data2, dept=="IT" & salary >= 600 )
> print(person2)
  id     name salary  startdate dept
1  1     Rick  623.3 2012-01-01   IT
3  3 Michelle  611.0 2014-11-15   IT

##문) emp3.csv파일의 데이터를 data.frame객체에 저장한 후에
입사날자가 2014년 7월 01일 이후인 사원추출
b<-as.Date("2014-07-01")
date <- subset(data2, as.Date(startdate) > b )
> date
  id     name salary  startdate    dept
3  3 Michelle 611.00 2014-11-15      IT
4  4     Ryan 729.00 2014-11-05      HR
5  5     Gary 843.25 2015-03-27 Finance


```





### read.xlsx() 

################################################################
read.xlsx() 엑셀 파일로부터 데이터 읽기
xlsx 패키지가 필요하면 의존하고 있는 rJava패키지를 먼저 로드해야 합니다.
sheetIndex=1은 선택한 엑셀 파일에서 첫 번째 시트 탭을 지정
################################################################



```R
install.packages("xlsx")   # xlsx 패키지 설치 
install.packages("rJava")   # rJava 패키지 설치 

#Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_151')

library(rJava) # 로딩
library(xlsx) # 로딩

studentex <- read.xlsx(file.choose(), 
                       sheetIndex=1, encoding="UTF-8")
studentex

itperson <- subset(data1, dept=="IT")
print(itperson)
write.xlsx(itperson,  "./output/itperson.xlsx", sheetName="IT", 
           col.names=FALSE, row.names=FALSE)
list.files("./output/")
newdata <- read.xlsx("./output/itperson.xlsx", sheetIndex=1)
print(newdata)
```





### readLines(), read.table()

```R
################################################
텍스트파일 읽기 readLines(), read.table()
################################################
#아래 내용을 메모장에 작성해서 작업디렉토리의 data디렉토리 아래 fruits.txt로 저장하세요
no  name  price   qty  
1   apple   500     5  
2   banana  200     2  
3   peach   200     7  
4   berry    50     9  

# 텍스트 파일 읽기, 라인 단위를 문자열로 로딩, 라인단위로 저장되는 벡터 객체로 생성함
file1 <- readLines("./data/fruits.txt")  
print(file1)
str(file1)

#텍스트 파일의 내용을 읽어서 data.frame객체로 생성함
fruits1 <- read.table("./data/fruits.txt" ) 
print(fruits1)
str(fruits1)

fruits1 <- read.table("./data/fruits.txt", header=T)
print(fruits1)
str(fruits1) 

fruits1 <- read.table("./data/fruits.txt", header=T, stringsAsFactor=FALSE)
print(fruits1)
str(fruits1)
```

