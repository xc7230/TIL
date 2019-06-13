## JDBC

=========성적처리 DB연동====================





```sql
create table student (
studentno  varchar2(5)	constraint student_pk primary key,
studentName  varchar2(15)	not null,
c	number(3),
linux	number(3),
java	number(3),
careerYears	number(2),
internYn	char(1) check(internYn in('Y', 'N'))
);

alter table student add (average number(5,2), 
pass char(1) check(pass in('Y', 'N')));

drop table student purge;


alter table student modify (
c	number(3) default 0,

linux	number(3) default 0,

java	number(3) default 0
);

select * from student;


```







**db에 연결할 Properties 파일 만들기** 

**dbinfo.Properties** 

```java
driver = oracle.jdbc.OracleDriver
url = jdbc:oracle:thin:@localhost:1521:orcl
user = scott
pwd = oracle
```









**메서드 만들기**

```sql
package lab.jdbc.entity;

public class Student {

	private String studentNo;     //학생번호
	private String studentName;   //학생이름
	private int c;   //c점수
	private int linux; // linux 점수
	private int java;  // java 점수
	private int careerYears;  //경력년수
	private String internYn;  //인턴경험
	private String pass;  //합격여부
	private double average; //점수 평균

	public Student() {
		super();
	}

	public Student(String studentNo, String studentName, int c, int linux, int java, int careerYears, String internYn,
			String pass, double average) {
		super();
		this.studentNo = studentNo;
		this.studentName = studentName;
		this.c = c;
		this.linux = linux;
		this.java = java;
		this.careerYears = careerYears;
		this.internYn = internYn;
		this.pass = pass;
		this.average = average;
	}

	public String getStudentNo() {
		return studentNo;
	}

	public void setStudentNo(String studentNo) {
		this.studentNo = studentNo;
	}

	public String getStudentName() {
		return studentName;
	}

	public void setStudentName(String studentName) {
		this.studentName = studentName;
	}

	public int getC() {
		return c;
	}

	public void setC(int c) {
		this.c = c;
	}

	public int getLinux() {
		return linux;
	}

	public void setLinux(int linux) {
		this.linux = linux;
	}

	public int getJava() {
		return java;
	}

	public void setJava(int java) {
		this.java = java;
	}

	public int getCareerYears() {
		return careerYears;
	}

	public void setCareerYears(int careerYears) {
		this.careerYears = careerYears;
	}

	public String getInternYn() {
		return internYn;
	}

	public void setInternYn(String internYn) {
		this.internYn = internYn;
	}

	public String getPass() {
		return pass;
	}

	public void setPass(String pass) {
		this.pass = pass;
	}

	public double getAverage() {
		return average;
	}

	public void setAverage(double average) {
		this.average = average;
	}

	@Override
	public String toString() {
		StringBuffer info = new StringBuffer();
		info.append(studentNo);
		info.append("  ");
		info.append(studentName);
		info.append("  ");
		if (this.studentNo.startsWith("1")) {
			info.append("신입");
		} else if (this.studentNo.startsWith("2")) {
			info.append("경력");
		}
		if (internYn != null) {
			info.append(internYn);
		} else {
			info.append("\t\t");
		}
		if (careerYears > 0) {
			info.append(careerYears);
		} else {
			info.append("\t\t");
		}
		info.append("  ");
		info.append(c);
		info.append("  ");
		info.append(linux);
		info.append("  ");
		info.append(java);
		info.append("  ");
		info.append((c + java + linux));
		info.append("  ");
		info.append(average);
		info.append("  ");
		if (pass.equalsIgnoreCase("Y")) {
			info.append("합격");
		} else {
			info.append("불합격");
		}

		return info.toString();
	}

}


```



### GradeManager

db에 연결하기

```java
public Connection dbCon() {
		Connection con = null;
		try {
			Properties prop = new Properties();
			prop.load(new FileInputStream("C:/workspace2/Day13/src/dbinfo.properties"));
            //만들어둔dbinfo.Properties 파일을 input한다.
            
            

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
```



Connection  인터페이스는 특정 데이터베이스와의 연결

```java
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
```



