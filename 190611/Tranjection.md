**테이블 컬럼 추가**

```sql
 alter table ~ add (컬럼 컬럼타입 [제약조건]);
```



**테이블 컬럼 삭제 **

```sql
alter talble ~ drop column 컬럼명;

alter table ~ drop (컬럼, 컬럼);
```

**테이블 컬럼 이름 변경** 

```sql
alter table ~ rename column old new;
```

**테이블 컬럼타입 또는 size변경**

```sql
alter table ~ modify(컬럼 컬럼타입(size))
```



**제약조건을 컬럼추가**

```sql
alter table ~ add constraint 이름 타입;
```



**칼럼에 정의되어 있는 제약조건 삭제**

```sql
alter table ~ drop constraint 이름 ;
```



**제약조건을 활성화**

```sql
alter table ~ enable constraint 이름;
```



**제약조건을 비활성화**

```sql
alter table ~ disable constraint 이름;
```

**테이블 삭제**

```sql
 drop table ~ ;  또는 drop table ~ purge;
```

**recyclebin으로부터 drop된 테이블 복원**

```sql
flashback table ~ to before drop;
```

**테이블의 구조는 남겨두고 데이터만 물리적으로 완전시키고, 사용했던 공간 할당 해제하지 않기 위해 사용하는 명령어**

```sql
truncate table ~;  / truncate table ~ reuse storage;
```

**view**

논리적 테이블, table에 대한 window



**Simple View**

DML이 가능한 뷰 (base table의 not null 컬럼 모두 포함, 표현식 X, 그룹핑 X, rowid X, rownum X)



**Complex View**

DML이 불가능한 뷰 (2개 이상의 테이블로부터 join 포함, 그룹핑, 함수 표현식 등이 포함된 경우)



**View 사용 목적**

보안, 간결한 sql 사용

```sql
create [or replace ] [force|noforce] view 뷰이름 
as 
  select ~
  from ~
  [where ~]
  [group by ~]
  [having ~]
  [order by ~]
  [with check option]  ---체크 제약 조건
  [with read only]  --read only 제약조건
```



**user_views, all_views, dba_views** 

text 컬럼

alter view 구문 X

**drop view 뷰이름**

테이블에 영향을 주지 않습니다.



**테이블을 삭제하면**

구조, 데이터, 제약조건, 인덱스

테이블에 대한 view가 존재하는데.. 테이블이 삭제(drop)되면 뷰는 status는 invalid상태로 변경되어 사용 불가

**index**

검색속도를 향상(select 수행 성능향상)을 위해서 사용하는 객체

**b*tree index**

root node - branch node - leaf node (컬럼값rowid형태로 인덱스 엔트리들이 저장됨, 컬럼값의 오름차순)

**bitmap index**

**단일 컬럼 인덱스**

**복합 컬럼 인텍스**

**function based index** 

컬럼표현식의 결과값으로 인덱스 생성



```sql
create index ~ on 테이블(컬럼 [desc]);
alter index ~ on 테이블(컬럼....);
drop index ~ ;
```



**Sequence**  

최소값 ~ 최대값 범위내에서 설정된 중감값에 따라 정수를 생성 객체

```sql
create sequence ~
[start with ~]
[increment by ~]
[minvalue ~ | nominvalue]
[maxvalue ~ | nomaxvalue]
[cache n | nocache]
[cycle | nocycle];
```



**alter sequence ~** 

로 변경 못하는 속성은 start with

drop sequence~;

**synonym **

'schema.객체@dblink명' 처럼 긴 객체이름을 간결하게 줄여서 쓰려면 

**create synonym** 

for schema.객체@dblink명;



**데이터베이스에 connect하려면**

대상 데이터베이스에 user명이 등록되어 있어야 하며, 인증방식도 정의되어 있어야한다

create session권한이 있어야합니다.



```sql
create user ~     --권한은 DBA(sys, system , drop user~로 삭제없음)
identified by 비밀번호
[default tablespace ~]
[temp tablespace ~]
[tablespace quota XXM]
[profile ~]
[consumer group ~]

```

권한 - 시스템 권한 - DBA

