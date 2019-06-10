# 인덱스(INDEX)



```sql
create table category (
cid   number(5),
cname   varchar2(20) 
);
insert into category values (10000, 'BOOK');
insert into category values (20000, 'Music');
insert into category values (30000, 'Game');
insert into category values (40000, 'Movie');

select * from category;
creat table product (
prodid number(5),
pname varchar2(50),
price number(6),
cid number(5) constraint product_tk references category(cid)

); --error


--foreign key제약조건이 참조하는 부모 컬럼에는  primary key 또는 unique key 제약조건이 선언되어 있어야 합니다.

alter table category add constraint category_pk  primary key (cid);

create table product (
prodid   number(5),
pname    varchar2(50),
price    number(6),
cid      number(5) constraint product_fk references category(cid)
);

select constraint_name, constraint_type
from user_constraints
where table_name = 'PRODUCT';

insert into product values(1, 'java', 5000, 10000);
insert into product values(2, 'oracle', 5000, 50000);
insert into product values(3, 'BTS', 15000, 20000);
update product
set cid = 2222 where prodid = 3; --error

delete from category where cid = 40000;
delete from category where cid = 10000; --error
update category set cid = 15000 where cid = 10000; -- ?


create table product (
prodid   number(5),
pname    varchar2(50),
price    number(6),
cid      number(5) ,
constraint product_fk foreign key (cid) references category(cid)  -- on delete cascade 또는 on delete set null
);

alter table 테이블명 modify (컬럼 컬럼타입(크기) );
--컬럼 타입 변경할 때  컬럼값이 존재하더라도 char5->varchar2(10) 변경은 가능
--컬럼 타입 변경할 때 호환되지 않는 컬럼타입으로 변경할때는 컬럼값을 null로 변경한후에 컬럼타입을 변경할 수 있습니다.
--컬럼 크기를 변경할 때 크기 증가는 항상 가능하지만, 컬럼값이 존재할때 컬럼 크기를 줄이려면 저장된 컬럼값의 최대 길이보다 작게 줄일 수 없습니다.
--not null제약조건 추가

alter table 테이블명 add constraint~;
alter table 테이블명 drop constraint~;
alter table 테이블명 add (컬럼 컬럼타입(크기), 컬럼타입(크기).....)
alter table 테이블명 drop (컬럼 컬럼타입(크기), 컬럼 컬럼타입(크기),..);
alter table 테이블명 drop column 컬럼명;
alter table 테이블명 rename column old명 to new명;
alter table 테이블명 enable constraint~;
alter table 테이블명 disable constraint~;

drop table 테이블명; --테이블이름 rename 되어 recyclebin에 저장됨....... 저장공간이 부족할때
oracle server가 제거함
drop table 테이블명 purge;  
purge recyclebine;

truncate table 테이블명 [reuse storage]; -- 구조만 남겨두고, data는 완전 삭제(recyclebin에도 undo data도 생성하지 않음)


drop table~ : --table메타정보, data, 제약조건, index도 함계 삭제됩니다.
```



PK와 UK에 index 자동 생성 목적 - 정합성 체크, 중복값 체크를 빠르게 

index 생성에 적합한 조건

where 조건에 사용되는 컬럼

join컬럼

order by 컬럼

컬럼중에서 distinct value(선택도)값이 많아야 합니다.

where절의 = 연산조건의 결과 행이 5%이내

인덱스 생성 컬럼으로 조회 결과 행수가 10%를 초과하면 손익분기점으로 table full scan이 더 유리합니다.

거의 update가 발생하지 않은 컬럼 - 자주 update 되는 컬럼은 인덱스 생성하면 성능 저하

4개 블럭이상에 데이터가 저장된 테이블

단일컬럼인덱스

복합컬러인덱스

**unique** 인덱스

**non-unique** 인덱스

**funcation - based** 인덱스 (컬럼값의 내림차순으로 생성, 컬럼표현식)

```sql
create index 인덱스명 on 테이블(컬럼);
alter index 인덱스 명 on 테이블(컬럼 desc);
drop index 인덱스명;
```



# 뷰(VIEW)

**simple view**



**complex view** 

하나 이상의 테이블에 대한 select문으로 정의, 컬럼표현식



create view 권한이 있어야 합니다.

