subquesubquery - select문 내부에 정의된 select문(inner query, nested query)
outer query, main query

2번 이상 select를 수행해서 결과 집합을 생성해야 할때 ..하나의 select문으로 정의해서 실행시킴


single row subquery - scalar subquery
multiple row subquery - mutiple column subquery

subquery가 main query보다 먼저 수행하고, 1번 수행
co-related subquery(상관관계 subquery) - subquery가 main query의 컬럼을 참조해서, main query의 행수만큼 subquery 반복적으로 수행하는 Query

subquery가 올 수 있는 위치 
select절
from절  ---inline view
where절  --연산자 오른쪽 (subquery)
having절  --연산자 오른쪽 (subquery)
order by절


subquery를 where절이나 having절에 정의할때 single row subquery는 single row operator(>, >=, <, <=, !=, <>) 함께 사용
multiple row subquery는 multiple row operator (in, any>, any<, all<, all>)

subquery에는 모든 select절, 함수등 제약없이 사용 가능하지만, 
order by절은 from절의 inline view에서만 허용됨

rownum -결과행에 순차적인 번호를 발행 내장 컬럼
rownum은 order by 전에 발생되므로, order by 후에 rownum으로 순차적인 번호를 발행하려면 subquery를 사용합니다.

#### co-related subquery(상관관계 subquery)

```sql
 select~~
 from  table1 a
 where column 연산자 (select ~
                      from table2
                      where a.column = column2)
```




co-related subquery에서 존재 유무를 체크해주는 연산자 - exists, not exists

긴 query문에서 반복적으로 사용하는 subquery를 먼저 정의해서 재사용하려면
with 
별칭 as (subquery),
별칭 as (subquery),
별칭 as (subquery),
....
별칭 as (subquery)
select ~
from ~
where ~



set operator - 서로 다른 select의 결과를 단일 결과 집합으로 만들기 위해

합집합 - union, union all

교집합 - intersect

차집합 -  minus



select ~

from ~

[where ~]

[group by ~]

[having ~]

[order by~];



※ 각 select문에서 컬럼개수와 컬럼타입이 일치해야 합니다.
※ 결과는 첫번째 컬럼값을 기준으로 정렬된 결과가 리턴되므로 다른 컬럼으로 정렬하려면 order by절은 마지막 select문에만 허용됩니다.



**union** - 각 select의 결과 행에서 중복된 행을 제외하기 위해 sorting

**intersect** - 각 select의  결과 행에서 중복된 행을 제외하기 위해 sorting울 비교합니다.

**minus** - 첫번째 select의  결과 행에서 중복된 행을 제외하기 위해 sorting울 비교합니다.

**union all - append**  방식

##### 문> 전체 사원의 급여 평균

##### 		부서별 사원의 급여 평균

##### 		부서와 직무별 사원의 급여 평균



```sql
select to_number(null), to_char(null), avg(sal)
from emp
union all
select deptno, to_char(null), avg(sal)
from emp
group by deptno
union all
select deptno, job, avg(sal)
from emp
group by deptno, job;

select deptno, job, avg(sal)
from emp
group by rollup (deptno, job);
```







##### 문> 전체 사원들의 급여 평균과

#####     부서별 사원들의 급여 평균과 

#####     직무별 사원들의 급여 평균과

#####     부서와 직무별 사원들의 급여 평균을 단일 결과 집합으로 출력합니다.

```sql
select to_number(null), to_char(null), avg(sal)
from emp
union all
select deptno, to_char(null), avg(sal)
from emp
group by deptno
union all
select to_number(null), job, avg(sal)
from emp
group by deptno, job
union all
select deptno, job, avg(sal)
from emp
group by deptno, job;

select deptno, job, avg(sal)
from emp
group by cube (deptno, job);

select deptno, job, mgr, avg(sal)
from emp
group by grouping sets((deptno, mgr), (mgr), (job), ());
```





#테이블에 이미 존재하는 행의 데이터를 수정할때 컬럼단위로 수정합니다.

update 테이블명

set 컬럼명 = new 컬럼값 [, 컬럼명 = new컬럼값, ....]; -- 테이블의 모든 데이터



```sql
select empno, ename, deptno, sal from emp10;
update emp10
set sal = 1;
select empno, ename, deptno, sal from emp10;
rollback;
select empno, ename, deptno, sal from emp10;


```

update 테이블명

set 컬럼명 = new 컬럼값 [, 컬럼명=new 컬럼값, ....]

where 조건







```sql
update dept
set deptno = 100
where dname = 'IT' ; --error, 컬럼 size초과

update dept
set deptno = 40
where dname = 'IT' ; --error, 중복값

update emp
set deptno = 60
where empno = 7788; --error, 참조무결성제약조건 오류
```





문>SMITH사원의 급여를KING사원의 급여와 동일하도록 변경하세요.

