	<dependency>
		<groupId>commons-fileupload</groupId>
		<artifactId>commons-fileupload</artifactId>
		<version>1.4</version>
	</dependency>
	
	<dependency>
		<groupId>commons-io</groupId>
		<artifactId>commons-io</artifactId>
		<version>2.6</version>
	</dependency>




```java
package lab.spring.web.model;

import org.springframework.web.multipart.MultipartFile;

public class ReportCommend {
	
	public String getStudentNumber() {
		return studentNumber;
	}






	public void setStudentNumber(String studentNumber) {
		this.studentNumber = studentNumber;
	}






	public MultipartFile getReport() {
		return report;
	}






	public void setReport(MultipartFile report) {
		this.report = report;
	}






	private String studentNumber;
	private MultipartFile report;
	
	

	


	public ReportCommend() {
		super();
	}






	public ReportCommend(String studentNumber, MultipartFile report) {
		super();
		this.studentNumber = studentNumber;
		this.report = report;
	}

}

```





```java
<bean id="multipartResolver" 
	class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
  <property name="maxUploadSize" value="1000000" />

</bean>
```





```
============================reportForm.jsp============================
<%@ page contentType="text/html; charset=utf-8"%>

<html>
<head>
<meta charset="utf-8">
<title>리포트 제출</title>
</head>
<body>
<h3>@RequestParam 사용</h3>
<form action="submitReport1.do" method="post" enctype="multipart/form-data">
	학번: <input type="text" name="studentNumber" />
	<br/>
	리포트파일: <input type="file" name="report" />
	<br/>
	<input type="submit" value="제출"/>
</form>

<h3>MultipartHttpServletRequest 사용</h3>
<form action="submitReport2.do" method="post" enctype="multipart/form-data">
	학번: <input type="text" name="studentNumber" />
	<br/>
	리포트파일: <input type="file" name="report" />
	<br/>
	<input type="submit" value="제출"/>
</form>

<h3>커맨드 객체 사용</h3>
<form action="submitReport3.do" method="post" enctype="multipart/form-data">
	학번: <input type="text" name="studentNumber" />
	<br/>
	리포트파일: <input type="file" name="report" />
	<br/>
	<input type="submit" />
</form>


</body>
</html>
```





```
===========================reportComplete.jsp=============================
<%@ page contentType="text/html; charset=utf-8"%>
 

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>리포트 제출 완료</title>
</head>
<body>
리포트 제출 완료
</body>
</html>
```



### @RequestParam 사용

```java
package lab.spring.web.controller;

import java.io.FileOutputStream;
import java.io.File;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;



@Controller
public class ReportController {
	
	@RequestMapping("/report/report.do")
	public String form() {
	return "report/reportForm";
	}
	
	@RequestMapping("/report/submitReport1.do")
	public String submitReport1(
			@RequestParam("studentNumber") String studentNumber,
			@RequestParam("report") MultipartFile report) {
		printInfo(studentNumber, report);
		if(report.getSize()==0)
			throw new NullPointerException("업로드된 파일 없음");
		return "report/reportComplete";
	}
	
	
	private void printInfo(String studentNumber, MultipartFile report) {
		if(!report.isEmpty()) {
			String filename = report.getOriginalFilename();
			String imgExt = filename.substring(filename.lastIndexOf(".")+1, filename.length());
			try {
				if(imgExt.equalsIgnoreCase("JPG")
					||imgExt.equalsIgnoreCase("JPEG")
					||imgExt.equalsIgnoreCase("GIF")
					||imgExt.equalsIgnoreCase("PNG")) {
					
					byte[] bytes = report.getBytes();
					File outFile = new File("c://upload/" + "_" + filename);
					FileOutputStream fos = new FileOutputStream(outFile);
					fos.write(bytes);
					fos.close();
				} else {
					System.err.println("File type error! ");
				}
				System.out.println(studentNumber + "제출된 보고서: " + report.getOriginalFilename());


						
				
			}catch(Exception e) {
				e.printStackTrace();
			}
		}
		
		
	}


	@ExceptionHandler(NullPointerException.class)
	public String handleException(NullPointerException exception) {
		return "common/error"; //뷰이름 리턴
	}
	

}

```



WEB-INF / view

```
============================error.jsp============================


<%@ page contentType="text/html; charset=utf-8" isErrorPage="true"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>error.jsp</title>
</head>
<body>
예외가 발생했습니다. :<br>
<%=exception.getMessage()%>
${exception.message}<br>
</body>
</html>
```







```
============================loginSuccess.jsp============================


<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
  <%@ taglib  prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
p { color: blue;}
</style>
<title>loginSuccess.jsp</title>
</head>
<body>
<c:if test="${!empty authInfo}">
<p> ${authInfo.userid}님 환영합니다.%%</p>
<a href="<c:url value='/view.do?userid=${authInfo.userid}'/>">정보를 수정하시겠습니까?</a><br>
<a href="<c:url value='/list.do' />">정보리스트</a><br>
<a href="<c:url value='/logout.do' />">로그아웃</a><br>


</c:if>
</body>
</html>
```



### 

```
package lab.spring.web.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import lab.spring.web.model.UserVO;
import lab.spring.web.service.UserService;

@Controller
public class LoginController {
	
	@Autowired
	UserService service;
	
	@RequestMapping(value = "/login.do", method=RequestMethod.GET)
	public String form() {
		return "loginForm"; 
	}
	
	@RequestMapping(value = "/login.do", method=RequestMethod.POST)
	public ModelAndView login(@RequestParam("userid")String uid,
							@RequestParam("userpwd")String upwd,
							HttpSession session) {
		
		ModelAndView mav = new ModelAndView();
		UserVO vo = null;
		vo = service.login(uid, upwd);
		session.setAttribute("authInfo", vo);
		//mav.addObject("user", vo);
		if(vo!=null) {
			mav.setViewName("loginSuccess");
		} else {
			mav.setViewName("loginFail");
		}
		
		return mav;
		
	}
	@RequestMapping(value = "/logout.do")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:login.do";
	}

	

	

	
}

```





```
package lab.spring.interceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

@Component
public class AuthoCheckInterceptor implements HandlerInterceptor {



	public boolean preHandel(HttpServletRequest request,
							HttpServletResponse response,
							Object handler )
	throws Exception {
		HttpSession session = request.getSession(false);
		if(session!=null) {
			Object authInfo = session.getAttribute("authInfo");
			if(authInfo !=null ) {
				return true;
			}
		}
		response.sendRedirect(request.getContextPath()+"/login.do");
		return false;
	}


}

```













----------------------------------------------------------------------------------------------------------------------------------------------------

시험 실습 product비슷한거

### Servlet





기능과 관계없이 HttpServlet 클래스를 상속해야함

main() 메서드 구현x

#### GET 방식 

Http메소드 중 가장 단순한것, 단순히 서버에 자원(HTML, JPEG, PDF 등)을 요청하는 메서드

GET으로 보낼 수 있는 글자수는 제한이 있다.

전송방식은 URL 뒤에 쿼리스트링 붙여 보내는 방식, 중요한 데이터든 아니든 화면에 다 보인다.



#### POST방식

POST방식은 서버에세 자원을 요청할 때 필요한 정보를 함께 넘겨준다. 이 때 정보는 엔티티 바디에 포함되어 전송

길이제한x

쿼리스트링에 노출되지 않아 로그인시 많이 사용

  HTTP메소드로는 HEAD, TRACE, PUT,DELETE, 
  OPTION, CONNECT 등이 있다. 그러나 GET,POST를 가장 많이 사용한다.





