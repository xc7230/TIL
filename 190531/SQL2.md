1. 제어판>관리도구>서비스 (services.msc)에러 Oralce~ 서비스 시작되어 있는 것 모두 중시시킴
2. 레지스트리에서 Oracle관련 정보 삭제
   - Window실행에서 regedit입력
   - HKEY_LOCAL_MACHINE > SOFTWARE > Oracle 디렉토리 삭제
   - HKEY_LOCAL_MACHINE > System > CurrentControlSet > services > Oracle 디렉토리들 삭제
   - HKEY_LOCAL_MACHINE > System > CurrentControlSet > services > eventlog > Application Oracle 디렉토리들 삭제
3. 탐색기 C:\Program Files 아래 Oracle 디렉토리 삭제
4. 윈도우 프로그램 메뉴 Oracle 메뉴 디렉토리 삭제
5. C:\app\사용자명폴더~~~~~~ 에 오라클 관련 파일들이 있습니다.
   C:\app 디렉토리 삭제합니다. 만약 xxx.dll파일 때문에 삭제가 안되면 reboot 해서 삭제합니다.



=======================기타 단일행 함수(null처리, 조건 처리)=========================

# Database

**Database**에는 2가지 유형(Business 또는 User, Meta Data)의 데이터가 저장됩니다.

**DBMS** 

계층형 - 망형 - 관계형 - 객체관계형 - 클러스터로 구성

**Table** - Column(속성) + Row(Record)

**Primary Key** - Not NULL + Unique

**Foreign Key** - 참조관계 (parnent 테이블의 PK를 참조하는 child 테이블의 외래키)

**null** - 아직 값이 할당되지 않음을 의미, 0 아니며, " "와 다르며

​          산술연산 결과는 null, 비교연산(=, !=, >)  결과는 null

​          nvl(컬럼, null일때 리턴할 값) 함수를 사용해서 변환 후 처리합니다.

SQL - 선언적 언어, 결과 기술 

**DML**  ( DML : Data Manipulation Language )  : 데이터 조작 언어, 테이블에 데이터 검색, 삽입, 수정, 삭제하는데 사용합니다.

**select** 검색

**update** 수정

**insert** 삽입

**delete** 삭제



**DDL** ( DDL : Data Definition Language ) : 데이터 정의 언어, 테이블이나 관계의 구조를 생성하는데 사용합니다.



**create** 새로운 데이터 관계 (테이블),View, 인덱스, 저장프로시저 만들기

**alter** 이미 존재하는 데이터베이스 개체에 대한 변경, RENAM의 역할을 한다.

**drop** 이미 존재하는 데이터 관계 (테이블),View, 인덱스, 저장프로시저를 삭제한다.

**truncate** 관계(테이블)에서 데이터를 제거한다. (한번삭제하면 돌이킬 수 없다)

**comment** 생성된 객체의 코멘트를 달아준다.





**DCL**( DCL : Data Control Language) : 데이터 제어 언어, 데이터의 사용 권한을 관리하는 데 사용

**grant** 특정 데이터베이스 사용자에게 특정 작업에 대한 수행 권한을 부여한다.

**revoke** 특정 데이터베이스 사용자에세 특정 작업에 대한 수행 권한을 박탈 or 회수 한다.



**TCL**  (TCL : Transaction Control Language): 트랜잭션 제어언어  DML문이 실행되어 DBMS에 저장되거나 되돌리기 위해 실행해야 하는 SQL 

**commit**   SQL 문의 결과를 영구적으로 DB에 반영하는 SQL문. 데이터 변경 후 확정 사용한다.

**roolback**  SQL문의 결과를 취소하는 SQL문. 데이터 변경 후 되돌릴때 사용한다.

**savepoint** 트랜잭션의 한 지점에 표시하는 임시 저장점. 해당 savepoint로 이동한다.



검색 구문

select * | [distinct] column,..... | expression [as] Alias

from 테이블명

[where 조건]

...

[order by 정렬기준컬럼 asc|desc]

테이블 구조 확인 - desc, describe

#### 컬럼타입:

**char(size)**  

**varchar2(size)**

**number(p, s)**

**date**

**timestemp**

**timestemp with timezone**

**interval year to timezone**

**interval year to month**

**interval day to second**

**rowid**

#### 컬럼타입에 따른 연산 : 

**number** - 산술연산

**char/varchar2** - || 결합연산자