--update의 set절 subquery (Scalar Su)

--update의 where절 subquery

```sql
update emp
set sal = (select sal from emp where ename = 'KING')
where ename = 'SMITH'

rollback;
```

문>KING사원과 동일한 부서에 근무하는 KING을 제외한 다른 사원의 급여를 20%인상합니다.



```sql
update emp
set sal = sal*1.2
where deptno = (select deptno from emp where ename = 'KING')
and ename<>'KING'
```













--테이블이 이미 저장되어 있는 레코드를 삭제하려면
delete from 테이블명;  --오라클에서는 from절 생략가능

delete 테이블명 where 조건 ; --조건을 만족하는 행만 사용

delete 테이블명 where 컬럼 연산자(subquery) ;



```sql
select * from emp;
delete from emp;
select * from emp;
rollbackl

delete from emp where deptno = 30;
select * from emp;

rollback;
select * from emp;

delete from dept;
delete from dept where deptno = 55;
```



문> ADAMS 사원과 동일한 직무를 담당하는 사원 삭제(ADAMS 사원은 제외)

```sql
select ename, job
from emp;
delete from emp
where job = (select job from emp where ename = 'ADAMS')
and ename<>'ADAMS'

select ename, job
from emp;

rollback;
```

### merge문

ETL(데이터 이관 작업)에 쓰여지는 구문 중 하나

```sql
merge int 대상테이블 t
using 소스테이블 s
on t.pk컬럼 = s.pk컬럼
when matched then
update set t.컬럼 = s.컬럼,......
[delete where 조건]
when not matched then
insert(t.컬럼리스트)
values(s.컬럼리스트);
```

문> emp테이블로부터 30번 부서 사원정보를 emp30 테이블로 복제하시오
30번부서 사원은 직무와 급여를 update하고
급여가 2500이상이면 삭제하시오
20, 10번부서 사원은 사원번호와 이름과 부서번호만 입력하시오 



```sql
update emp30
set sal=null;

alter table emp30 modify (job  varchar2(15), sal number(8,2));

select * from emp30
```



**Trasaction** - Unit of Work(분리되어 수행될 수 없는 작업단위)

**ACID** - 원장성, 일관성, 격리성,  영속성

DB관점의 Transaction은 변경(DML, DDL, DCL)이 포함되면

select는 Transaction으로 포함되지 않고

Transaction 단위

1개 이상의 DML들로 구성 - 명시적 commit, rollback

1개의 DDL - auto commit;

1개의 DCL - auto commit;

수행중인 DML 트랜잭션의 세션이 비정상종료하면 oracle server는 rollback 합니다.

수행중인 DML 트랜잭션의 세션을 정상종료(exit;) 하면 oracle server는 commit



**읽기 일관성** - select하는 user들이 변경중이 user 작업이 종료될때까지 기다리지 않고, 
변경 작업하려는 user들은 select하는 user들이 검색을 종료할때까지 기다리지 않고,
변경 작업중인 user들은 변경중인 값을 조회 결과로 볼 수 있고, 
변경 작업중이 아닌 user들은 DB에 저장된(commit된) 데이터 값을 조회 결과로 볼 수 있도록 ... 

오라클 서버는 읽기 일관성을 위해서 Lock, undo segment등을 지원합니다.



```sql
create table test (num number(2));
insert into test values (1);
insert into test values (2);
savepoint a;
insert into test values (3);
insert into test values (4);
savepoint b;
insert into test values (5);
insert into test values (6);
select * from test;
rollback to savepoint b;
select * from test;
rollback to savepoint a;
select * from test;
rollback;


https://localhost:1158/em

cmd 2개 실행
sqlplus scott/oracle
update emp
set sal = sal * 1.1
where empno = 7900;

```



Table - Row + Column

​			물리적 Data 저장

​			Heap, IOT, partition

View - 			table의 Data에 대한 window

보안				물리적 data x

복잡한			논리적 Table

Query			Select문으로 정의









## Window



**RANK :**  특정 컬럼에 대한 순위를 구하는 함수로서 동일한 값에 대해서 동일한 순위를 가지며, 동일한 순위의 수만큼 다음 순위는 건너뛴다. 

```sql
select  ename, job, sal, 
        rank( ) over ( order by sal desc ) sal_rank
        , rank() over (partition by job order by sal desc) job_rank
from emp;  -
```



**DENSE_RANK :** 특정 컬럼에 대한 순위를 구하는 함수로서 동일한 순위 다음의 순위는
동일 순위의 수와 상관없이 1 증가된 값을 돌려준다**.**

```sql

select  ename, job, sal, 
        rank( ) over ( order by sal desc ) sal_rank
        , rank() over (order by sal desc) sal_rank2
from emp;  --? 

```

**ROW_NUMBER** 

