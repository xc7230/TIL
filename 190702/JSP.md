# 액션태그



include태그 

JSP 수행 결과 내에 다른 자원의 내용 또는 수행 결과를 포함합니다.

```jsp
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%request.setCharacterEncoding("utf-8"); %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
</head>
<body>
<h3>include 지시자 예제</h3>
<table border="1">
<tr>
<td colspan="2" align ="center">
<jsp:include page="header.jsp" >
<jsp:param name = "company" value="인공지능기반 매칭서비스" />
</jsp:include>
</td></tr>
<tr>
	<td>
	<jsp:include page="menu.jsp" />
	</td>
	<td width ="400"><img src="cat.jpg"></td>
	</tr>
	<tr>
	<td colspan = "2" align ="center">
	<jsp:include page="footer.jsp">
	<jsp:param name = "address" value="서울 광화문" />
	
	</jsp:include>
	</td></tr>

</table>
</body>
</html>
```





```jsp
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="EUC-KR"%>
 
<style>
h3 {text-align: center;}
</style>
<h3>${param.company }</h3>

```



EL의 연산자 점검

```jsp
<%@ page contentType="text/html;charset = utf-8" pageEncoding="utf-8" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>EL테스트</title>
</head>
<body>
<h2>EL의 연산자들</h2>
<hr>
\${200+100} : ${200+100} <br>
\${200-100} : ${200-100} <br>
\${200/100} : ${200/100} <br>
\${200>100} : ${200>100} <br>
\${200==100} : ${200==100} <br>
\${200!=100} : ${200!=100} <br>
\${'10'- 10} : ${'10'- 10} <br>
\${10 * "10"} : ${10 * "10"} <br>
\${40 div 5} : ${40 div 5 } <br>
\${ 40 mod 5 } : ${ 40 mod 5 } <br>
\${10 eq 10} : ${10 eq 10} <br>
\${10 lt 10} : ${10 lt 10} <br>
\${10 gt 10} : ${10 gt 10} <br>
\${10 le 10} : ${10 le 10} <br>
\${10 ge 10} : ${10 ge 10} <br>
\${10 > 5?'A':'B'} : ${10 > 5?'A':'B'} <br>
\${100 + 200 + 300} : ${100 + 200 + 300} <br>
\${100 += 200 += 300} : ${100 += 200 += 300} <br>
\${"EL" += 12 += 34 += "문자열 결합연산"} : ${"EL" += 12 += 34 += "문자열 결합연산"} <br>
</body>
</html>
```





# JSTL



### core 라이브러리

```jsp
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ taglib prefix = "c" uri="http://java.sun.com/jsp/jstl/core" %>
<%request.setCharacterEncoding("utf-8"); %>
<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8">
<title>Insert title here</title>
</head>
<body>
<c:set var = "username" value="korea" scope="request" />
<c:if test="${username != null}" >
<c:out value ="${username }"/> <br>

</c:if>
<c:set var = "jumsu" value="${param.jumsu}" scope="request" />
<c:out value = "${jumsu +=\"점은\" }"/>
<c:choose>
 <c:when test="${jumsu>=90}">
 <c:out value ="A" />
 </c:when>
 
  <c:when test="${jumsu>=80}">
 <c:out value ="B" />
 </c:when>
 
  <c:when test="${jumsu>=70}">
 <c:out value ="C" />
 </c:when>

 <c:when test="${jumsu>=60}">
 <c:out value ="D" />
 </c:when>
 

<c:otherwise>
	<c:out value="F"/>
	</c:otherwise>
	

</c:choose>

</body>
</html>
```









```java
package lab.web.model;

public class Product {
	private String name;
	private int price;
	private String category;
	
	
	public Product() {
		super();
	}


	public Product(String name, int price, String category) {
		super();
		this.name = name;
		this.price = price;
		this.category = category;
	}


	public String getName() {
		return name;
	}


	public int getPrice() {
		return price;
	}


	public String getCategory() {
		return category;
	}
	


}


```