```sql
conn scott/oracle
select * from session_privs; --user_sys_privs

create view empno, ename, deptno, job, sal*12
from emp
where deptno = 20;

consys/oracle as sysdba
grant create view to scott, hr;

conn scott/oracle
create view emp20_vu
as select empno, ename, deptno, job, sal*12 salary
from emp
where deptno =
```



```sql
con sys/oracle as sysdba
grant create view to scott, hr;

conn scott/oracle
create view emp20_vu
as select empno, ename, deptno, job, sal*12  
   from emp
   where deptno = 20; --error

create view emp20_vu
as select empno, ename, deptno, job, sal*12 salary
   from emp
   where deptno = 20

select text
from user_views
where view_name = 'EMP20_VU';

create or replace view~~~~ => alter view 역할

create or replace view dept_vu
as select *
   from dept10; ---error?

create or replace foce view dept_vu
as select *
   from dept10;   ---?
   
 select object_name, object_type, status
from user_objects
where object_name = 'DEPT_VU'; --dept_vu는 생성되었으나 유효하지 않음

select * from emp20_vu; --뷰의 데이터 조회
insert into emp20vu values (9005, 'Song' , 20 , 'SALESMAN', 2000);

create view emp20_vu
as select empno, ename, deptno, job, sal*12 salary
   from emp
   where deptno = 20
insert into emp20vu values (9005, 'Song' , 20 , 'SALESMAN', 2000);

select * from emp20_vu;
select empno, ename, deptno, job, sal
   from emp
   where deptno = 20;

update emp20_vu set sal = 1900 where empno = 9005;
select * from emp20_vu;
select empno, ename, deptno, job, sal
   from emp
   where deptno = 20;

delete from emp20_vu where empno = 9005;
select * from emp20_vu;
select empno, ename, deptno, job, sal
   from emp
   where deptno = 20;

delete from emp20_vu ;  --view객체 삭제, base 테이블에 영향을 주는지?
select * from emp20_vu;
select empno, ename, deptno, job, sal
   from emp
   where deptno = 20;

create or replace view emp20_vu
as select empno, ename, deptno, job, sal
   from emp
   where deptno = 20
   with check option;  --check 제약조건을 설정

select constraint_name, constraint_type
from user_constraints
where table_name = 'EMP20_VU';

insert into emp20vu values (9005, 'Song' , 20 , 'SALESMAN', 2000);  --error
select * from emp20_vu;
select empno, ename, deptno, job, sal
   from emp
   where deptno = 20;

create or replace view emp20_vu
as select empno, ename, deptno, job, sal
   from emp
   where deptno = 20
   with read only;  --제약조건 설정, select만 가능
   
select constraint_name, constraint_type
from user_constraints
where table_name = 'EMP20_VU';

insert into emp20_vu values (9005, 'Song', 20, 'SALESMAN', 2000);
delete from emp20_vu; 


```



## 시퀀스(Sequence)

```sql
create sequence emp_seq;
select *
from user_sequences;
--시퀀스 객체를 생성하면 자동으로 시퀀스의 내장 컬럼 curr_val, next_val을 생성합니다.
select emp_seq.currval
from dual;  --시퀀스를 생성하면 최초값을 생성한 다음에 currval을 확인가능합니다.

select emp_seq.nextval
from dual;

insert into emp(empno, ename)
values(emp_seq.nextval , 'Kang');

select empno, ename
from emp;

update dept
set deptno = emp_seq.nextval
where deptno = 50;

select deptno, dname
from dept;

alter sequence 시퀀스명
increment by~
maxvalue ~
minvalue ~
cycle ~
cache ~;

drop sequence 시퀀스명 :  --메타 정보만 data dictionary로부터 삭제됨

```

## 동의어(SYNONYM)

테이블 ,뷰, 시퀀스 등 객체 이름 대신 사용할 수 있는 다른 이름을 부여하는 객체

```cmd
sqlplus system/oracle

grant create SYNONYM to scott;
```



**동의어(SYNONYM) 생성**

```sql
create SYNONYM E  
for emp;  --E를 쓰면 emp테이블의 데이터가 조회됩니다.

select * from E; --테이블 내용 조회
```



**동의어 (SYNONYM)삭제**

```sql
drop SYNONYM E;
```



## 권한

396p



**시스템 권한**

DB에서 특정 sql을 수행할 수 있는 권한

**객체권한**

예)  

table에는

view에는



sequence