```sql
select  ename, job, sal, 
        rank( ) over ( order by sal desc ) sal_rank
        , rank() over (order by sal desc) sal_rank2
                , row_number() over (order by sal desc) sal_rank2

from emp;
```





#### Sum 

```sql
select  ename, mgr, sal, sum(sal) over (partition by mgr) 
from emp;
```



#### RANGE  UNBOUNDED  PRECEDING 



```sql
select  ename, mgr, sal, 
        sum(sal) over (partition by mgr order by sal
                       rows between unbounded preceding and current row   ) 
from emp;

select  ename, mgr, sal, 
        sum(sal) over (partition by mgr order by sal
                       rows between 1 preceding and 1 following) 
from emp;


select  ename, mgr, sal, 
        count(sal) over (order by sal
                         range between 200 preceding and 200 following   ) 
from emp;
```

문> emp 테이블에서 사원이름, 직무, 급여 데이터와 전체 사원의 급여가 높은 순서와 JOB별로 급여가 높은 순서 출력하시오

```sql
select  ename, job, sal, 
        rank( ) over ( order by sal desc ) sal_rank
        , rank() over (partition by job order by sal desc) job_rank
from emp;  --? 
```







문> emp 테이블에서 사원이름, 직무, 급여 데이터와 전체 사원의 급여가 높은 순서의 순위를 rank(), dense_rank(), row_number()로 출력하시오

```sql
select  ename, job, sal, 
        dense_rank( ) over ( order by sal desc ) sal_rank
        ,  rank( ) over ( order by sal desc ) sal_rank2
        ,  row_number( ) over ( order by sal desc ) sal_rank2
from emp; 
```







문> emp 테이블에서 관리자로 파티셔닝된 사원이름, 오름차순 정렬된 급여 데이터 누적 합 출력

```sql
select  ename, mgr, sal, sum(sal) over (partition by mgr order by sal) 
from emp;
```





문> emp 테이블에서 관리자로 파티셔닝된 사원이름, 오름차순 정렬된 급여 데이터 누적 합 출력

```sql
select  ename, mgr, sal, 
        sum(sal) over (partition by mgr order by sal
                       range  unbounded preceding) 
from emp;
```





문> emp 테이블에서 관리자로 파티셔닝된 사원이름, 오름차순 정렬된 급여 데이터의 행 기준 누적 합 출력

```sql
select  ename, mgr, sal, 
        sum(sal) over (partition by mgr order by sal
                       rows between unbounded preceding and current row   ) 
from emp;
```






문> emp 테이블에서 관리자로 파티셔닝된 사원이름, 오름차순 정렬된 급여 데이터의 행 기준으로 현재행의 앞에 한행, 뒤에 한 행의 누적 합 출력

```sql
select  ename, mgr, sal, 
        sum(sal) over (partition by mgr order by sal
                       rows between 1 preceding and 1 following   ) 
from emp;
```





문> emp 테이블에서 관리자로 파티셔닝된 사원이름, 오름차순 정렬된 급여 데이터의 행 기준으로 급여의 -200~+200 범위의 급여자 수 출력

```sql
select  ename, mgr, sal, 
        count(sal) over (order by sal
                         range between 200 preceding and 200 following   ) 
from emp;
```









```sql
select  ename, hiredate, sal, 
        lag(sal) over (order by hiredate ),
        lag(sal, 2, 0) over (order by hiredate ) 
from emp;

select  ename, hiredate, sal, 
        lead(sal) over (order by hiredate ),
        lead(sal, 2, 0) over (order by hiredate ) 
from emp;
```





conn scott/oracle

테이블 생성하려면 create table 시스템 권한이 있어야 합니다.

tablespace(data container) 저장소에 quota가 할당되어 있어야 합니다.

table 또는 컬럼 이름 규칙 : 

영문자또는 _, $, #로 시작,

두번째 문자부터 숫자 허용

키워드 안됨

schema - 서로 연관된 table, index등의 객체를 그룹핑하는 논리적 개념

​				객체 명을 재사용할 수 있는 namespace역할을  합니다.

​				오라클은 user명을 schema명으로 사용합니다.

schema내에서 중복된 이름 사용 불가

길이 제한 30자

DB이름 길이 제한 8자



컬럼타입 : 

**char** 고정길이 문자열 ~2000byte

**varchar2** 가변길이 문자열 ~4000byte

**number**(p, s)

**date** --_세기 _년 _월 _일 _시 _분 _초

**timestamp** --date타입 확장, 1/10^9의 정밀한 초값 저장

 **timestamp  with timezone**

**timestamp  year to month**

**timestamp  day to second**

**rowid**

**CLOB** (character large object) ~4G

**raw** - binary 형식의 값 저장 예)지문, 증명사진 ~2000byte

**BLOB**(binary large object) ~4G

**BFILE** - read only 가능한 file을 DB외부에 운영체제의 풀더에 저장, TX처리는 불가