```jsp
<%@page import="java.util.ArrayList"%>
<%@page import="lab.web.model.Product"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ taglib prefix = "c" uri="http://java.sun.com/jsp/jstl/core" %>
<%
request.setCharacterEncoding("utf-8");
Product p1 = new Product("수박",10000,"과일");
Product p2 = new Product("손선풍기",5000,"전자");
Product p3 = new Product("브라보콘",1500,"빙과");
ArrayList<Product> alist = new ArrayList();
alist.add(p1);
alist.add(p2);
alist.add(p3);
request.setAttribute("products", alist);


%>
<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8">
<title>Insert title here</title>
</head>
<body>


<c:forEach var="count" begin="1" end="10" step="2">
	${count }<br>
	
</c:forEach>

#상품정보 리스트<br>
<table>
<tr><th>상품명</th><th>가격</th><th>분류</th></tr>
<c:forEach var="product" items="${products }">
<tr><th>${product.name }</th><th>${product.price }</th><th>${product.category }</th></tr>
</c:forEach>

</table>

</body>
</html>
```













------------------------------복습------------------------------------

354p~408p

Http 프로토콜 접속시 생성된 상태 정보를 유지하지 않는 stateless 프로토콜

#접속시 웹 컨테이너에서 생성한 JSESSION ID, 로그인 정보, 쇼핑 카트에 저장된 상품 정보등 유지하는 방법

1. url의 쿼리 스트링으로 추가

   http://ip:port/웹컨텍스트/xxx/jsp

2. html페이지에 <input type = hidden name="" value=""> form 전송

3. Cookie 사용 -클라이언트 브라우저 저장소에 저장

   Cookie c = new Cookie(key, value);

   HttpServletResponse.addCookie(): 로 응답 (클라이언트에게 전송)

   HttpServletRequest.getCookie() : Cookie[] 클라이언트 요청으로부터 쿠키를 추출

   쿠키 유효기간 설정 setMaxAge(); //초단위

   쿠키 정보 삭제 setMaxAge(0)

4. Session 사용 - 웹 컨테이너의 메모리에 저장 (Java기반이므로 객체로 저장)

   Session객체는 최초 요청시에 웹 컨테이너가 HttpSession 구현 객체를 생성

   요청시에 생성된 Session객체를 받아오려면  HttpServletRequest.getSession()

   setAttribute(key, value)

   removeAttribute(key)

   getAttribute()

   웹 컨테이너가 생성한 HttpSession 객체에 저장된 JESSION ID 반환 메소드

   getLastAccessTime()

   클라이언트 요청이 없어도 HttpSession을 웹 컨테이너의 메모리에 유지 시간을 설정 웹 컨텍스트 전역으로 세션 시간 설정은 web.xml에 다음 설정 추가

   <session-config>

   ​	<session-timeout> 30 </session-timeout>

   </session-config>

   

   세션에 저장된 상태정보를 삭제하고 세션 객체를 만료시키려면 invalidate()

   

   

5. 

#요청을 재지정 - 클라이언가 요청한 Servlet이나 JSP에서 응답하는 대신 요청을 다른 자원 (JSP, 서블릿)에 전달

1. request dispatcher 방식

   ```
   -동일한 웹 컨텍스트의 JSP나 Servlet에게 요청 재지정 가능
   
   -url주소 표현은 최종 요청이 전달된 Servlet이나 JSP
   
   -ServletContext sc = request.getServletContext()
   
    RequestDispatcher sc = request.getServletDispatcher("/요청 재지정 자원 경로와 동일");
   
    request.setAttribute(key, value);
   
    rd.forward(request, response)
   
    동일한 웹 컨텍스트의 JSP나 Servlet에게 request를 이용해 공유 가능
   ```

   

   

2. redirect 방식

   ```
   
   
   -동일한 웹 컨텍스트의 JSP나 Servlet에게 요청 재지정 가능
   
   -다른 웹 컨텍스트의 JSP나 Servlet에게 요청 재지정 가능
   
   -다른 웹 서버로 요청 재지정 가능
   
   -url주소 표현은 최종 요청이 전달된 Servlet이나 JSP 또는 웹 서버의 주소
   
    response.sendRedirect("url의 path형식"); // http /상대경로 root conntext로 부터 시작하는
   
   최초 요청시에 컨테이너가 생성한 request와 response는 소멸되고 ,새로운request와 response객체가 redirect된 자원으로 전달됩니다.
   
   동일한 웹 서버내에 동일한 웹 컨텍스트에 공유해야 할 정보를 전달하려면 HttpSession.setAttribute(key, value)또는 ServletContext.setAttribute(key, value) 사용
   ```

   

   



# JSP

html또는 xml 기반의 동적인 웹 컨텐츠를 개발하는 스크립트