```java
	//모든 학생정보 불러오기

		public ArrayList<Student> getAllStudent() {
		ArrayList<Student> students = new ArrayList();
		Connection con = null;
		Statement stat = null;
		String sql = "select * from Student";//sql
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.createStatement();
			rs = stat.executeQuery(sql); //String sql에 입력한 내용을 db에 명령을 내림
			while (rs.next()) {
				Student s1 = new Student();
				s1.setStudentNo(rs.getString("studentNo"));
				s1.setStudentName(rs.getString("studentName"));
				s1.setC(rs.getInt("c"));
				s1.setJava(rs.getInt("java"));
				s1.setLinux(rs.getInt("linux"));
				s1.setCareerYears(rs.getInt("careerYears"));
				s1.setInternYn(rs.getString("internYn"));
				s1.setPass(rs.getString("pass"));
				s1.setAverage(rs.getDouble("average"));
				students.add(s1); //array데이터에 뒤에 s1을 새로 붙인다.
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);
		}
		return students;
	}

```



```java
	//합격한 학생정보만 불러오기
	//grade student는 평균 80점이상
	//new student는 평균 70점이상

		public ArrayList<Student> getPassStudent() {
		ArrayList<Student> students = new ArrayList();
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "select * from Student where pass = ?";  //?는 변수자리
            //값을 지정하려면 set메서드를 통해 입력가능  
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.prepareStatement(sql); //sql에 입력된 값을 계속 써야하기 때문에 prepareStatement를 쓴다.
			stat.setString(1, "Y"); //column pass의 값이 "Y" 인 데이터를 불러온다.
			rs = stat.executeQuery();
			while (rs.next()) {
				Student s1 = new Student();

				s1.setStudentNo(rs.getString("studentNo"));
				s1.setStudentName(rs.getString("studentName"));
				s1.setC(rs.getInt("c"));
				s1.setJava(rs.getInt("java"));
				s1.setLinux(rs.getInt("linux"));
				s1.setCareerYears(rs.getInt("careerYears"));
				s1.setInternYn(rs.getString("internYn"));
				s1.setPass(rs.getString("pass"));
				s1.setAverage(rs.getDouble("average"));
				students.add(s1);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);
		}
		return students;

	}
```







```java

//불합격 학생 조회
public ArrayList<Student> getFailStudent() {

		ArrayList<Student> students = new ArrayList();
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "select * from Student where pass = ?";
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setString(1, "N"); //column pass의 값이 "N" 인 데이터를 불러온다.
			rs = stat.executeQuery();
			while (rs.next()) {
				Student s1 = new Student();

				s1.setStudentNo(rs.getString("studentNo"));
				s1.setStudentName(rs.getString("studentName"));
				s1.setC(rs.getInt("c"));
				s1.setJava(rs.getInt("java"));
				s1.setLinux(rs.getInt("linux"));
				s1.setCareerYears(rs.getInt("careerYears"));
				s1.setInternYn(rs.getString("internYn"));
				s1.setPass(rs.getString("pass"));
				s1.setAverage(rs.getDouble("average"));
				students.add(s1);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);
		}
		return students;

	}
```





```java
	
//수강정보 추가
public int inserteStudent(Student s) {
		int rows = 0;
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "insert into student (studentno, studentname, c, java, linux, careeryears, internyn, average, pass) values (?,?,?,?,?,?,?, ?, ?)";
    //다음 column을 insert 해준다.
    
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setString(1, s.getStudentNo());
			stat.setString(2, s.getStudentName());
			stat.setInt(3, s.getC());
			stat.setInt(4, s.getJava());
			stat.setInt(5, s.getLinux());
			if (s.getStudentNo().startsWith("1")) {
				stat.setString(7, s.getInternYn());
				stat.setInt(6, 0); //만약 getStudentNo 첫번째 숫자가 1이면 6번째 ?(경력)는 0으로 처리한다.
			} else {
				stat.setInt(6, s.getCareerYears());
				stat.setString(7, "N");
			} //그외 6번째 ?에 getCareerYears을 넣어주고 7번째 ?(internyn)에 N을처리 한다.
			double avg = (s.getC() + s.getJava() + s.getLinux()) / 3.0;
			stat.setDouble(8, Double.parseDouble(String.format("%.2f", avg)));
			if (s.getStudentNo().startsWith("1") && avg >= 70) {
				stat.setString(9, "Y"); //getStudentNo가 1이고, 평균이 70이상이면 9번째 ?(pass) 에 "Y"를 넣어준다.
			} else if (s.getStudentNo().startsWith("2") && avg >= 80) {
				stat.setString(9, "Y"); //getStudentNo가 2이고, 평균이 80이상이면 9번째 ?(pass) 에 "Y"를 넣어준다.
			} else {
				stat.setString(9, "N");
			}
			rows = stat.executeUpdate();  //executeUpdate :  INSERT, UPDATE, DELETE 등 (DML), CREATE, DROP 등(DDL)문들을 실행하는데 사용

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, null);
		}
		return rows;
	}
```







