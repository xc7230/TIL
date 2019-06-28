



# JSP

 스크립트, HTML태그와 함께 java코드 포함

view와 로직이 분리 안되어서 재사용성이 낮음



Servlet -> JSP -> EJB(망함) -> MVC패턴 적용 웹 애플리케이션 구현 (View 페이지는 JSP, Controller는 Servlet, data 영속성과 비지니스 로직은 JavaObject)



### 기본요소

현재 JSP는 MVC구조에서 View로만, 태그와 EL(Expression L)

정적 지시자 <%@ page 지시자%>

​					  <%@ include ~~~~%>

​					  <%@ taglib  ~~~~%>

동적 지시자 <jsp:include ~></jsp:include>

​					  <jsp:useBean ~></jsp:getProperty~~~~/><jsp:setProperty~~/><



declare scriptlet <%! 

변수 선언 초기화; //변환된 서블릿의 멤버변수로 정의

public void method() {

문장;

}///변환된 서블릿의 멤버 메서드로 정의

%>

scriptlet<%

자바 실행 문장 ; //변환된 서블릿의 _service()의 실행문장으로 보이는 내용

....

%>



expresstion <%= 출력내용%> 은 <% out.println(출력내용) %> 와 동일 합니다.

# 세션

```jsp
package lab.web.session;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


@WebServlet("/lottolimit")
public class LottoServletLimit extends HttpServlet {
	
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	HttpSession session = request.getSession();
	if(session.getAttribute("lottocnt") == null) {
		session.setAttribute("lottocnt", new int[1]);
	}
	int[] count = (int[]) session.getAttribute("lottocnt");
	String msg = "";
	if(++count[0]>3) {
		msg = "<h3>더이상 응모할 수 없습니다.ㅋㅋㅋㅋ</h3><h3>브라우저를 재시작하여 응모하세요.</h3>";
	}else {
		int answer = (int)(Math.random() *10)+1;
		int input = Integer.parseInt(request.getParameter("guess"));
		if(answer == input) {
			msg = "<h3>축하합니다..... 당첨입니다.</h3>";
			count[0] = 4;
		}else {
			msg = "<h3>다음 기회를 ...ㅋㅋㅋㅋ</h3><a href ='" + request.getHeader("referer")+"'>재도전</a>";
		}
	}
	response.setContentType("text/html; charset=utf-8");
	PrintWriter out = response.getWriter();
	out.println(msg);
	out.close();
	}
	

}

```



```jsp
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>calc.jsp</title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
 $(document).ready(function(){
	 $("#f1").submit( function(event){
		 event.preventDefault();
		 var n1 = $("#num1").val();
		 var n2 = $("#num2").val();
		 var op = $("#operator option:selected").val();		 
		  $.ajax( {
			    url  : "./CalcServlet2",
			    data : {"num1" : n1, "num2": n2, "operator" : op},
				  success: function(data){ 
					  console.log(data);
					  $("#result").html("<mark>"+n1+op+n2+"="+data+"</mark>");
				  }
		  });
		 
	 })
 });
 
</script>
</head>
<body>
<h3>계산기</h3>
  <form id="f1" >
   number1 :
   <input type="text"  name="num1" id="num1"  ><br>
   operator :
   <select name="operator" id="operator">
   <option value="+">+</option>
   <option value="-">-</option>
   <option value="*">*</option>
   <option value="/">/</option>
   </select>
   <br>
   number2 :
   <input type="text"  name="num2"  id="num2" ><br>
   
   <input type="submit"  value="계산">
  </form>
  <hr>
  계산결과 :  <span id="result"></span>
</body>
</html>
```





```jsp
package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("./CalcServlet2")
public class CalcServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;


    public CalcServlet() {
        super();
    }

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/plain;charset=utf-8");
		PrintWriter out = response.getWriter();
		int num1 = Integer.parseInt(request.getParameter("num1"));
		int num2 = Integer.parseInt(request.getParameter("num2"));
		String op = request.getParameter("operator");
		int result = 0;
		switch(op) {
		case "+" : result = num1+num2 ; break;
		case "-" : result = num1-num2 ; break;
		case "*" : result = num1*num2 ; break;
		case "/" : result = num1/num2 ; break;
		
		
		}
		out.println(result);

	}

}

```





---------------------------복습-----------------------------------

http 요청 메시지로부터 헤더 정보 추출?



 httpServletRequest.getHeaderName() : Enumeration<String>

Enumeration.hasMoreElement() : boolean

Enumeration.nextElement() : String

httpServletRequest.getHeader()

httpServletRequest.getHeader() : header이름으로 지정된 value를 반환 (String)

httpServletRequest.getHeaders() : header이름으로 지정된 value가 하나이상이면 



http 요청 메시지를 전송한 클라이언트 ip 정보 추출?

httpServletRequest.getRemoteAddr()