​			객체권한 --객체의 소유자, DBA



grant 권한 .... to user 명 ..... role명 ......public;

**role?** 

특정 업무, 직무와 연관된 권한들을 그룹핑한 것

```sql
revoke 권한,...from user명,..., role명,...public;
```

**객체 권한 부여** 

```sql
grant 권한,...on 객체[(컬럼,...)] to user명,..., role명,...public;
grant 권한,...on 객체[(컬럼,...)] from user명,..., role명,...public;
```

**role 생성 권한  --DBA**

1. create role ~ ;
2. grant 권한,.... to 롤명;
3. grant 롤,..to user명,..., role명,...public;



#############JDBC프로그래밍 단계############

0. 연결할 데이터베이스의 driver class 클래스 (~.jar)를 
   - 운영체제의 환경변수 classpath에 추가
   - JDK또는 JRE의 라이브러리 검색 위치중에 외부 확장 라이브러리 저장위치 (%JAVA_HOME%jre/lib/ext)
   - 이클립스(IDE)에서 프로젝트의 bulid path>configure build path>library> add external jar......추가
   
1. import java.sql.*; --JDBC API import 합니다.

2. DriverClass 로딩

   ```java
   try{
       Class.forNmae(" "); //oracle.jdbc.OracleDriver
       
   }catch(ClassNotFoundException e) {
       
   }
   ```

   

3. Connection 객체 생성
      로딩된 드라이버 클래스의 static 멤버 객체의 DriverManager.getConnection( dburl, user , pwd ) 이용해서
      DB에 connect합니다.
      DB에 세션 생성되고, 세션이 리턴됩니다. => java.sql.Connection객체로 받습니다.
      Connection 인터페이스에 주요 메소드 : close(), createStatement(), prepareStatement(), callableStatement(), setAutoCommit(false), commit(), rollback(), setSavepoint(),..

4. SQL 실행 대행 객체 Statement 객체 생성
      **Statement** - 완전한 sql문장을 문자열로 전송하므로 매번 hard parsing을 수행합니다.
      **PreparedStatement** - sql문장중에서 변경되는 부분들을 ? (index 파라미터)로 설정해서 미리 sql을 전송하고, 실행할때마다 값만 전송해서 실행(soft parsing수행될 확률이 높습니다.)
      **CallableStatement** - DB에 저장되어 있는 procedure, function을 호출해서 결과를 받을때

5. SQL문 실행

   executeQuery() -- select문장, ResultSet 객체 리턴

   executeUpdate() -- DML문은 int(변경된 행수) 리턴, DDL, DCL문

   execute() -- select문 , DML문 , boolean 리턴(true 일때는 select수행, false)

   

6. select 수행결과 처리

   ```java
   while(rs.next()) {
        rs.getInt(컬럼position | "컬럼명"),
        rs.getDouble(컬럼position | "컬럼명"),...
        rs.getString(컬럼position | "컬럼명"),
        rs.getDate(컬럼position | "컬럼명"),
         ...
      }
   ```

7. SQLException 예외 처리