**date** - +-n, +-1/24, date - date

#### where 절 연산자 :

**in** - 여러 값의 리스트에서 값들을  =, or

**like** - 문자로 패턴 비교, _ , % 만능문자와 함께 사용합니다.

**bettween ~ and ~** - 범위 연산자, 하한값, 상환값을 포함해서 범위 비교

is null, is not null - null비교

=, >, <=, >=, != ,<>



조건이 여러개 이면 논리 연산자로(not, and, or) 결합합니다.

order by 컬럼;

order by 표현식;

order by 별칭;

order by column position;





함수 - 반드시 하나의 값을 리턴한다.



단일행함수 - character, number, date, conversion

복수행함수

분석(Window)함수



=======================기타 단일행 함수(null처리, 조건 처리)=========================

**nvl(column, expression)** 해당 컬럼에 null 상태가 있을시 명시된 값으로 바꿔주는 역활

**nvl2(column, expression1, expression2)** : expression1과  expression2이 동일한 타입이어야 한다. 정의되어 있는 값이 null이 아니면 값1, null이면 값2

**coalesce(column, expression1, expression2, ....)** : 해당 컬럼들 중에서 null이 아닌 첫 번째 값을 반환하는 함수





**nullif(expression1, expression2)** : expression1과 expression2 동일한  타입이어야 합니다. expression1값과 expression2 값이 동일하면 NULL을 그렇지 않으면 exp1을 반환





문> 사원들중 커미션을 받지 않는 사원들은 -1로 출력합니다. (이름, 급여, 커미션)

```sql
select ename, sal, nvl(comm, -1) from emp;
```

문> 사원들중 커미션을 받는 사원은 급여+커미션을 출력하고, 커미션을 받지 않는 사원은 'No Commission'으로 출력합니다. (이름, 급여, 커미션, 비고)

```sql
select ename, sal, comm, nvl2(comm, to_char(sal+comm), 'No Commission') "비고" from emp;
```



**조건처리 함수** : **decode**함수, 표현식1, 리턴값1, 표현식2, 리턴값2,.......
조건처리 표현식 , 표준 sql3 : case [표현식] when [값|조건표현식] then 값 [else 값] end

문> 사원들의 부서번호가 10번이면 월급을 5%인상
    부서번호가 20번이면 월급을 10%인상
    부서번호가 30번이면 월급을 3%인상 
    그 외의 부서는 월급 100인상합니다.
    현재의 월급과 인상된 월급을 출력합니다.

```sql
select ename, deptno, sal,
decode(deptno , 10 , sal*1.05
      		  , 20 , sal*1.1
       		  , 30 , sal*1.03 , sal+100)"Increase" 
       		  from emp;
              
select ename, deptno, sal,
case deptno when 10 then sal*1.05
            when 20 then sal*1.1
            when 30 then sal*1.03 
            else sal+100 end"Increase" 
            from emp;
```



문> 월급에 대한 세금 출력하시오
    월급이 1000미만이면 0,  
    2000미만이면 월급의 5%, 
    3000미만이면 월급의10%
    4000미만이면 월급의15%, 
    4000이상이면 월급의 20%



```sql
select ename,  sal , 
decode(trunc(sal/1000) , 0 , 0
       ,1
       ,2,sal * 0.1
       ,3,sal * 0.15
       ,sal * 0.2)"Tax"
       from emp;
       
select ename,  sal , 
case --뒤에 조건문을 넣을 수 있다.
       when sal < 2000 then sal * 0.05
       when sal  < 3000 then sal * 0.1
       when sal < 4000 then sal * 0.15
       when sal >= 4000 then  sal * 0.2
       else sal*0
       end"Tax"
       from emp;       
```





그룹함수

그룹핑된 행 집합, 테이블의 전체 행 집합의 컬럼이 함수의 인수로 전달되고

결과는 반드시 1개 리턴

sum(number타입|experession)

avg(number타입|experession)

min(number, char, date 컬럼타입 | expression)

max(number, char, date 컬럼타입 | expression)

count([distince]number, char, date 컬럼타임 | expression) : nu

stddev(number타입|experession) : 표준편차

variance(number타입|experession) : 분산



conn scott/oracle

문> 전체 사원의 급여 합계, 평균, 최대값, 최소값, 결과 출력

```sql
select sum(sal),avg(sal),max(sal),min(sal)
from emp;
```

문>전체 emp테이블 행수는?