```sql
desc user_tables

select table_name, tablespace_name from user_tables;

create table 테이블명 (
컬럼명 컬럼타입(size) ,
컬럼명 컬럼타입(size) [default 값],
컬럼명 컬럼타입(size) [제약조건],
.......
[제약조건]
)   
[..........];
CTAS이용해서 테이블 구조만 복제, 테이블 구조+데이터 복제, 테이블 구조 + 데이터 복제 가능

create table 테이블 이름
as
(subquery);
create table emp20
as select empno, ename, deptno, sal*12
from emp
where deptno = 20; --error

create table emp20
as select empno, ename, deptno, sal*12 salary
from emp
where deptno = 20;
desc emp20
select * from emp20;

drop table emp20 purge;

create table emp20 (empid, name, deptid, salary)
as select empno, ename, deptno, sal*12
from emp
where deptno = 20;


제약조건  constraint - table의 DML수행시 규칙
Primary key
not null
Uniuqe Key
Foreign Key
cheak
```



drop table;

data > Undo 생성없이 물리적 삭제

구조삭제

복구하려면 back up

```sql
create table copy_dept
as select * from dept;
desc copy_dept
select * from copy_dept;


drop table copy_dept;
desc copy_dept
select * from copy_dept;
select tname from tab;	-----BIN$-----이름의 테이블
select * from user_recyclebins;
select * from "BIN$~~~~~~~";


```



```sql
create table userinfo

(userid varchar2(10) not null,

username varchar2(15) constraint userinfo_nn not null ,

age number(30)

);

desc userinfo
insert into userinfo
values('tester1','테스터1', 20);

insert into userinfo (username, age)
values ('테스터1', 20); --error

select * from userinfo;
select constraint_name, constraint_type
from user_constraints
where table_name = 'USERINFO';

insert into userinfo (userid, age)
values('tester2', 30);

alter table userinfo disable constraint userinfo_nn;

insert into userinfo






```

======unique 제약 조건=============

```sql
create table userinfo 
(userid  varchar2(10)  constraint userinfo_uk  unique,
 username  varchar2(15)  ,
 age  number(30)
);

desc userinfo
insert into userinfo 
values ('tester1', '테스터1', 20);

insert into userinfo  (username, age)
values ( '테스터2', 25);    ---userid는 null?

insert into userinfo  (username, age)
values ( '테스터3', 30);    ---userid는 null?

insert into userinfo 
values ('tester1', '테스터5', 35); ---error

select * from userinfo;

select constraint_name, constraint_type
from user_constraints
where table_name = 'USERINFO';

select index_name, uniqueness
from user_indexes
where table_name = 'USERINFO';

--oracle server는 unique제약조건이 선언된 컬럼에 자동으로 unique index 생성합니다.

alter table userinfo disable constraint userinfo_uk;
select index_name, uniqueness
from user_indexes
where table_name = 'USERINFO'; --? 
--제약조건 비활성화 하면 인덱스 자동 삭제 

alter table userinfo enable constraint userinfo_uk;
 
select index_name, uniqueness
from user_indexes
where table_name = 'USERINFO'; ---? index 다시 자동 생성?



drop table userinfo purge;


```



============primary key 제약조건 ===================

```sql
#primary key = not null+unique
#다른 제약조건은 하나의 테이블에 여러개 선언가능합니다만,
primary key 제약조건은 하나만 선언 가능합니다.

create table userinfo 
(userid  varchar2(10)  constraint userinfo_pk primary key,
 username  varchar2(15)  ,
 age  number(30)
);

desc userinfo
insert into userinfo 
values ('tester1', '테스터1', 20);---?

insert into userinfo  (username, age)
values ( '테스터2', 25);     ---?error

insert into userinfo 
values ('tester1', '테스터5', 35); ---?

select * from userinfo;

select constraint_name, constraint_type
from user_constraints
where table_name = 'USERINFO';

select index_name, uniqueness
from user_indexes
where table_name = 'USERINFO';

```





=============================제약조건 : check ============================

```sql
create table userinfo(
userid  varchar2(10),
username  varchar2(15),
gender   char(1) constraint userinfo_ck  check (gender in ('F', 'M')),
age  number(2) check (age > 0 and age < 100)
);

select constraint_name, constraint_type, search_condition
from user_constraints
where table_name='USERINFO';

insert into userinfo  values ('a001', 'an', 'f', 20);  --? error
insert into userinfo  values ('a001', 'an', 'w', 20); --?error
insert into userinfo  values ('a001', 'an', null, 20);  
insert into userinfo  values ('a002', 'choi', 'M', 0); --?error
insert into userinfo  values ('a002', 'choi', 'M', 100); --?error
insert into userinfo  values ('a002', 'choi', 'M', 25);  --?

drop table user_info purge;
```

