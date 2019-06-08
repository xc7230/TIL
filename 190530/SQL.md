# Database





## Database 특징

**통합된 데이터** - 데이터의 중복을 최소화하여 중복으로 인한 데이터 불일치 현상을 제거합니다.

**저장된 데이터** - 디스크, 테이프 같은 컴퓨터 저장장치에 저장된 데이터

**운영 데이터** - 업무를 위한 검색을 할 목적으로 저장된 데이터

**공용 데이터** - 동시공유

**실시간 접근성**

**지속적인 변화**

**내용에 따른 참조**



## 파일 시스템

데이터를 파일 단위로 저장하므로 중복 가능

데이터의 중복 저장으로 일관성이 결여됨

데이터 정의와 프로그램의 독립성 유지 불가능

관리 기능 보통

프로그램 개발 생산성 나쁨



## DBMS 장점

DBMS를 이용하여 데이터를 공유하기 때문에 중복 가능성이 낮음

중복 제거로 데이터의 일관성이 유지됨

데이터 정의와 프로그램의 독립성 유지 가능

데이터 복구, 보안, 동시성 제어, 데이터 관리 기능 등을 수행



# SQL

DML - DQL검색  Select~

​			추가 Insert~

​			수정 Update~

​			삭제 Delete~

# DDL 

생성 Create~

변경 Alter~

삭제 Drop ~



# 구조 - Table

View

Index

sequence



# DCL

DBMS 보안

1.인증

2.권한 - Grant~ revoke~



# Tx - Unit of Work(원자성)



이체 > A (update)> 10000원 > B(update)

쇼핑 > 1.결제(Insert)  2.제품수량변경 3.배송정보추가 4.고객 histroy ------영속성 commit; rollback **TCL**



# lsnrctl status

리스너의 상태



# number타입 컬럼은 산술연산

char/varchar2 타입 컬럼은 문자열 결함 : ||

date 타입 컬럼 : date+n, date-n, date-date, date +-1/n

```sql
 select sal+100, sal-100, sal*2,sal/100
```





# SQL단점

**조건처리** : 함수

**반복처리** > **table의 형단위 반복처리** 

명시적 for문x while문 x exception처리 x 변수사용 x



# 함수

predfine > DB 벤더 nvl, sysdate,user

custom(PL/SQL)



단일행 함수 >intput> 함수처리>outputdata>>

복수행 함수(그륩함수)

분석함수(Window함수)



## *문자, 날짜 데이터는 반드시 ' '를 사용해서 표현, 처리

## *날짜 데이터 세션에 설정된 포맷 형식하고 일치해야 합니다.(RR/MM/DD)

```sql
select ename||job

from emp;



select ename|| ' works as '   ||job

from emp;
```







### Quiz> 'A' 결과로 출력하려면?

```sql
select  '''A'''

from dual;

select  q'['A']''

from dual;
```







### Quiz> select 10||10 from dual;

```sql
select 10||10 from dual;
select '10'+'10' from dual;--숫자인경우 문자열 10을 정수로 자동 형변환합니다.
10
20
```



## *select~ from 절이 필수절입니다.

## *단순계산 결과, 함수 결과, 문자 데이터 출력등은 dual 테이블을 사용합니다.

```sql
desc dual

select * from dual;

select sysdate+1, sysdate-1 from dual; --날짜와 산술연산하는 정수는 Number of Days입니다.



select sysdate - hiredate from emp; --기간이 리턴



select sysdate _ hiredate from emp;  --error



alter session set nls_date_format = 'YYYY-MM-DD HH24:MI:SS';

select sysdate, sysdate +1/24, sysdate+5/1440 from dual;


```









조건 검색 :

문> 부서 번호 30번인 사원 검색

select ename, deptno from emp

where deptno = 30;

문>직무가 ANALYST인 사원 검색

select ename, job from emp

where job = 'ANALYST'

문>급여가 3000이상인 사원 검색

select ename, sal from emp

where sal>=3000



alter session set nls_date_format = 'RR/MM/DD';





select empno, ename,hiredate from emp

where hiredate >= '87/01/01';



문>커미션을 받지 않는 사원을 검색하시오

select empno, comm

where comm>= null; --error



*is null, is not null 연산자 : null 비교 연산자

select ename, comm from emp

where comm is null;

논리연산자 and,or, not



문> 월급이 3000이상 5000 이하인 사원 검색 (3000포함, 5000포함)

select ename, sal from emp

where sal >=3000 and sal <=5000;



*범위 연산자 between 하한값 and 상한값

select ename, sal from emp

where sal between  3000 and 5000;