```java
	
//학생 정보 수정

public int updateStudent(Student s) {
		int rows = 0;
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "update student set c=?, java=?, linux=?, careeryears=?, internyn=? , average=? , pass=? where studentno=?  "; 
    //db 에서 update는 데이터 수정을 의미한다.
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setString(8, s.getStudentNo());
			stat.setInt(1, s.getC());
			stat.setInt(2, s.getJava());
			stat.setInt(3, s.getLinux());
			if (s.getStudentNo().startsWith("1")) {
				stat.setInt(4, 0);
				stat.setString(5, s.getInternYn());
			} else {
				stat.setInt(4, s.getCareerYears());
				stat.setString(5, "N");
			}
			double avg = (s.getC() + s.getJava() + s.getLinux()) / 3.0;
			stat.setDouble(6, Double.parseDouble(String.format("%.2f", avg)));
			if (s.getStudentNo().startsWith("1") && avg >= 70.0) {
				stat.setString(7, "Y");
			} else if (s.getStudentNo().startsWith("2") && avg >= 80.0) {
				stat.setString(7, "Y");
			} else {
				stat.setString(7, "N");
			}
			rows = stat.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, null);
		}
		return rows;
	}
```





```java
	

//학생정보 삭제
public int deleteStudent(String sno) {

		int rows = 0;
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "delete from student where studentNo = ?";
    //데이터 삭제
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setString(1, sno);
			rows = stat.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, null);

		}
		return rows;

	}
```







```java
//학생번호로 해당 자료 찾기

public Student searchStudent(String sno) {
		Student s1 = new Student();

		Connection con = null;
		PreparedStatement stat = null;
		String sql = "select * from Student where studentno like ?";
    //학생번호가 ?이면 자료를 불러온다.
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setString(1, "%" + sno + "%");
			rs = stat.executeQuery();
			while (rs.next()) {
				s1.setStudentNo(rs.getString("studentNo"));
				s1.setStudentName(rs.getString("studentName"));
				s1.setC(rs.getInt("c"));
				s1.setJava(rs.getInt("java"));
				s1.setLinux(rs.getInt("linux"));
				s1.setCareerYears(rs.getInt("careerYears"));
				s1.setInternYn(rs.getString("internYn"));
				s1.setPass(rs.getString("pass"));
				s1.setAverage(rs.getDouble("average"));
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);
		}
		return s1;

	}
```





```java
//일력 메서드를 만든다.


package lab.jdbc.util;

import java.util.Scanner;

public class StudentUtil {
	
	   public static String getUerInput() {
		   Scanner input = new Scanner(System.in);
		   return input.nextLine();
	   }
	   public static void printHead() {
			   System.out.println("=======================================================================================");
			   System.out.println("사번      이름   신입/경력  인턴여부  경력년수  C   Linux   Java   총점   평균   합격여부");;
			   System.out.println("=======================================================================================");	 
			   }
	   public static void printTail() {
		   System.out.println("=======================================================================================");	   }

}

```









