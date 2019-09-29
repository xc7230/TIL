# 스터디 1일차



## t - test

### 예제(단일 표본)

#### 1.데이터 생성

``` R
data <- c(35,40,12,15,21,14,46,10,28,48,16,30,32,48,31,22,12,39,19,25)
```





#### 2.정규성 검정

- 샤피로 윌크 검정 : 표본수가 2000개 미만인 데이터셋에 적합한 정규성 검정
- H0 : 주어진 데이터의 분포는 정규분포를 따른다.
  H1 : 주어진 데이터의 분포는 정규분포를 따르지 않는다.



```R
shapiro.test(data)

######결과#######
Shapiro-Wilk normality test

data:  data
W = 0.93351, p-value = 0.1803

#0.1803으로 데이터가 정규분포를 따른다고 할 수 있다.
#따라서 t-test를 할 수 있다.

```



#### 3.양측검정

- mu: 비교하는 대상의 평균
- alternative : 검정방법
  - two.sided(양측검정)
  - greater(우측검정 : 모평균보다 크다)
  - less(좌측검정 : 모평균보다 작다.)



- H0 : 두 평균은 서로 같다.

  H1 : 두 평균은 서로 다르다.

```R
t.test(data, mu = 25, alternative = 'two.sided')

######결과#######
One Sample t-test

data:  data
t = 0.76872, df = 19, p-value =
0.4515
alternative hypothesis: true mean is not equal to 25
95 percent confidence interval:
 21.29608 33.00392
sample estimates:
mean of x 
    27.15 

#p-value는 0.4515로 귀무가설을 채택, 두 평균은 서로 같다고 할 수 있다.
#신뢰구간을 보면 21.29608 33.00392 사이로 비교하려는 평균(25)가 구간안에 있는것을 확인 할 수 있다.
#따라서 분산의 평균(27.15)와 비교하려는 평균(25)의 차이 2.15는 단순 우연한 차이라고 할 수 있다.
```





### 예제(대응 표본)

#### 1.데이터생성

```R
data0<- c(74, 75, 75, 77, 79, 76, 77, 78, 81 ,82) 
data1<-c(70, 71, 73, 73, 75, 76, 76, 77, 78, 80)


```





#### 2.정규성검정

```R
shapiro.test(data0)

######결과#######
	Shapiro-Wilk normality test

data:  data0
W = 0.94191, p-value = 0.5745

shapiro.test(data1)

######결과#######
	Shapiro-Wilk normality test

data:  data1
W = 0.9741, p-value = 0.9261

```



#### 3.우측검정



- H0 : data0=data1

  H1: data0>data1

```R
#대응비교시, paired = T를 넣어준다.

t.test(data0,data1, paired=T,alternative="greater", var.equal = TRUE)




######결과#######
	Paired t-test

data:  data0 and data1
t = 5.2382, df = 9, p-value =
0.000268
alternative hypothesis: true difference in means is greater than 0
95 percent confidence interval:
 1.625127      Inf
sample estimates:
mean of the differences 
                    2.5 

#p-value는 0.000268 대립가설 채택 data0의 평균이 크다고 할 수 있다.


```





## Wilcoxon rank sum test

### 예제(윌콕스 순위합 검정)



- 자료가 어떤 분포를 따르는지 가정하지 않고 자료 값들의 순위를 이용하여 두 그룹 간에 차이가 있는지 알아본다.



- A와 B 두 그룹간에 수술 결과 기능성 호전 정도(score)에 차이가 있는지 검정해 보자.

#### 1.데이터생성

```R
group <- c("A", "A", "A", "A", "A", "A", "A", "B", "B","B", "B", "B", "B", "B")
score <- c(1, 2, 3, 6, 40, 10, 25, 5, 8, 48, 9, 67, 10, 57)
data <- data.frame(group, score)

```



#### 2.정규성검정

```R
tapply(data$score, data$group, shapiro.test)



######결과#######

$A #group A의 정규성검정

	Shapiro-Wilk normality test

data:  X[[i]]
W = 0.80436, p-value = 0.04523 


$B #group B의 정규성검정

	Shapiro-Wilk normality test

data:  X[[i]]
W = 0.79672, p-value = 0.03801

#두 그륩은 정규분포를 따른다고 볼 수 없다.

```



#### 3.윌콕스 검정

- H0 : 두 그륩의 수술결과는 서로 같다.
- H1 : 두 그륩의 수술결과는 서로 다르다.

```R
wilcox.test(data$score~ data$group, exact = T)


######결과#######

wilcox.test(data$score~ data$group, exact = F)

Wilcoxon rank sum test with
	continuity correction

data:  data$score by data$group
W = 12.5, p-value = 0.1413
alternative hypothesis: true location shift is not equal to 0

#p-value는 0.1413 귀무가설 채택 두 그륩의 수술 결과는 서로 같다고 할 수 있다.
```