8. 사용 자원 (Connection, Statement, ResultSet)들 반납 close() ---> 예외처리 필요함

   소스코드에 db연결정보를 hard coding하는것은 보안상..문제가 되므로 보안 폴더에 

   ```java
   Properties prop = new Properties();
   prop.load(new FileInputStream("경로/이름.."));
   String value = prop.getProperty("key");
   ```

   

   

   

   ## Tranjection

   ```java
   package lab.java.core;
   
   import java.io.FileInputStream;
   import java.io.IOException;
   import java.sql.Connection;
   import java.sql.DriverManager;
   import java.sql.PreparedStatement;
   import java.sql.ResultSet;
   import java.sql.SQLException;
   import java.sql.Savepoint;
   import java.sql.Statement;
   import java.util.Properties;
   
   public class TranjectionTest { 
   
   	public static void main(String[] args) {
   
   		Connection con = null; //DB연결상태 새션 정보
   		PreparedStatement selectPs = null;
   		PreparedStatement updatePs = null;
   		ResultSet rs =null;
   		String query = "SELECT id, price FROM product "+
   		"WHERE price > ?";
   		String update = "UPDATE product SET price = ? WHERE id = ?";
   
   	
   		try {
   			Properties prop = new Properties();
   			prop.load(new FileInputStream("C:/workspace2/Day13/src/dbinfo.properties"));
   			Class.forName(prop.getProperty("driver"));
   			System.out.println("driver loading 성공");
   			con = DriverManager.getConnection(prop.getProperty("url"),
   					prop.getProperty("user"),
   					prop.getProperty("pwd")	);
   			System.out.println("DB connect 성공");
   			
   			con.setAutoCommit(false);
   			
   			selectPs = con.prepareStatement(query);
   			updatePs = con.prepareStatement(update);
   			
   			selectPs.setInt(1, 100);
   			rs = selectPs.executeQuery();
   			
   			Savepoint save1 = con.setSavepoint();
   			
   		while (rs.next()) {
   			String id = rs.getString("id");
   			int oldPrice = rs.getInt("price");
   			int newPrice = (oldPrice * 2);
   			updatePs.setInt(1, newPrice);
   			updatePs.setString(2, id);
   			updatePs.executeUpdate();
   			System.out.println("New price of "+oldPrice + "is" + newPrice);
   			if(newPrice >= 5000) {
   				con.rollback(save1);
   				
   				
   				
   				}
   			
   		}//while end
   		
   		
   		
   		
   		
   			
   		System.out.println();
   		selectPs.setInt(1, 100);
   		rs = selectPs.executeQuery();
   		
   		Savepoint save2 = con.setSavepoint();
   		
   		while (rs.next()) {
   			String id = rs.getString("id");
   			int oldPrice = rs.getInt("price");
   			int newPrice = (oldPrice * 2);
   			updatePs.setInt(1, newPrice);
   			updatePs.setString(2, id);
   			updatePs.executeUpdate();
   			System.out.println("New price of is" + newPrice);
   			if(newPrice >= 5000) {
   				con.rollback(save2);
   				
   			}
   			}//while end
   			System.out.println();
   			con.commit();
   				
   				Statement stmt = con.createStatement();
   				rs = stmt.executeQuery("SELECT id, price FROM product");
   				
   				System.out.println();
   				while(rs.next()) {
   					String id = rs.getString("id");
   					int price = rs.getInt("price");
   					System.out.println("id : "+id + ", price: "+ price);
   	
   			
   		}	
   			
   		}catch(ClassNotFoundException e) {
   			System.out.println("dirver 없음");
   		} catch(SQLException e) {
   			System.out.println(e.getMessage());
   			//연결실패
   		} catch(IOException e) {
   			System.out.println(e.getMessage());
   		}
   		
   		finally{
   			try {
   				if(rs != null)rs.close();
   				if(selectPs != null)selectPs.close();
   				if(selectPs != null)updatePs.close();
   				if(con != null)con.close();
   				
   			}
   			catch(Exception e) {
   				e.printStackTrace();
   			}
   		}
   	}
   }
   
   
   
   ```

   





sql 실습(도서조회시스템)

```sql

drop table book purge;


create table Book(
isbn varchar2(5) constraint book_isbn_pk primary key,
category varchar2(15), 

title varchar2(50),
author varchar2(30),
price number(6),
descript varchar2(500)
);

--------테이블 생성----------

insert into book (isbn, title, category, price, descript)
values ('M0001','Cooking Light','living, cooking', 15000, 'America Cooking');



insert into book (isbn, title, author, price)
values ('N0001', 'The Confession', 'Grisham, John', 10500);




commit;
```



## 연습) 도서정보 조회(JDBC)