```sql
conn kim/oracle
select * from scott.emp;

conn scott/oracle
select * from scott.emp;
grant select on scott.emp to hr; --error

conn scott/oracle
grant select on emp to kim with grant option;

conn kim/oracle
select * from scott.emp;
grant select on scott.emp to hr; --?

conn hr/oracle
select * from scott.emp; --?

conn scott/oracle
revoke select on emp from hr --? error, 객체권한은 직접 권한을 준 user가 회수 가능합니다.
revoke select on emp from kim

conn kim/oracle
select * from scott.emp; --?

conn hr/oracle
select * from scott.emp; --? 객체권한은 cascade로 회수됨


```











```sql
conn hr/oracle
select *
from emp; -- error, select * from hr.emp;를 수행함

select *
from scott.emp; --권한 없어서오류


```



```cmd
conn / as sysdba
create user kim
identified by 1234
password expire;

conn kim/1234
--alter user kim identified by 새비밀번호:
--password 명령어로 비밀번호 변경

```



```sql
conn kim / oracle
--create session 권한
```



```cmd
conn / as sysdba
grant create session to kim;
```



```sql
conn kim / oracel
create table test (name varchar2(10)); --error

select user from dual;

#dual --- 소유자?
select owner, table_name
from all_tables
where table_name= 'DUAL'; --sys

--public으로 dual 테이블에 대한 select 권한을 줌

desc dual  -- ?  dummy컬럼 존재
select * from dual;   ---? dummy컬럼값은 x

dual의 목적....from절이 필수이므로 단순 계산결과, 함수 결과를 확인할때


```



```sql
select *
from 'user%privs'; -- user_tab_privs, user_sys_privs
select *
from session_privs;

```



## 롤(Predefined Roles)

신규 생성 사용자는 아무런 권한이 없으므로 권한을 부여 해줘야 합니다. 롤은 여러 권한을 한 번에 부여하고 해제할 수 있습니다.

Role을 생성할 수 있는 권한은 DBA

1.create role 롤이름;

2.grant 시스템권한, 객체 권한 to 롤이름;

3.grant 롤이름 to 사용자 | 롤이름 | public;



revoke 롤이름 from 사용자 | 롤이름 | public; ;

--user_role_privs

drop role 롤이름

Role의 또 하나의 장점은 동적 권한 관리 가능





## JDBC

C:\app\student\product\11.2.0\dbhome_1\jdbc\lib 에서 ojdbc6파일 복사



C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext 에 붙여넣기





```java
package lab.java.core;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBTest {

	public static void main(String[] args) {

		
		Connection con = null; //DB연결상태 새션 정보
		String url = "jdbc:oracle:thin:@localhost:1521:orcl";
		try {
			Class.forName("oracle.jdbc.OracleDriver");
			System.out.println("driver loading 성공");
			con = DriverManager.getConnection(url, "scott","oracle");
			System.out.println("DB connect 성공");
		} catch(ClassNotFoundException e) {
			System.out.println("dirver 없음");
		} catch(SQLException e) {
			System.out.println(e.getMessage());
			//연결실패
		}
	}

}

```





SQL문이 select 일 경우

```java
package lab.java.core;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DBTest {

	public static void main(String[] args) {

		
		Connection con = null; //DB연결상태 새션 정보
		Statement stat = null;
		ResultSet rs = null;
		
		String url = "jdbc:oracle:thin:@localhost:1521:orcl";
		String sql = "select * from dept";
	
		try {
			Class.forName("oracle.jdbc.OracleDriver");
			//System.out.println("driver loading 성공");
			con = DriverManager.getConnection(url, "scott","oracle");
			//System.out.println("DB connect 성공");
			
			stat = con.createStatement();
			rs = stat.executeQuery(sql);
			while(rs.next()) {
				System.out.print(rs.getInt("deptno"));
				//System.out.print(rs.getInt("1"));
				System.out.print(rs.getString("dname"));
				//System.out.print(rs.getString("2"));
				System.out.println(rs.getString("loc"));
				//System.out.print(rs.getString("3"));



				
            }
		} catch(ClassNotFoundException e) {
			System.out.println("dirver 없음");
		} catch(SQLException e) {
			System.out.println(e.getMessage());
			//연결실패
		} finally{
			try {
				if(rs !=null) rs.close();
				if(stat !=null) stat.close();
				if(con !=null) con.close();
			}
			catch(Exception e) {
				e.printStackTrace();
			}
		}
	}

}

```