문> 직무가 clerk 또는 analyst 인 사원 검색

select ename, job from emp

where job = 'CLERK' or job = 'ANALYST';

*in 리스트 연산자 : in(값,값,값,.......)

select ename, job from emp

where job in('CLERK' ,'ANALYST');



*character pattern matching 연산자 : like '%,_'

문> 사원이름중에서 두번째 문자가 'D' 인 사원 검색

select ename from emp

where ename like '_D%';



문> 사원이름중에서 첫번째 문자가 'S' 인 사원 검색

select ename from emp

where ename like 'S%';

문> 사원이름중에서 문자가 'S' 인 사원 검색

select ename from emp

where ename like '%N';



문> 81년도에 입사한 사원 검색

select ename, hiredate from emp

where hiredate like '81%';



--논리연산자의 우선순위 NOT, AND, OR

문>업무가 PRESIDENT 이고 금여가 1500이상이거나 업무가 SALESMAN인 사원의

사원번호, 이름, 업무, 급여를 출력하여라.

select empno, ename, job, sal from emp

where (job = 'PRESIDENT ' and sal >= 1500)  or job = 'SALESMAN'



### 문>급여가 급여가 1500이상이거나 업무가 SALESMAN이거나 PRESIDENT 사원의 사원번호, 이름, 업무, 급여를 출력하여라.

```sql
select empno, ename, job, sal from emp

where sal  >= 1500 and job  in ('PRESIDENT', 'SALESMAN')
```





select ~
from ~

[where 필터 조건]

[group by 컬럼]

[having 조건]

[order by 정렬기준커럼 정렬방식] - asc 오름차순 default, desc 내림차순



### 문> 월급의 오름차순으로 사원 정보 출력

```sql
select ename, job, sal from emp

order by sal ;



select ename, job, sal from emp

order by sal  desc;
```





### 



### 문> 사원들의 사번, 이름, 부서번호, 월급,커미션, 연봉(sal+comm*12) 의 결과 출력

### ,연봉의 내림차순으로

```sql
select empno, ename,  deptno, sal , comm,(sal+nvl(comm, 0 ))*12 "연봉"  from emp

order by "연봉"  desc;



select empno, ename,  deptno, sal , comm,(sal+nvl(comm, 0 ))*12 "연봉"  from emp

order by  6 desc;



select empno, ename,  deptno, sal , comm,(sal+nvl(comm, 0 ))*12 "연봉"  from emp

order by  3asc, "연봉" desc;


```







**문제1)  EMP Table의 모든 자료를 출력하여라.**

--empno:사원번호 , ename:사원이름, sal:급여, job:담당업무, comm:급여보너스



```sql
select * from emp; -- *은 전체
```



**문제2)  EMP Table에서 사원 번호, 이름, 급여, 담당업무를 출력하여라.**

```sql
select empno,ename,sal,job from emp; --empno:사원번호 , ename:사원이름, sal:급여, job:담당업무

```

**문제3) 모든 사원의 급여를 $300 증가시키기 위해 덧셈 연산자를 사용하고 결과에 SAL+300을 조회한다**

```spl
select ename,sal+300 from emp;
```



**문제4) EMP 테이블에서 사원번호, 이름, 급여보너스를 출력하여라.**

```spl
select empno,ename,comm from emp;
```



**문제5) EMP 테이블에서 ENAME를 NAME로 SAL을 SALARY로 출력하여라.**

```sql
select ename"NAME",sal"SALARY" from emp;
```



**문제6) EMP 테이블에서 ENAME를 Name로 SAL*12를 Annual Salary 로 출력하여라.**

```sql
select ename"NAME",(sal*12)"Annual SALARY" from emp;
```



**문제7) EMP 테이블에서 ENAME를 '성 명'으로, SAL를 ‘급 여'로  출력하여라.**

```sql
select ename"성 명",sal"급 여" from emp;
```



**문제8) EMP 테이블에서 이름과 업무를 연결하여 출력하여라.**

```sql
select ename || job from emp;--||은 테이블 연결해줍니다.
```



**문제9) EMP 테이블에서 이름과 업무를 "King is a PRESIDENT" 형식으로 출력하여라.**

```sql
select (ename || job)"King is a PRESIDENT" from emp;
```



**문제10) EMP 테이블에서 이름과 연봉을 "KING: 1 Year salary = 60000"** 

```sql
select ename, (sal*12)"1 Year salary" from emp;
```



**문제11) EMP 테이블에서 JOB을 모두 출력하여라.**

```spl
select job from emp;
```



**문제12) EMP 테이블에서 담당하고 있는 업무의 종류를 출력하여라.**