```sql
select count(*), count(empno) from emp;
```



문>전체 사원들 중에서 가장 빠른 입사 날짜와 가장 최근 입사 날짜는?

```sql
select min(hiredate), max(hiredate) from emp;

```



문>전체 사원들중에 이름순서가 가장 빠른 사원의 이름과 이름순서가 가장 느린사람

```sql
select min(ename), max(ename) from emp;
```

문>사원들이 소속된 부서의 종류의 수 출력

```sql
select count(distinct deptno) from emp;
```

문>커미션을 받는 사원수는?

```sql
select count(comm) from emp;


--커미션을 받는 커미션의 평균
select avg (nvl(comm,0) from emp;
            
select sum(comm)/count(*) from emp;
```

문> 부서번호와 부서의 평균급여를 함께 출력

```sql
select deptno, avg(sal) from emp; --error

select deptno, avg(sal) from emp group by deptno;
 --그룹함수를 적용한 컬럼과 그룹함수를 적용하지 않은 컬럼이 select절에 
 --함께 선언될 경우 반드기 그룹함수를 적용하지 않은 컬럼은 group절에 선언해야합니다.
 
 
 --group by 절에 선언한 컬럼이 select절에 반드시 선언은 선택적입니다.
select avg(sal) from emp group by deptno;

--group by절에는 column명만 선언할 수 있습니다.
```

문> 부서와 직무별 급여 평균 출력

```sql
select deptno,job, avg(sal) from emp group by deptno, job;
```

문>각 부서별로 인원수, 급여의 평균, 최저 급여, 최고 급여, 급여의 합을 
구하여  급여의 합이 많은 순으로 출력하여라.

```sql
select deptno, count(ename), avg(sal), min(sal), max(sal), sum(sal) from emp  group by deptno
order by sum(sal) desc;
```





문> EMP 테이블에서 부서 인원이 4명보다 많은 부서의 부서번호, 인원수, 
급여의 합을 출력하여라

```sql
select deptno, count(*), sum(sal) --4
from emp  --1
group by deptno; --2
having count(*) --3
--그룹함수의 조건은 having절에 선언합니다. having절은 group by절과 함께쓰인다.
```



문> EMP 테이블에서 급여가 최대 2900 이상인 부서에 대해서 부서번호, 평균 급여, 
급여의 합을 구하여 출력하여라.

```sql
select deptno, avg(sal), sum(sal) 
from emp
group by deptno
having max(sal)>=2900;

```











문> EMP 테이블에서 업무별 급여의 평균이 3000 이상인 업무에 대해서 업무면, 
평균 급여, 급여의 합을 구하여 출력하여라.

```sql
select deptno, avg(sal), sum(sal) 
from emp
group by deptno
having avg(sal)>=3000;
```

문>전체 사원수, 1995, 1996, 1997, 1998년도에 입사한 사원수를 출력하시오
컬럼 타이틀은 total,  1995, 1996, 1997, 1998 로 출력하시오.

```sql
select count(*)"Total",
  sum(decode(to_char(hire_date,'YYYY'),'1995',1)) "1995",
  count(case to_char(hire_date,'YYYY') when '1996' then 1 end)"1996",
  count(case to_char(hire_date,'YYYY') when '1997' then 1 end)"1997",
   count(case to_char(hire_date,'YYYY') when '1998' then 1 end)"1998"
  from employees;
```

문> 사원이름, 부서번호, 부서이름

```sql
select last_name, department_id, department_name
from employees, departments;
```





## Join