insert

```java
package lab.java.core;

import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Properties;


public class DBTest {

	public static void main(String[] args) {

	
		Connection con = null; //DB연결상태 새션 정보
		PreparedStatement stat = null;
		String sql = "insert into dept values(?,?,?)";
		String url = "jdbc:oracle:thin:@localhost:1521:orcl";
	
		try {
			Properties prop = new Properties();
			prop.load(new FileInputStream("C:/workspace2/Day13/src/dbinfo.properties"));
			Class.forName(prop.getProperty("driver"));
			System.out.println("driver loading 성공");
			con = DriverManager.getConnection(prop.getProperty("url"),
					prop.getProperty("user"),
					prop.getProperty("pwd")	);
			System.out.println("DB connect 성공");
			
			stat = con.prepareStatement(sql);
			stat.setInt(1, 70);
			stat.setString(2, "Bigdata");
			stat.setString(3, "Seoul");
			
			int rows = stat.executeUpdate();
			if(rows>0) {
				System.out.println("insert 성공");
			}
		
		} catch(ClassNotFoundException e) {
			System.out.println("dirver 없음");
		} catch(SQLException e) {
			System.out.println(e.getMessage());
			//연결실패
		} catch(IOException e) {
			System.out.println(e.getMessage());
		}
		
		finally{
			try {
			
				if(stat !=null) stat.close();
				if(con !=null) con.close();
			}
			catch(Exception e) {
				e.printStackTrace();
			}
		}
	}

}

```











#### ---------------------------------------------Review------------------------------------------------------------

순위관련 함수
rank() over (partition by 컬럼 order by 컬럼 rows|range  unbounded preceding|between current row and unbounded following | n preceding |n following |) 
dense_rank()
row_number()

집계관련 window 함수
sum(), min(), max(), avg(), count()

행순서 관련 함수
first_value()
last_value()
lag(컬럼, n, null대체값)
lead(컬럼, n, null 대체값)

## DML

새 데이터 추가

insert into 테이블명 (컬럼명 리스트) values (컬럼명 리스트의 순서와 타입에)

insert into 테이블명 values (테이블에 선언된 컬럼순서대로 모든 값);

values절에nullm default, 단일행함수 등 사용가능

insert into 테이블명 (컬럼형 리스트) subquery: -- 컬럼명 리스트는  subquery의 컬럼순서 , 개수, 타입과 일치해야 합니다.

insert 오류 - 컬럼타입 불일치, 컬럼크기 불일치, 제약조건 오류



## 컬럼 값 변경

update 테이블명 set 컬럼명 = 변경할 값 [, 컬럼명 = 변경할 값........];

update 테이블명 set 컬럼명 = 변경할 값 [, 컬럼명 = 변경할 값........] where  조건;



update 테이블명 set 컬럼명 =(subquery) [, 컬럼명 = 변경할 값...] where subquery

update 오류 - 컬럼타입 불일치, 컬럼크기 불일치, 제약조건 오류

변경할 값에 null,default, 단일행 함수 등 사용가능



## 테이블의 행 삭제

delete from 테이블명 ; -- 모든 행 삭제

delete 테이블명; -- oracle 에서 from 생략

delete from 테이블명 where 조건 ; --조건을 만족하는 행만 삭제

delete from 테이블명 where (subquery) ;

--참조무결성제약조건오류 : 참조하는 지식레코드가 존재하면 부모 레코드는 삭제할 수 없습니다.

예) 부서테이블의 레코드를 삭제하려면 소속 사원이 없는 부서정보 레코드만 삭제 가능합니다.

## ELT 작업에 사용되는 하나의 DML로 insert, update, delete 수행

merge into 대상테이블 t
using 소스테이블 s
on (s.pk컬럼 = t.pk컬럼)
when matched then
  update set t.컬럼 = s.컬럼, ...
  delete where조건
when not matched then
  insert (t.컬럼, t.컬럼,....)
  values (s.컬럼, s.컬럼,...);



## TCL (Transaction Control Language)

Transaction - Unit or Work, all or nothing, ACID

DB에서 Transaction 단위 - 하나 이상의 DML, 하나의  DDL(auto commit)

하나 이상의 DML로 구성된 트랜잭션은 명시적으로 commit; 또는 rollback;해야합니다

트랜잭션 수행중에 DB 연결된 세션 정상 종료 (exit;)할 경우 oracle server는 트랜잭션을 commit합니다.