```sql
select job from emp;
```





**문제13) EMP 테이블이 부서번호를 중복 값을 제거해서 조회하라**

```sql
select distinct deptno from emp; --distinct 중복값 한번만 출력
```



**문제14) 부서별로 담당하는 업무를 한번씩 출력하여라.**

```sql
select distinct job from emp;
```



**문제15) EMP 테이블에서 사원번호, 이름, rowid를 조회하라.**

```sql
select empno, ename, rowid from emp;
```



**문제17) EMP 테이블에서 급여가 3000 이상인 사원의 사원번호, 이름, 담당업무, 급여를 출력하라.**

```sql
select empno,ename, job, sal from emp where sal>=3000 --where sal>=3000 = 3000이상인 사람만 출력
```



**문제18) EMP 테이블에서 담당업무가 Manager인 사원의 정보를 사원정보, 성명, 담당업무, 급여, 부서번호를 출력하라.**

```sql
select empno,ename, job, sal, deptno from emp where job="MANAGER";
```



**문제19) EMP 테이블에서 1982년 1월 1일 이후에 입사한 사원의 사원번호, 성명, 담당업무, 급여, 입사일자, 부서번호를 출력하라.**

```sql
select empno,ename, job, sal,hiredate, deptno from emp where hiredate >('1982/1/1')
```



**문제20) EMP 테이블에서 급여가 1300에서 1700사이의 사원의 성명, 담당업무, 급여, 부서 번호를 출력하여라.**

```sql
select ename, job, sal  from emp where sal >1300 and sal <1700;
```



**문제21) EMP 테이블에서 사원업호가 7902, 7788, 7566인 사원의 사원번호, 성명, 담당업무, 급여, 입사일자를 출력하여라.**

```sql
select empno, ename, job, sal, hiredate  from emp where empno in(7902, 7788, 7566);
```



**문제22) EMP 테이블에서 입사일자가 82년도에 입사한 사원의 사번, 성명, 당당업무, 급여, 입사일자, 부서번호를 출력하여라.**

```sql
select empno, ename, job, sal,hiredate,deptno from emp where hiredate like '82%';  --%은 82에  해당하는 모든자료를 불러온다.
```



**문제23) EMP 테이블 이름의 첫 글자가 'M'인 사원의 이름, 급여 조회하라**

```sql
select ename, sal from emp where ename like 'M%';
```



**문제24) EMP 테이블 이름의  두 번째 글자가 ‘L'인 사원의 이름,업무를  조회하라**

```sql
select ename, job from emp where ename like '_L%'; --두번째를 고르고 싶으면 _ 를 앞에 붙여준다.
```



**문제25) EMP 테이블에서 보너스가 NULL인 사원의 사원번호, 성명, 담당업무, 급여, 입사일자, 부서번호를 출력하여라.**

```spl
select empno, ename, job, sal, hiredate, deptno from emp where comm like 'null';
```





**문제26) EMP 테이블에서 급여가 1100 이상이고 JOB이 Manager인 사원의 사원번호, 성명, 담당업무, 급여, 입사일자, 부서번호를 출력하여라.**

```sql
select empno, ename, job, sal, hiredate, deptno from emp where sal>=1100 and job like 'MANAGER';
```







```sql
select initcap(ename), lower(ename), upper(ename) from emp;



select length('Korea'), length('대한민국') from dual;



select lengthb('Korea'), lengthb('대한민국') from dual;



--함수 안에 함수를 nested 하면 nested 된 함수부터 처리

select concat(concat(ename, ' is '), job) from emp;


```







```sql
select substr('today is 2015년 4월 26일', 1, 5),
       substr('today is 2015년 4월 26일', 10, 5),
       substr('today is 2015년 4월 26일', 15),
       substr('today is 2015년 4월 26일', -3, 2)
from dual;

select instr('korea is wonderful', 'o'),
       instr('korea is wonderful', 'o', 1, 2),
       instr('korea is wonderful', 'o', 9),
       instr('korea is wonderful', 'x')
from dual;
```



**lpad : left padding,**  
**rpad : right padding**
문자열로 변환, 문자열 전체 길이내에 왼쪽 공백에 특정 문자를 padding

```sql
select ename, sal, lpad(sal, 10, '*')
from emp;

select ename, sal, rpad(sal, 10, '*')
from emp;
```





**trim, ltrim, rtrim 함수**