```sql

검색방법 :
Projection
selection
join


employees, emp - 사원정보
departments, dept - 부서정보

ex) 사원이름, 부서번호, 부서이름

oracle join syntax - where절에 조인조건 선언
sql1999 표준 syntax  -  from절에 조인조건 선언

equi join (inner join)
non-equi join
self-join (자기참조가 가능한 테이블에서만)
※ 조인 조건을 잘못 정의하거나 , 조인 조건을 누락하면 cartesian product (cross join)
outer join (조인컬럼값이 null인 경우 결과집합에 포함시키기 위한 조인)

conn hr2/oracle
문> 사원이름, 부서번호, 부서이름
select last_name, department_id, department_name
from  employees  , departments  ; ---error 


select a.last_name, a.department_id, b.department_name
from  employees a, departments b;  ---? 20명의 사원 데이터 (20*8)rows, cartesian product, 조인조건 누락


select a.last_name, a.department_id, b.department_name
from  employees a, departments b
where a.department_id = b.department_id; ---? 20명의 사원 데이터?error

--natual join 은 oracle 서버가 조인할 테이블에서 동일한 이름의 컬럼으로 자동 equi 방식 조인을 수행합니다.
--natual join 은 조인할 테이블에서 동일한 이름의 컬럼 앞에 소유자 테이블명 또는 alias를 선언하지 않습니다.
--natual join 은 동일한 속성이지만, 설계할때 부모와 자식 테이블에서 이름을 다르게 정의하면 조인 수행 안됩니다
select a.last_name,  department_id, b.department_name
from  employees a natural join  departments b;  -->? 19rows?


select a.last_name, a.department_id, b.department_name
from  employees a, departments b
where a.department_id = b.department_id
and a.manager_id = b.manager_id;


select a.last_name,  department_id, b.department_name
from  employees a  join  departments b using (department_id); 


```







```sql
create table  copy_emp
as select  empno , ename, job, hiredate, sal, mgr, deptno deptid
from emp;

desc  copy_emp
select * from copy_emp;
```

문> copy_emp와 dept테이블에서 ,사번, 이름, 부서번호, 부서명 출력

```sql
select a.empno, a.ename, b.deptno, b.dname
from copy_emp a join dept b on a.deptid = b.deptno

drop table copy_emp purge; --테이블 삭제

desc salgrade
desc emp
```



문> 사원이름, 급여, 급여의 등급을 조회 출력  --non-equi join으로 해결

```sql
select a.ename, a.sal, b.grade
from emp a, salgrade b
where a.sal between b.losal and b.hisal;

select a.ename, a.sal, b.grade
from emp a join  salgrade b  on a.sal between b.losal and b.hisal;
```





문> 사원번호 사원이름 관리자번호 관리자이름을 조회결과 출력 --self join

```sql
select a.empno, a.ename, a.mgr , b.ename
from  emp a, emp b
where a.mgr = b.empno;

select a.empno, a.ename, a.mgr , b.ename
from  emp a join emp b  on a.mgr = b.empno;
```



```sql
desc employees
desc departments
desc locations
--n개의 테이블을 조인할때 최소 조인 조건은 n-1개

```

문> 사원이름, 소속 부서이름,부서가 위치한 도시를 조회 출력

```sql
select a.last_name, b.department_name, c.city
from employees a, departments b, locations c
where a.department_id = b.department_id
and b.location_id = c.location_id;

select a.last_name, b.department_name, c.city
from employees a join  departments b on a.department_id = b.department_id
join locations c  on   b.location_id = c.location_id;

```

```sql
conn scott/oracle
insert into emp (empno, ename) values (8000, 'Hong');
commit
```







문> 부서번호가 없는 사원을 포함해서 사원들의 부서이름을 함께 출력

```sql
select a.empno, a.ename, a.deptno, b.dname
from emp a, dept b
where a.deptno = b.deptno;  --8000번  Hong 사원 누락됨

select a.empno, a.ename, a.deptno, b.dname
from emp a, dept b
where a.deptno = b.deptno(+); --8000번  Hong 사원 포함

```

문>부서정보를 기준으로 부서의 소속 사원을 출력하고, 소속 사원이 없는 부서도 출력합니다.



```sql
select a.empno, a,ename, a.deptno, b.dname
from emp a left outer join dept b on a.deptno = b.deptno;



select b.deptno, b.dname, a.empno, a.ename, 
from emp a, dept b
where a.deptno = b.deptno
order by  b.deptno;   ---40번 부서정보 누락?


select b.deptno, b.dname, a.empno, a.ename, 
from emp a, dept b
where a.deptno(+) = b.deptno
order by  b.deptno;  ------40번 부서정보 포함?
```





문> 부서번호가 없는 사원을 포함하고, 소속 사원이 없는 부서도 사원들의 사번, 이름, 부서번호

부서이름을 함께 출력합니다.

```sql
select b.deptno, b.dname, a.empno, a.ename, 
from emp a, dept b
where a.deptno(+) = b.deptno(+)
order by  b.deptno;  -- outer 연산자는 양쪽에 선언 불가, 오류 


select b.deptno, b.dname, a.empno, a.ename, 
from emp a full outer join dept b on a.deptno  = b.deptno
order by  b.deptno; 
```