http 요청 메시지를 전송한 방식 정보 추출?

httpServletRequest.getMethod()



WAS가 서비스하는 웹 컨텍스트를 생성하면 웹 컨텍스트를 추상화한 객체 : ServletContext

httpServletRequest.getServletContext() : 요청한 웹 컨텍스트의 객체를 반환하는 메서드

클라이언트가 form태그내에 data를  서버 웹 컴포넌트로 전송,

서버 웹 컴포넌트에서 클라이언트가 보낸 form데이터를 추출하려면?

httpServletRequest.getParameter("input 요소의 name속성값")

cheakbox input요소 checked 요소의 value들을 추출 String[] 반환 

httpServletRequest.getParameterValues('input 요소의 name속성값')

예) 1. memberform.html요청 (단순페이지요청 : GET방식)

 	 2.HttpListener가 html페이지 응답

   3. 클라이언트가 데이터 입력하고 form data전송

      <form action="" method=" " encType = ""

   4. @WebServlet("/join") 선언된 서블릿이 요청을 받이서 응답 처리

      파일 업로드 처리하는 서블릿에 선언할 Annotation? 

      @MultipartConfig(location ="", maxFileSize="", maxRequestSiz = " ")

      업로드된 파일의 메타정보와 스트림등을 추출하기 위해 반환 객체

      HttpServletRequest.getPart() : Part

      HttpServletRequest.getParts() : Collection<Part>

      part.getName() : 업로드된 파일 이름 반환

      Part.getConteneType() : 업로드된 파일의 내용 유형을 반환

      Part.getSize() : 업로드된 파일 크기 반환

      Part.write() : 업로드된 파일을 @MultipartConfig의 location에 출력 (서버에 파일로 기록, )

      

      

#요청을 동일한 웹 컨텍스트의 다른 servlet 또는  jsp에 전송 가능

ServletContext sc = request.getServletContext(); //요청 웹 컨텍스트 객체 반환

RequestDispatcher rd = sc.getRequestDisaptcher("/다른 servlet 또는 jsp 경로")//요청을 전달할 

rd.forward(request, response);

rd.include(request, response);



HttpServletRequest.setAttribute(키로 사용될 객체, 값 객체); //

HttpServletRequest.getAttribute(키) : object로 반환되므로 실제 저장한 타임으로



</a href="./xxx"> 요청 전달 </a>



Http 특성은 요청시 Connection되며, 응답이 전송되면 disconnect됩니다. => 비연결형 protocol

상태 정보를 저장할 방법 : 클라이언트 브라우저에 저장 (key = value)

#상태 정보를 저장할 방법 :

1. 클라이언트 브라우저에 저장(key=value) : Cookie, setMaxAge()
2. url의 쿼리 스트링으로 요청시마다 전송
3. 요청을 전송하는 페이지에 <input type="hidden" name = "" value = "">
4. 웹 서버에 객체로 저장 : Session, 클라이언트의 브라우저 종료되오 세션아 종료



1. 클라이언트가 특정 웹 서버(tomgat)로 최초 요청을 전송

2. 웹 서버(tomcat)가 클라이언트 요청에 대해 응답을 할때 JSessionID 값을 생성해서 쿠키로 전송

3. 클라이언트가 웹 서버로 두번째, 세번째, ....요청할때 마다 브라우저 자체적읋 요청 웹 서버에서 보내준 쿠키 정보를 찾아서 전송

4. .웹 서버의 웹 컴포넌트(서블릿)에서 요청과 함께 정보를 추출하려면

   HttpServletRequest.getCookies() : Cookie[]

     

new Cookie(key, name)객체를 응답으로 전송하려면 HttpServletResponse.addCookie

예) 1. http://ip:port/web1/cookieLogin 요청(GET방식)

​	  2.@webServlet("/cookieLogin") 서블릿의  doGet()요청 처리

   - 쿠키 정보 추출 request.getCookies(), userid키로 저장된 값 검색

   - 추출한 쿠키 정보를 request.setAttribute("userid" 쿠키값);

   - RequestDispatcher 를 사용해서 "/cookie_login.jsp"로 전달

     3. form태그 전송 (action = "cookieLogin" method="post")

     4. @webServlet("/cookieLogin")서블릿의 doPost()요청 처리

        -로그인 처리

        -아이디 저장 checkbox 선택된 경우  userid를 쿠키로 저장

        -RequestDispatcher를 사용해서 "/main.jsp"로 전달

     5. main.jsp에서 로그아웃(/cookieLogout) 요청 (GET방식)

     6. @webServlet("/cookieLogout")서블릿 의 doGet 요청처리

        -쿠키 정보 삭제 request.getCookies(), 쿠키 정보 추출해서 cookies[i].setMaxAge(0);

        -RequestDispatcher를 사용해서 다시 로그인 페이지 전송