```sql
select length('  hello  '),  length(trim('  hello  '))
from dual; --trim:빈공간을 없애준다.

select trim('H' from 'Hello wonderful'), trim('l' from 'Hello wonderful')
from dual;--'H'를 없애준다.

select ltrim('Hello wonderful', 'He' ), rtrim( 'Hello wonderful' , 'ful')
from dual;

select replace('Jack AND Jue', 'J', 'BL')
from dual;--'J'를 'BL'로 바꿈


```

**translate**

#########################number function########################



```sql
select round(12.345, 2), round(12.345, 0), round(12.345, -1)
from dual;-- round : 소수점 자리수 반올림

select trunc(12.345, 2), trunc(12.345), trunc(12.345, -1)
from dual;--trunc :  소수점 자리수 버림

select mod (99, 4)
from dual; --mod  : 나머지

select ceil(12.345), floor(12.345) from dual;
--ceil: 가까운 정수 올림 floor: 가까운 정수 내림
select power(3, 2), power(5, 2)
from dual;--power 3^2
```



문> 사원 번호중 홀수 인 사원들만 출력





**where절에 함수 사용 가능**

#########################date function########################

```sql
timestamp컬럼 타입 (YYYY/MM/DD HH24:MI:SS.SSSSSSSSS)
timestamp(3)  #6이 default
timestamp with time zone

select sessiontimezone from dual;  --sessiontimezone 살고있는 국가시간
alter session set time_zone = '+3:00';
select sessiontimezone from dual;

--sysdate 시스템의 현재 리턴
--current_date 세션의 timezone기반 현재시간을 date 타입으로 리턴
--current_timestamp 세션의 timezone기반 현재시간을 timezone타입으로 리턴


```

#add_months(date, n) - 개월 수를 더한 날짜가 리턴
#months_between(date, date) - 기간이 리턴



```sql
select add_months(sysdate, 6)
from dual;

select hiredate, add_months(hiredate, 6)  --add_months(날짜,숫자) 날짜(월)에 숫자를 더해준다.
from emp;

select months_between(sysdate, hiredate)  --months_between 두 날짜 사이의 월 수를 계산합니다.
from emp;

--next_day(date.'요일명')  --next_day 지정한 날짜 이후 지정한 요일이 처음 나오는 날짜를 뽑아준다.

select next_day(sysdate,'목')
from emp;

alter session set nls_date_format = 'RR/MM/DD';

--trunc, round
select trunc(to_date('14/02/14'), 'MONTH'),  --TRUNC은 주로 값을 없앨때 사용합니다. 14.02.14중 Month의 값밑으로 버림
trunc(to_date('14/02/14'), 'YEAR') --TRUNC은 주로 값을 없앨때 사용합니다. 14.02.14중 Year의 값밑으로 버림 
from dual;

select round(to_date('14/02/14'), 'MONTH'),  --round은 주로 값을 없앨때 사용합니다. 14/06/20중 Month의 밑의 값을 반올림 14.07.01
round(to_date('14/02/14'), 'YEAR')  --round은 주로 값을 없앨때 사용합니다. 14/08/14중 Year의 밑의 값을 반올림 15.01.01
from dual;

--last_day(date)

last_day(date)
select last_day(to_date('14/02/14')),  last_day(to_date('2000/02/14')), last_day(to_date('2100/02/14')) --last_day는 해당하는 날짜의 마지막 일을 알려줍니다.
from dual;



```



**문> 사원들의 입사 날짜로부터 6개월후날짜로부터 다음 금요일이 연봉 조정 면담날짜입니다.**

**사원들의 사번과 입사날짜와 연봉 조정 면담날짜 출력하세요.**

```sql
select empno, hiredate, next_day(add_months(hiredate, 6),'금')
from emp;  --next_day 지정한 날짜 이후 지정한 요일이 처음 나오는 날짜를 뽑아준다.
```



```sql
select to_char(123456.789, '$9,999,999.9999')  --To_char(숫자 or 날짜, format) 숫자나 날짜를 format형식으로 변환해준다.
from dual;
select to_number($1,234,567,999, '9,999,999.9999')
from dual; --error
select to_number($1,234,567,999, '$99,999,999.9999')
from dual;

select sysdate, to_char(sysdate, 'YYYY"년" MM"월" DD"일" DY')
from dual;

alter session set nla_language = american;

select sysdate, to_char(sysdate, 'Year Month DDspth Day')
from dual; --미국식 날짜로 출력

alter session set nls_language = korean;
select '2019-05-30 5:43PM'
,to_date('2019-05-30 5:43PM', 'HH12:MI AM YYYY-MM-DD') from dual;

select '2019-05-30 5:43PM'
,to_date('2019-05-30 5:43', 'YYYY-MM-DD HH12:MI') from dual;
```



