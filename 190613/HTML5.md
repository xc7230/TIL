# HTML5

## 웹구조

웹 요청, 응답구조





post 

바디에다 보안적으로 중요한 내용 보낼때

회원가입 



도메인/ bss / list.html

accept 허용가능한거

aceept - language 언어





## 웹역사

### 초기

www(1990 초반) 팀리버스가 만듦 

단순 html서비스 

동기방식 

전체페이지 갱신방식web1.0

정적 서비스



#### BackEnd

JSP(Mode 방식)

EJB(분산방식)

Framework 등장





### FrontEnd

html - 문서구조

css - 스타일

javascript - 동적

Rich Client Internet

W3C 웹표준화

Ajax 비동기 요청 부분페이지 갱신



### 연습

```html
<!D0CTYPE html>
<html>
<head>
<meta charSet = 'utf-8'>
<title>Html 기본구조 </title>
<style>
body {
	font-Size : 20px;
	color : red;
}

</style>
</head>
<body>
안녕하세요. 반갑습니다 ~~~~~
</body>
</html>
<!--주석 소스보기에는 있습니다. -->

```



저장은  .html로 저장합니다.





## HTML5

주소 : [https://www.w3schools.com]



태그(Tag), 요소(Element),속성(Attribute)



### lang속성

해당 웹 페이지가 어떠한 언어로 만들어져 있는지 인식



### head태그

body 태그에 필요한 스타일시트와 자바스크립트를 제공하는 데 사용



### body태그

사용자에게 실제 보이는 부분

```html
<body>
<h1>Header 1</h1>
<h2>Header 2</h2>
<h3>Header 3</h3>
<h4>Header 4</h4>
<h5>header 5</h5>
<h6>header 6</h6>
<!--Block태그  -->
</body>
```



### 글자형태태그

```html
<b> Header 1 </b><br> <!--굵은 글자 -->
<i>Header 2</i><br> <!--기울어진 글자 -->
<small>Header 3</small><br> <!--작은 글자 -->
<sub>Header 4</sub><br> <!--아래에 달라붙은 글자 -->
<sup>Header 5</sup><br> <!--위에 달라붙는 글자 -->
<ins>Header 6</ins><br> <!--밑줄 글자 태그 -->
<del>Header 7</del><br> <!--가운데 줄이 그어진 글자 태그 -->
```



### Ruby

```html
<!D0CTYPE html>
<html>
<head>
<meta charSet = 'utf-8'>
<title>Html 기본구조 </title>
<style>
body {

	
}

</style>
</head>
<body>
	<ruby>
		<span>大韓民國</span>

		<rt>대한민국 </rt>


	</ruby>

</body>
</html>

```





### Ol Tag



```html
<ol>
		<li>Facebook</li> <!--목록 앞에 숫자가 순서대로 붙는다 -->
		<li>Tweeter</li>
		<li>Linked In</li>
	</ol>
```





### Ul Tag

```html
<li>Facebook</li> <!--목록 앞에 점이 붙는다. -->
		<li>Tweeter</li>
		<li>Linked In</li>
```





### 테이블태그

데이터를 표에 넣어준다.

```html
<!D0CTYPE html>
<html>
<head>
<meta charSet = 'utf-8'>
<title>Html 기본구조 </title>
<style>


</style>
</head>
<body>
	<table border="1">
		<tr>
			<tr>Header 1</tr> 
			<tr>Header 2</tr>
		</tr>
		<tr>
			<td>Data 1</td> <!--1행 1열 -->
			<td>Data 1</td> <!--1행 2열 -->

		</tr>
		<tr>
			<td>Data 2</td> <!--2행 1열 -->
			<td>Data 2</td>	<!--2행 열 -->

		</tr>

	</table>
</body>
</html>
```





### 사진넣기

```html
<!D0CTYPE html>
<html>
<head>
<meta charSet = 'utf-8'>
<title>Html 기본구조 </title>
<style>


</style>
</head>
<body>
	<img src="Chrysanthemum.jpg" alt="국화" width="300"/>
</body>
</html>
```





### 음악넣기

```html
<!D0CTYPE html>
<html>
<head>
<meta charSet = 'utf-8'>
<title>Html 기본구조 </title>
<style>


</style>
</head>
<body>
	<audio src="SAMPLE_1.mp3" controls autoplay loop></audio>

</body>
</html>
```





### 비디오 넣기

```html
<!D0CTYPE html>
<html>
<head>
<meta charSet = 'utf-8'>
<title>Html 기본구조 </title>
<style>


</style>
</head>
<body>

	<video width="1000" height="1000" autoplay controls loop>
		<source src="sample.mp4" type="video/mp4">
		<source src="sample.webm" type="video/webm">
		<source src="sample.ogg" type="video/ogg">

	 </video>

</body>
</html>
```





### 링크걸기

```html
<!D0CTYPE html>
<html>
<head>
<meta charSet = 'utf-8'>
<title>Html 기본구조 </title>
<style>


</style>
</head>
<body>

	 <h2>링크걸기 </h2>
	<h3><a href="http://70.12.50.130:9000/web1.html" target="_blank"> 웹 </a></h3>

</body>
</html>
```



### 회원가입

```html
<!D0CTYPE html>
<html>
<head>
<meta charSet = 'utf-8'>
<title>Html 기본구조 </title>
<style>


</style>
</head>
<body>


<h1>회원가입</h1>
<form method="post" action="login.jsp" name="" id="">
	아 이 디 : <input type="text" name="userid" id="userid" required><br>
	비밀번호 : <input type="password" name="userpwd" id="userpwd"><br>
	url : <input type="url" name="url"><br>
	email : <input type="email" name="email"><br>
	연락처 : <input type="tel" name="phone" pattern="\d{3}-\d{4}-\d{4}" placeholder="000-0000-0000"><br>
	number : <input type="number" max="100" min="0" step="5" title="0~100사이의 값만 허용합니다. "><br>

	취미 : <input type="checkbox" name="hobby" value="등산"> 등산
	<input type="checkbox" name="hobby" value="수영"> 수영
	 <input type="checkbox" name="hobby" value="코딩">코딩<br>

	 기술 : <input type="radio" name="skill" value="java"> JAVA
	<input type="radio" name="skill" value="oracle"> ORACLE
	 <input type="radio" name="skill" value="r">R<br>

	 date : <input type="date"><br>
	 time : <input type="time"><br>
	 week : <input type="week"><br>
	 month : <input type="month"><br>
 	 color : <input type="color"><br>
 	 range : <input type="range" max = "100" min = 0 step =5><br>
 	 암호화 키<keygen name = "key"><br />
 	 Serch : <input type="serch"><br>
 	 <textarea rows="5" col = "30">
 	 </textarea>


 	<input type="file"><br>
 	<select>
 		<option>서울</option>
 		<option>경기</option>
 		<option>강원도</option>
 		<option>경상도</option>
 		<option>전라도</option>

 	</select>
	<input type="button" value="버튼"><br>

	<input type="text" name="fruit list="fruits>
	<datalist id = "fruits">
	<option value="apple" label="사과">
	<option value="orange" label="오렌지">
	<option value="grape" label="포도">
	<option value="lemon" label="레몬">
	<option value="mango" label="망고">
	<option value="melon" label="멜론">
	</datalist>

	<br>
	<br>
	<details open>
	<summary> 복사중
...
<progress max="375505392" max="97543287"></progress> 25%
	</summary>
	<dl>
	<dt>초당 전송량</dt><dd>452KB/s</dd>
	<dt>복사파일명</dt><dd>/home/rpausch.raycd.m1v/s</dd>
	<dt>대상파일명</dt><dd>/var/www/lectures/raycdm4v</dd>
	<dt>걸린시간</dt><dd>01:16:27</dd>
	<dt>영상크기</dt><dd>2320x240</dd>
</dl>
</details>

	<input type="submit" value="로그인"><br>
	<input type="reset" value="취소"><br>
</body>
</html>
```





### 웹페이지 레이아웃

```html
<!D0CTYPE html>
<html>
<head>
<meta charSet = 'utf-8'>
<title>Html 기본구조 </title>
<style>
.clear {
	clear: both;
}
header {
width: 995px;
height: 100px;
margin-top: 10px;
border: solid 1px green; 
}

nav {
width: 995px;
height: 70px;
margin-top: 10px;
border: solid 1px green; 

}

section {
width: 674px;
height: 240px;
float: left;
margin-top: 10px;
border: solid 1px green; 
}

aSide {
width: 290px;
height: 240px;
float: left;
margin-top: 10px;
margin-left: 29px;
border: solid 1px green; 
}
footer {
width: 995px;
height: 130px;
margin-top: 10px;
border: solid 1px green; 

}

</style>
</head>
<body>
<header>
	상단헤더
</header>

<NAV>
	내비게이션 메뉴 
</NAV>
<section>
	메인 콘텐츠
</section>

<aside>
	사이드바
</aside>

<div class = "clear"></div>	

<footer>
	하단푸터

</footer>
</body>
</html>

```