```java
package lab.jdbc.entity;

public class Book {

	private String isbn;
	private String category;

	private String title;
	private String author;
	private int price;
	private String descript;

	public Book() {
		super();
	}

	public Book(String isbn, String title, int price) {
		super();
		this.isbn = isbn;
		this.title = title;
		this.price = price;
	}

	public Book(String isbn, String title, String author, int price) {

		this(isbn, title, price);
		this.author = author;

	}

	public Book(String isbn, String category, String title, String author, int price, String descript) {
		this(isbn, title, price);
		this.category = category;
		this.descript = descript;
	}

	public String getIsbn() {
		return isbn;
	}

	public String getCategory() {
		return category;
	}

	public String getTitle() {
		return title;
	}

	public String getAuthor() {
		return author;
	}

	public int getPrice() {
		return price;
	}

	public String getDescript() {
		return descript;
	}

	public void setPrice(int price) {
		this.price = price;
	}

	public void setDescript(String descript) {
		this.descript = descript;
	}

	public void setIsbn(String isbn) {
		this.isbn = isbn;
	}

	public void setCategory(String category) {
		this.category = category;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	@Override
	public String toString() {
		String info = null;
		if (isbn.startsWith("N")) {
			info = "소설 [isbn=" + isbn + ", title=" + title + ", author=" + author + ", price=" + price + " ]";
		} else {
			info = "잡지[isbn=" + isbn + ", category=" + category + ", title=" + title + ", author=" + author + ", price="
					+ price + ", descript=" + descript + "]";
		}
		return info;
	}

}

```