트랜잭션 수행중에 DB 연결된 세션 비정상 종료 (exit;)할 경우 oracle server는 트랜잭션을 rollback합니다.

긴 트랜잭션의 경우 rollback을 일부 할 수 있습니다. - savepoint 식별자; ,

## 읽기 일관성 

변경중인 user는 자신이 변경중인 값만 조화되고, 변경중이지 않는 user 들은 DB에 이전에 commit되서 저장된 값을 조회합니다. Lock과 undo data를 이용해서 읽기 일관성 보장합니다.

undo data는 트랜잭션을 rollback을 하면 변경전값을 undo segment로부터 restore(복원)합니다.



## 데이터베이스의 객체

**table** 

 구조, 물리적 data (Record + Column)

 heap, partition, IOT, clustered,....종류

**view**

table에 대해서 select로 정의된 table의 window역할

보안, 간결한 select문 사용을 위해서 base가 되는 table 이나 view가 있어야 합니다.

예외) MeterializedView - 성능향상이 목적인 물리적 data를 가지는 view

**index**

테이블의 컬럼에 생성

where절에 검색조건으로 사용되는 컬럼, join 컬럼 , order by 절의 컬럼

내부적으로 oracle server가 select 수행시 사용

b*tree구조로 저장

**sequence** 

순차적으로 숫자값이 저장되어야 하는 컬럼 (주문번호, 게시판의 글번호등) 의 값을 자동으로 발행해주는 객체

최솟값, 최대값, 증감값 설정합니다.

**synonym(동의어)** 

schema명.객체@dblink명 과 같은 객체이름을 간결하게 사용하기 위한 동의어

#테이블 생성

creat table 테이블명 (

컬러명 컬럼타입(크기) 제약조건 | default 기본값,

...

)

[tablespace 저장소명

storage...];

#테이블 생성을 위해 필요한 권한 - creat table 권한 , tablespace에 대한 quota가 할당되어 있어야 합니다.

#테이블명, 컬럼명 이름 규칙

대소문자 구별 안함 - Data Dictionary에는 대문자 저장됨

첫문자로 영문자, _ , $, # 허용

두번쨰 문자부터 숫자 허용

키워드 허용 안됨

동일 schema내에서 같은 이름의 객체 안됨

길이제한 30자 ( 데이터베이스이름 길이 제한 8자)



schema

서로 연관된 객체들을 그룹핑, 오라클에서는 user명을 schema명으로 사용함 user소유의 객체들을 그룹핑해서  다른 user소유의 객체들을 구별하는 namespace역할을 하면서 동일한 이름의 객체를 다른 schema에서 사용 가능



schema명,객체명



#컬럼타입

char

varchar2

number

date

timestamp

timestamp with timezone

interval year to month

interval day to second

Bfile

BLOB(LONG RAW)

CLOB(LONG)

RAW

rowid 

행주소(objectid+fileid+blockid+행순서번호)



```sql

creat table 태이블명 (컬럼명 리스트)
as select ~
from~
[where~]

--select절의 컬럼 리스트와 create table 절에 선언된 컬럼명 리스트의 순서 개수, 타입이 일치해야 합니다.
```



#테이블의 구조 복제

```sql
creat table 태이블명 (컬럼명 리스트)
as select ~
from~
where 1=2; -- false조건
```



## 제약조건(constraint) 

 DML 수행시 컬럼값의 허용 또는 제한규칙

primary key - unique + not null

not null - null 허용안함 , 컬럼레벨에서만 제약조건 선언가능

unique -중복값을 허용허자 않음, oracle은 null은 unique 값으로 취급해서

check - 특정값의 허용 범위

foreign key 



```sql
create table emp2 (
empno number(4),
ename varchar2(15) constraint 이름 not null,  --컬럼 레벨
    hiredate date constraint 이름 not null,
    job varchar2(15) constraint 이름 not null,
    sal number(8, 2) ,
 constraint emp2_pk primary key (empno, ename) --테이블 레벨
);
```



컬럼에 index가 자동 생성되는 제약조건 - primary key, unique key

제약조건 메타 정보 조회 - user_constraints, all_constraints, dba_constraints

테이블의 메타 조건 조회 - user_tables (tab), all_tables, dba_tables

컬럼 메타의 정보 조회 - user_indexes, user_ind_columns











