# JSP

http

JVM

Web server 기능 + A







## CGI

초기 웹 프로그래밍에 사용된 기술

프로세스 단위로 실행되기 때문에 사용자 증가하면 급격히 성능 저하



## ASP

윈도우운영체제에 기반한 웹 애플리케이션 기술로 비교적 쉽고 빠르게 웹 애플리케이션 구현이 가능하다. 최근 윈도우 개발 환경이 닷넷(.Net) 플랫폼으로 변화 되면서 ASP.Net 이라는이름으로 변경되어 보다 강력해 졌다.

## PHP

오픈소스 프로젝트로 다양한 운영체제와 웹서버를 지원한다. 빠른 처리속도와 메일, 데이터베이스 연동기능등을 통해 초기 서버 스크립트 기술의 대표로 주목 받았으나 완전한 프로그래밍 언어가 아닌 관계로 **기능확장에 한계**가 있다. 최근까지도 거급된 발전을 통해 처음 보다 많이 향상 된 기능을 제공하나 예전에 비해 전체적인 사용빈도는 떨어진다.

## 서블릿(Servlet)

자바기반의 웹 프로그래밍 기술로 자바 언어의 모든 기능을 사용할 수 있으며 쓰레드 기반의 빠른 처리 속도를 자랑하나, 프로그램 내에서 화면 코딩을 제어해야 하는 문제로 인해 유지 보수에 많은 문제가 있다. 이러한 문제점을 개선한것이 JSP로 JSP는 내부적으로 서블릿 기술에 기반하고 있다.

## JSP

**servlet**이라고 하는 자바 웹 프로그래밍 기술에 기반을 두고 있으며, PHP 나 ASP와 같이 HTML과 함께
스크립트를 사용할 수 있도록 되어 있다.
JSP 의 장점은
스레드 기반으로 시스템 자원을 절약하고 효율적인 공류가 가능하며 최초 요청시 서블릿으로 컴파일 되어 이후 요청에 대해서는 메모리에서 처리
하므로 보다 빠른 처리 속도를 제공 한다.
또한 자바
언어의 모든 기능을 사용할 수 있으므로 무한한 확장성을 자랑한다.





## JSP와 서블릿(Servlet)

- 웹 브라우저의 요청을 받아 해당하는 웹 페이지를 찾아서 보내주는 일을 하는 컴퓨터를 **웹 서버**라고 한다.
- **웹 서버**는 웹 브라우저로부터 URL을 받아서 그에 해당하는 HTML 문서를 찾아서 웹 브라우저로 보내주는 일을 한다.
- **HTML**문서는 순수하게 텍스트로만 이루어지며, **<HTML>,</HTML>, <BODY>, </BODY>, <H1>, </H1>**과 같이 꺽쇠괄호로 묶여진 부분을 태그(**tag**) 또는 마크업(**markup**)이라고 한다.
- **태그**는 웹 브라우저 상에 그대로 표시되는 것이 아니라 그 밖의 부분이 웹 브라우저 상에 어떻게 표시될지 지시하는 역할을 한다. 



## 지오로케이션

```html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title> </title>
<style>
 
</style>

<script>
	function showPosition(pos) {
		document.getElementById("demo").innerHTML = "위도: " + pos.coords.latitude + "<br>경도: " + pos.coords.longitude
	}

	function locationEventHandler(){
		if(navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(showPosition);
		} else {
			document.getElementById("demo").innerHTML = "브라우저가 geolocation을 지원하지 않습니다.";
		}
	}


</script>
</head>
<p>현재 위치</p>
<button onclick="locationEventHandler()">위도/경도</button>
<p id="demo"></p>
</body>
</html>
```