```java
package lab.jdbc.biz;

import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Properties;

import lab.jdbc.entity.Book;
import lab.jdbc.util.BookUtil;

public class Bookbiz {

	private ArrayList<Book> books;

	public Bookbiz() {
		super();

	}

	public Connection dbCon() {
		Connection con = null;
		try {
			Properties prop = new Properties();
			prop.load(new FileInputStream("C:/workspace2/Day13/src/dbinfo.properties"));

			Class.forName(prop.getProperty("driver"));
			// System.out.println("driver loading 성공");
			con = DriverManager.getConnection(prop.getProperty("url"), prop.getProperty("user"),

					prop.getProperty("pwd"));
			// System.out.println("DB connect 성공");

		} catch (Exception e) {
			e.printStackTrace();
		}

		return con;
	}

	public void dbClose(Connection con, Statement stat, ResultSet rs) {

		try {
			if (rs != null)
				stat.close();
			if (stat != null)
				stat.close();
			if (con != null)
				con.close();
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	public void printAllBooks() {
		Connection con = null;
		Statement stat = null;
		String sql = "select * from book";
		ResultSet rs = null;

		try {
			con = dbCon();
			stat = con.createStatement();
			rs = stat.executeQuery(sql);
			BookUtil.printHeader();
			while (rs.next()) {
				Book book = new Book();
				book.setIsbn(rs.getString("isbn"));
				book.setTitle(rs.getString("title"));
				book.setAuthor(rs.getString("author"));
				book.setPrice(rs.getInt("price"));
				book.setCategory(rs.getString("category"));
				book.setDescript(rs.getString("descript"));
				System.out.println(book);

			}
			BookUtil.printTail();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);

		}

	}

	public void printAllNovels() {
		Connection con = null;
		Statement stat = null;
		String sql = "select * from book where isbn like 'N%'";
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.createStatement();
			rs = stat.executeQuery(sql);
			BookUtil.printHeader();
			while (rs.next()) {
				Book book = new Book();
				book.setIsbn(rs.getString("isbn"));
				book.setTitle(rs.getString("title"));
				book.setAuthor(rs.getString("author"));
				book.setPrice(rs.getInt("price"));
				System.out.println(book);

			}
			BookUtil.printTail();

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);

		}

	}

	public void printAllMagazine() {
		Connection con = null;
		Statement stat = null;
		String sql = "select * from book where isbn like 'M%'";
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.createStatement();
			rs = stat.executeQuery(sql);
			BookUtil.printHeader();
			while (rs.next()) {
				Book book = new Book();
				book.setIsbn(rs.getString("isbn"));
				book.setTitle(rs.getString("title"));
				book.setCategory(rs.getString("category"));

				book.setPrice(rs.getInt("price"));
				book.setDescript(rs.getString("descript"));

				System.out.println(book);

			}
			BookUtil.printTail();

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);

		}

	}

	public void printMagazoneOneYearSubscription() {
		Connection con = null;
		Statement stat = null;
		String sql = "select * from book where isbn like 'M%'";
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.createStatement();
			rs = stat.executeQuery(sql);
			System.out.println("-----------");
			int num = 1;
			while (rs.next()) {
				System.out.println(num++ + ", " + rs.getString("title") + " : " + rs.getInt("price") * 12 + "원");

			}
			System.out.println("--------------------");
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);

		}

	}

	public ArrayList<Book> serchNovelByAuthor(String author) {
		ArrayList<Book> searchBooks = new ArrayList();
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "select * from book where isbn like 'N%' and author like ?";
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setString(1, "%" + author + "%");
			rs = stat.executeQuery();
			while (rs.next()) {
				Book book = new Book();
				book.setIsbn(rs.getString("isbn"));
				book.setTitle(rs.getString("title"));
				book.setAuthor(rs.getString("author"));
				book.setPrice(rs.getInt("price"));
				searchBooks.add(book);

			}

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);

		}
		return searchBooks;

	}

	public ArrayList<Book> serchNovelByPrice(int minPrice, int maxPrice) {
		ArrayList<Book> searchBooks = new ArrayList();
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "select * from book where isbn like 'N%' and price between ? and ?";
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setInt(1, minPrice);
			stat.setInt(2, maxPrice);

			rs = stat.executeQuery();
			while (rs.next()) {
				Book book = new Book();
				book.setIsbn(rs.getString("isbn"));
				book.setTitle(rs.getString("title"));
				book.setAuthor(rs.getString("author"));
				book.setPrice(rs.getInt("price"));
				searchBooks.add(book);

			}

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);

		}
		return searchBooks;

	}

	public int inserBook(Book newBook) {
		int rows = 0;
		Connection con = null;
		PreparedStatement stat = null;
		String novel = "insert into book(isbn, title,author,price)  values(?,?,?,?)";
		String magazine = "insert into book(isbn, title,price,category,descript)  values(?,?,?,?,?)";
		try {
			con = dbCon();
			if (newBook.getIsbn().startsWith("N")) {
				stat = con.prepareStatement(novel);
				stat.setString(1, newBook.getIsbn());
				stat.setString(2, newBook.getTitle());
				stat.setString(3, newBook.getAuthor());
				stat.setInt(4, newBook.getPrice());

			} else {

				stat = con.prepareStatement(magazine);
				stat.setString(1, newBook.getIsbn());
				stat.setString(2, newBook.getTitle());
				stat.setInt(3, newBook.getPrice());
				stat.setString(4, newBook.getCategory());
				stat.setString(5, newBook.getDescript());

			}
			rows = stat.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, null);

		}
		return rows;
	}

	public int updateBook(Book modifyBook) {
		int rows = 0;
		Connection con = null;
		PreparedStatement stat = null;
		String novel = "update book set price =? where isbn = ?";
		String magazine = "update book set price =? , descript = ? where isbn = ?";
		try {
			con = dbCon();
			if (modifyBook.getIsbn().startsWith("N")) {
				stat = con.prepareStatement(novel);
				stat.setString(2, modifyBook.getIsbn());
				stat.setInt(1, modifyBook.getPrice());

			} else {

				stat = con.prepareStatement(magazine);
				stat.setString(3, modifyBook.getIsbn());
				stat.setInt(1, modifyBook.getPrice());
				stat.setString(2, modifyBook.getDescript());

			}
			rows = stat.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, null);

		}
		return rows;

	}

	public int deleteBook(String isbn) {

		int rows = 0;
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "delete from book where isbn = ?";
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setString(1, isbn);
			rows = stat.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, null);

		}
		return rows;

	}

}

```



```java
package lab.jdbc.util;

import java.util.Scanner;

public class BookUtil {
   public static String getUerInput() {
	   Scanner input = new Scanner(System.in);
	   return input.nextLine();
   }
   public static void printHeader() {
	   System.out.println("-------------------------------------------- 도서 정보 --------------------------------------------");
   }
   public static void printTail() {
	   System.out.println("------------------------------------------------------------------------------------------------");
   }
}

```



