자바 기반의 웹 어플리케이션에서 JSP의 역할 - View (사용자에게 제공되는 content, 입력 페이지)

정적 지시자 <% page .... %> <%@ include .. %> <% tagilb ... %>

동적 태그 <jsp:include .../><jsp:forward..../>

<jsp:setProperty ..../><jsp:getProperty........>



자바 코드와 관련된 JSP요소

<%!



변수 선언 초기화;

메서드 정의



%>

<%

​	자바 실행 문장;

%>



<%= 출력내용 %> 는 <% out.print(출력내용); %>와 동일



익스프레션 언어(**expression language**) :  자바 코드를 대신할 새로운 언어

•{로 시작해서} 로 끝나고, 그 안에 데이터 이름이나 간단한 식을 쓸 수 있다.

액션(**action**)

•**XML** 태그 형태로 기술되며, 자바의 **if** 문**, for** 문, **switch** 문에 해당하는 태그들이 있다.

스크립팅 요소의 문법

스크립팅 요소(**scripting elements**)란 다음 세가지 문법을 말한다.

•스크립틀릿(**scriptlet**)

•익스프레션(**expression**)

•선언부(**declaration**)

스크립틀릿(**scriptlet**)은 <%로 시작해서 %> 로 끝나고, 그 사이 자바 명령문이 들어갈 수 있다. 





지시자의 문법

지시자(**directive**)는 **JSP**의 다른 문법들(스크립팅 요소, 익스프레션 언어, 액션)과는 다른 목적으로 사용된다.

웹 브라우저로부터의 요청을 처리하는 것이 아니라, 웹 컨테이너가 **JSP** 페이지를 서블릿 클래스로 변환할 때 필요한 정보들을 기술하는 역할을 한다.

**JSP** 페이지에 사용할 수 있는 지시자의 종류

•**page** 지시자

•**include** 지시자

•**taglib** 지시자





web.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd" id="WebApp_ID" version="3.0">
  <display-name>web2</display-name>
  <welcome-file-list>
    <welcome-file>index.html</welcome-file>
    <welcome-file>index.htm</welcome-file>
    <welcome-file>index.jsp</welcome-file>
    <welcome-file>login.jsp</welcome-file>
  </welcome-file-list>
</web-app>
```



db.properties

```
driver=oracle.jdbc.OracleDriver
url=jdbc:oracle:thin:@localhost:1521:orcl
user=scott
pwd=oracle
```





userinfoDB만들기

```sql
create table userinfo(
userid varchar2(15) primary key,
userpwd varchar2(15),
username varchar2(20),
phone varchar2(15),
email varchar2(15),
birth date
, address varchar2(100)
);

insert into userinfo (userid, userpwd, username) values('admin' , 'a1234', '관리자');
commit;

alter table userinfo add (job varchar2(20));
```







login.jsp

```jsp
<%@ page contentType="text/html;charset = utf-8" pageEncoding="utf-8" %>

<!DOCTYPE html>
<html>
  <head>
    <meta  charset="utf-8">
    <title>부분페이지 동적 갱신</title> 
</head>
<body>
 <h3>부분페이지 갱신, POST요청, XML응답처리</h3>
    <table border="1">
      <tr><td colspan="2" align="center"><font size=15><b>우리회사</b></font></td></tr>
      <tr>
         <td><form action="Login" method ="post">
               <div id="confirmed">
                 <table>
                    <tr>
                      <td>아이디</td>
                      <td><input type="text" id="userid" name = "userid" size="15" maxlength="12"/></td>
                    </tr>
                    <tr>
                      <td>비밀번호</td>
                      <td><input type="password" id="userpwd" name="userpwd" size="15" maxlength="12"/></td>
                    </tr>
                    <tr><td colspan="2" align="center">
                        <input type="submit" id="login" value="로그인" /></td>
                    </tr>
                </table>
              </div>
             </form>
         </td>
         <td width="400"><img src="cat.jpg"></td>
      </tr>
      <tr><td colspan="2" align="center">찾아오시는길 |회사소개|정보보호정책</td></tr>
    </table>
</body>
</html>
```





loginFail.jsp

```jsp
<%@ page contentType="text/html;charset = utf-8" pageEncoding="utf-8" %>

<!DOCTYPE html>
<html>
<head>
<meta  charset="utf-8">
<style>
p{color:blue;}

</style>
<title>loginFail.jsp</title>
</head>
<body>
<p> 아이디가 존재하지 않거나 비밀번호가 일치하지 않습니다.</p>
<a href="./login.jsp">다시 로그인 하기</a>
<br>
</body>
</html>
```





loginSuccess.jsp

```jsp
<%@ page contentType="text/html;charset = utf-8" pageEncoding="utf-8" %>

<!DOCTYPE html>
<html>
<head>
<meta  charset="utf-8">
<style>
p{color:red;}

</style>
<title>loginSuccess.jsp</title>
</head>
<body>
<p> ${userid}님 환영합니다.</p>

<br>
</body>
</html>
```





LoginDAO

```java
package lab.web.model;

import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;



public class LoginDAO {	
	public Connection dbCon() {
		Connection con = null;
		try {
			Properties prop = new Properties();
			prop.load(new FileInputStream("C:/workspace2/web2/WebContent/WEB-INF/db.properties"));
			Class.forName(prop.getProperty("driver"));
			con = DriverManager.getConnection(prop.getProperty("url")
					, prop.getProperty("user"), prop.getProperty("pwd"));
		} catch(Exception e) {
			e.printStackTrace();
		}
		return con;
		
	}



public void dbClose(Connection con, Statement stat, ResultSet rs) {
	try {
		if(rs!=null) rs.close();
		if(stat!=null) stat.close();
		if(con!=null) con.close();
	} catch(Exception e) {
		e.printStackTrace();
	}
}


public boolean loginProc(String uid, String upwd) {
	boolean success = false;
	Connection con = null;
	PreparedStatement stat = null;
	String sql = "select*from userinfo where userid=? and userpwd=?";
	ResultSet rs = null;
	try {
		con = dbCon();
		stat = con.prepareStatement(sql);
		stat.setString(1, uid);
		stat.setString(2, upwd);
		rs = stat.executeQuery();
		if(rs.next()) {
			success = true;
		}

		
	}catch(Exception e) {
		e.printStackTrace();
	}finally {
		dbClose(con, stat, rs);
	}
	return success;
}
}

```





LoginServlet.java

```java
package lab.web.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import lab.web.model.LoginDAO;


@WebServlet("/Login")
public class LoginServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       

    public LoginServlet() {

        
    }


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		response.setContentType("text/html;charset=utf-8");
		response.sendRedirect("./login.jsp");
	
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		String uid = request.getParameter("userid");
		String upwd = request.getParameter("userpwd");
		LoginDAO dao = new LoginDAO();
		ServletContext sc = request.getServletContext();
		RequestDispatcher rd =null;
		if(dao.loginProc(uid, upwd)) {
			rd = sc.getRequestDispatcher("/loginSuccess.jsp");
			request.setAttribute("userid", uid);
			rd.forward(request, response);
		} else {
			rd =sc.getRequestDispatcher("/loginFail.jsp");
			rd.forward(request, response);
		}
		
	
	}

}

```



