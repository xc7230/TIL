# 마이바티스(mybatis)



### 마이바티스(mybatis)란?

마이바티스는 개발자가 지정한 SQL, 저장프로시저 그리고 몇가지 고급 매핑을 지원하는 퍼시스턴스 프레임워크이다. 마이바티스는 JDBC로 처리하는 상당부분의 코드와 파라미터 설정및 결과 매핑을 대신해준다. 마이바티스는 데이터베이스 레코드에 원시타입과 Map 인터페이스 그리고 자바 POJO 를 설정해서 매핑하기 위해 XML과 애노테이션을 사용할 수 있다.






  

```
insert into products ( prodnum ,pname, unitPrice, Description, Category, Manufacturer, UnitsInStock,  Condition,  Filename )
values ( 'P1234', 'iPhone 6s',800000, '4.7-inch, 1334X750 Renina HD display 8-megapixel iSight Camera,);
'Smart Phone','Apple', 1000, 'New', 'P1234.png');

insert into products ( prodnum ,pname, unitPrice, Description, Category, Manufacturer, UnitsInStock,  Condition,  Filename )
values ( 'P1235','LG PC 그램',
1500000,
'13.3-inch, IPS LED display, 5rd Generation Intel Core processors',
'Notebook',
'LG',
1000,
'Refurbished',
'P1235.png');

insert into products ( prodnum ,pname, unitPrice, Description, Category, Manufacturer, UnitsInStock,  Condition,  Filename )
values ( 'P1236',
'Galaxy Tab S',
900000,
'212.8*125.6*6.6mm,  Super AMOLED display, Octa-Core processor',
'Tablet',
'Samsung',
1000,
'Old',
'P1236.png');
commit;


select * from products;

select * from products where prodnum =? ;

select * from products where unitPrice between ? and ?;


update products set unitPrice = ?, UnitsInStock=?  where prodnum = ? ;

delete from products  where prodnum = ? ;


create table products (
prodnum    varchar2(8)  primary key ,   --제품번호
pname      varchar2(30),   --상품 이름
category   varchar2(30), --상품 분류
description  varchar2(1000),--상품 특성, 설명
filename    varchar2(100),        ----이미지 파일 경로
manufacturer  varchar2(50), --제조사
unitPrice    number(7),     --개당 가격
unitsInStock   number(5),    --제고
Condition   varchar2(30)
);
 
 
===========================================================
1. maven 프로젝트 생성 (pom.xml)  //
2. mapper 파일 설정  (ProductMapper.xml) //
3. spring 설정 파일 설정  (application.xml) //
4. 엔티티 클래스 생성
5. DAO 클래스 생성
6. 서비스 클래스 생성
7. test 클래스 생성 실행 결과 보기
 
```