응답되는 웹 페이지의 컨텐츠를 만들기 위해 사용(View로만 제한) , 텍스트 기반의 문서

자바 코드 로직을 가능한한 포함하지 않고 태그, el로만 컨텐츠를 생성 권함



#### 정적 지시자

```jsp
<%@ page contentType="text/html; charset=ut-8"
    session
    buffer
    isThreadSafe
    errorPage
    isErrorPage
    info
    language
    import
    extends
    isELIgnored
    defferedSyntaxAllowedAsLiteral
     %>


<%@ include file=""%> 		#JSP 페이지내에 다른 JSP페이지를 포함

-포함될 JSP페이지에서 <html>, <head>, <body>를 제외하고, <body>태그의 내용의 컨텐츠만 ..



<%@ taglib  prefix="" uri="http://java.sun.com/jsp/jstl/~" %>

-JSP페이지내에 HTML 이 아닌 태그를 만나면 태그에 매핑된 Java class를 실행시켜서 실행 결과를 페이지의 컨텐츠로 처리
-JSTL(Java Standard Tag Library)을 사용하기 위한 선언 , core, sql, xml, 국제화 format처리 라이브러리등을 사용하기 위해 선언        




text/xml

text.plain, text/json

image/jpeg

...

application/vmd.ms-
    ${}
    
{} 템플릿 컨텐츠 - JSP의 표현식    
최초 JSP 요청 -> 컨테이너가 변환된 서블릿 java파일을 검색 -> 존재하지 않으면 서블릿 java파일 변환 -> 컴파일 -> 클래스를 메모리 로딩 -> 서블릿 객체 생성 -> lifecycle 메서드 호출
#declare <%! 전역변수 또는 메서드 정의   %> : 변환된 서블릿의 맴버로 정의
#scriptlet <% 자바 실행 문장;    %> : _jspService() 메서드의 문장으로 포함
#expression <%= 출력내용   %> : 변수, 연산식, 값을 리턴하는 함수을 웹 페이지에 출력할 내용, <% out.prinrln(출력내용) %>, ${출력내용}

JSP 주석
<%-- JSP 주석 --%>
<%
  //주석
  /* 여러줄 주석 */
    
 %>
<!-- html 또는 xml 주석 -->

```





### 

### 동적인 요청을 처리하는 JSP를 요청과 응답을 처리하기 위해서 JSP 컨테이너가 서블릿으로 변환하면서 내장 객체들을 생성해서 _jspS

```
JSP에서는 내장 객체를 new 로 생성하지 않고 컨테이너가 정의해놓은 이름으로 사용

request - javax.servlet.http.HttpServletRequest

response - javax.servlet.http.HttpServletResponse 

session - javax.servlet.http.HttpServletSession
application - javax.servlet.http.ServletContext
out - javax.servlet.jsp.JSPWriter
exception - java.lang.Throwable
page - java.lang.Objext
config - javax.servlet.ServletConfig
pageContext - javax.servlet.jsp.PageContext
```



###  내장 객체들의 유효범위 - 컨테이너 메모리에 유지되는 범위

```
page - 요청된 JSP가 수행되는 동안에만 유지
request - 요청이 종료될때까지
session - 세션 만료 될떄까지 또는 inactive상태에서 30분
appication - 웹 컨택스트가 웹 컨테이너로부터 삭제될때까지 또는 웹 컨테이너가 종료 될때까지

page, request, session, application에 정보를 저장, 삭제, 번환 메서드
setAttribute(),
getAttribute()
removeAttribute()
getAttributeNames()


```



### 자주 구현하는 기능을 태그로 정의

```
표준 액션 태그 : <JSP:useBean ~~~
				JSP 스펙에 정의된 기능, 모든 JSP 컨테이너가 지원하므로 항상 JSP 구현에 사용 가능

커스텀 액션 태그 : 개발자가 직접 태그 클래스 ,  tld(xml형식) 파일을 정의해서 사용

EL(Expression Language) : 표현언어, JSP2.0에서 추가    
<c:out ...> 또는 <jsp:getProperty ..> 보다 간결하게 사용가능
page, session, request, application 에 저장된 객체를 간결하게 표현함


표준 액션 태그 : <jsp:useBean ~>
                 <jsp:setProperty~
                 <jsp:getProperty~    

<jsp:include page=""/>
<jsp:param name="" value=""/>
```