```java
package lab.jdbc.test;

import java.util.ArrayList;

import lab.jdbc.biz.GradeManager;
import lab.jdbc.entity.Student;
import lab.jdbc.util.StudentUtil;

public class StudentTest {

	public static void main(String[] args) {
		GradeManager manager = new GradeManager();
		ArrayList<Student> students = null;
		Student std = null;
		while (true) {
			printMenu();
			System.out.print("## 메뉴 입력:");
			String menu = StudentUtil.getUerInput();
			if (menu.equals("9")) {
				System.out.println("------------------------");
				System.out.println("프로그램을 종료합니다. Bye~");
				System.out.println("------------------------");
				break;
			}
			switch (menu) {
			case "1":  //전체사원 출력
				students = manager.getAllStudent(); //getAllStudent을 불러온다.
				StudentUtil.printHead();
				for (Student s : students) {
					System.out.println(s);
				}
				StudentUtil.printTail();
				break; 
			case "2":  //합격한 학생 출력
				students = manager.getPassStudent();
				StudentUtil.printHead();
				for (Student s : students) {
					System.out.println(s);
				}
				StudentUtil.printTail();
				break;
			case "3":  //불합격한 학생 출력
				students = manager.getFailStudent();
				StudentUtil.printHead();
				for (Student s : students) {
					System.out.println(s);
				}
				StudentUtil.printTail();
				break;

			case "4":  //자료 추가
				std = new Student();
				System.out.print("> 사번 입력하세요:");
				std.setStudentNo(StudentUtil.getUerInput());
				System.out.print("> 이름을 입력하세요:");
				std.setStudentName(StudentUtil.getUerInput());
				System.out.print("> C 점수를 입력하세요:");
				std.setC(Integer.parseInt(StudentUtil.getUerInput()));
				System.out.print("> JAVA 점수를 입력하세요:");
				std.setJava(Integer.parseInt(StudentUtil.getUerInput()));
				System.out.print("> Linux 점수를 입력하세요:");
				std.setLinux(Integer.parseInt(StudentUtil.getUerInput()));
				if (std.getStudentNo().startsWith("1")) {
					System.out.print("> 인턴여부(Y/N)을 입력하세요:");
					std.setInternYn(StudentUtil.getUerInput());
				} else {
					System.out.print("> 경력년수을 입력하세요:");
								              
                           std.setCareerYears(Integer.parseInt(StudentUtil.getUerInput()));
				
                  }
				if (manager.inserteStudent(std) > 0) {
					System.out.println("수강생 정보 추가하였습니다.");
				}
				break;

			case "5":  //데이터 변경
				std = new Student();
				System.out.print("> 변경할 사번 입력하세요:");
				std.setStudentNo(StudentUtil.getUerInput());

				System.out.print("> C 점수를 입력하세요:");
				std.setC(Integer.parseInt(StudentUtil.getUerInput()));
				System.out.print("> JAVA 점수를 입력하세요:");
				std.setJava(Integer.parseInt(StudentUtil.getUerInput()));
				System.out.print("> Linux 점수를 입력하세요:");
				std.setLinux(Integer.parseInt(StudentUtil.getUerInput()));
				if (std.getStudentNo().startsWith("1")) {
					System.out.print("> 인턴여부(Y/N)을 입력하세요:");
					std.setInternYn(StudentUtil.getUerInput());
				} else {
					System.out.print("> 경력년수을 입력하세요:");
					std.setCareerYears(Integer.parseInt(StudentUtil.getUerInput()));
				}
				if (manager.updateStudent(std) > 0) {
					System.out.println("수강생 정보 수정하였습니다.");
				}
				break;
			case "6":
				System.out.print("> 삭제할 사번 입력하세요:");
				String sno = StudentUtil.getUerInput();
				if (manager.deleteStudent(sno) > 0) {
					System.out.println("수강생 정보 삭제하였습니다.");
				}
				break;
			case "7":
				System.out.print("> 검색할 사번 입력하세요:");
				sno = StudentUtil.getUerInput();
				std = manager.searchStudent(sno);
				if (std != null) {
					StudentUtil.printHead();
					System.out.println(std);
					StudentUtil.printTail();
				}
				break;

			}// switch end
		} // while end

	}

    //프린트 메뉴 출력
	public static void printMenu() {
		System.out.println("===<< 성적관리 시스템 메뉴 >>===");
		System.out.println("1. 전체 수강생 조회");
		System.out.println("2. 합격 수강생 조회");
		System.out.println("3. 불합격 수강생 조회");
		System.out.println("4. 수강생 정보 추가");
		System.out.println("5. 수강생 정보 수정");
		System.out.println("6. 수강생 정보 삭제");
		System.out.println("7. 학번으로 수강생 정보 조회");
		System.out.println("9. 시스템 종료");
		System.out.println("===============================");

	}

}

```