```java
package lab.jdbc.test;

import java.util.ArrayList;

import lab.jdbc.biz.Bookbiz;
import lab.jdbc.entity.Book;
import lab.jdbc.util.BookUtil;

public class BookTest {

	public static void main(String[] args) {
		Bookbiz biz = new Bookbiz();
		ArrayList<Book> books = null;
		Book book = null;
		while (true) {
			printMenu();
			System.out.print("## 메뉴 입력:");
			String menu = BookUtil.getUerInput();
			if (menu.equals("0")) {
				System.out.println("------------------------");
				System.out.println("프로그램을 종료합니다. Bye~");
				System.out.println("------------------------");
				break;
			}
			switch (menu) {
			case "1":
				biz.printAllBooks();
				break;
			case "2":
				biz.printAllMagazine();
				break;
			case "3":
				biz.printAllNovels();
				break;
			case "4":
				biz.printMagazoneOneYearSubscription();
				break;
			case "5":
				System.out.print("> 검색할 저자명을 입력하세요:");
				String author = BookUtil.getUerInput();
				books = biz.serchNovelByAuthor(author.trim());
				BookUtil.printHeader();
				for (Book b : books)
					System.out.println(b);
				BookUtil.printTail();
				break;
			case "6":
				System.out.print("> 검색할 소설 가격의  최소값을 입력하세요:");
				int minPrice = Integer.parseInt(BookUtil.getUerInput());
				System.out.print("> 검색할 소설 가격의 최대값을 입력하세요:");
				int maxPrice = Integer.parseInt(BookUtil.getUerInput());
				books = biz.serchNovelByPrice(minPrice, maxPrice);
				BookUtil.printHeader();
				for (Book b : books)
					System.out.println(b);
				BookUtil.printTail();
				break;

			case "7":
				book = new Book();
				System.out.print(">ISBN 입력하시오 : ");
				book.setIsbn(BookUtil.getUerInput());
				System.out.print(">책 제목을 입력하세요 : ");
				book.setTitle(BookUtil.getUerInput());
				System.out.print(">저자를 입력하시오 : ");
				book.setAuthor(BookUtil.getUerInput());
				System.out.print(">가격 입력하시오 : ");
				book.setPrice(Integer.parseInt(BookUtil.getUerInput()));
				System.out.print(">카테고리를 입력하시오 : ");
				book.setCategory(BookUtil.getUerInput());
				System.out.print(">설명을 입력하시오 : ");
				book.setDescript(BookUtil.getUerInput());

				if (biz.inserBook(book) > 0) {
					System.out.println("새 책 정보 추가 완료!!!!");
				}
				break;

			case "8":
				book = new Book();
				System.out.print(">ISBN 입력하시오 : ");
				book.setIsbn(BookUtil.getUerInput());
				System.out.print(">가격 입력하시오 : ");
				book.setPrice(Integer.parseInt(BookUtil.getUerInput()));
				System.out.print(">설명을 입력하시오 : ");
				book.setDescript(BookUtil.getUerInput());
				if (biz.updateBook(book) > 0) {
					System.out.println("새 책 정보 수정 완료!!!!");
				}
				break;

			case "9":
				System.out.print(">ISBN 입력하시오  : ");
				String isbn = BookUtil.getUerInput();
				if (biz.deleteBook(isbn) > 0) {
					System.out.println("새 책 정보 삭제 완료!!!!");
				}
				break;
			}
		}

	}

	public static void printMenu() {
		System.out.println("===<< 도서 정보 프로그램 >>===");
		System.out.println("1. 전체 도서 정보 조회");
		System.out.println("2. 전체 잡지 조회");
		System.out.println("3. 전체 소설 조회");
		System.out.println("4. 잡지 연간 구독료 조회");
		System.out.println("5. 소설 저자명 검색");
		System.out.println("6. 소설 가격 검색(최소값 ~ 최대값)");
		System.out.println("7. 새 책정보 추가");
		System.out.println("8. 책정보 수정");
		System.out.println("9. 책정보 삭제");
		System.out.println("0. 시스템 종료");
		System.out.println("========================");

	}

}

```

