# CSS

보통 헤드테그안에 쓰임

select {

propurty: value, value, .....;}





**CSS선택자**

태그 선택자

•태그의 영역 선택하고 이후에 오는 CSS 명령을 해당 영역에 적용

•p 줄바꾸기

•id 선택자

•웹 페이지에서 유일무이한 단 하나의 특정 영역 지정하여 CSS 명령 적용

•id명 앞에 샵(#) 붙여야

•클래스 선택자 

•두 군데 이상의 특정 영역 지정하여 동일한 CSS 적용

•클래스명 앞에 점(.) 붙여야





**박스모델**

```html

<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>

		h3 {
			border:  dotted 5px blue; /* 박스선 스타일 점으로 */
			padding: 20px 30px 10px 50px;  /* 시계방향으로 간격 */
			margin: 30px;


		}

		li {
			list-style-type: square;

		}
		

	</style>

</head>
<body>

<h3>축제명 : 제주마을박람회 축제</h3>

<ul>
	<li>일 시 : 2018년 9월 중</li>
	<li>장 소 : 원대천 및 외도동 일대</li>
	<li>주요 프로그램 : 어린이 사생대회, 뜸돌들기, 은어 낚시, 소원빌기  </li>

</ul>

</body>
</html>



```

**border**

•예시의 청색 경계선 등 그리는 데 사용하는 속성

**padding**

•경계선 내부 간격

•예시의 콘텐츠 ‘웹이란?’과 경계선 사이의 간격

**margin**

•경계선 외부 간격

•경계선과 외부의 요소 사이의 간격



**border**

•경계선 스타일

–solid (실선)

–double (이중실선)

–dotted (점선)

–dashed (줄 선)

•경계선 두께

–px 단위

•경계선 색상

–색상 이름 혹은 코드



**padding**

•글자와 경계선 사이의 간격



**width / height**

•박스의 너비 / 높이







## 배경색상



```html

<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>

		body {

			background-color: yellow;
		}
		
		#button {
			width: 120px;
			height: 25px;
			padding: 8px;
			background-color: blue;
		text-align: center;

		}

	</style>

</head>
<body>



<h3>축제명 : 제주마을박람회 축제</h3>

<ul>
	<li>일 시 : 2018년 9월 중</li>
	<li>장 소 : 원대천 및 외도동 일대</li>
	<li>주요 프로그램 : 어린이 사생대회, 뜸돌들기, 은어 낚시, 소원빌기  </li>

</ul>

<div id = 'button'>
	자세히 보기 &gt;

</div>

</body>
</html>



```





**배경이미지 삽입**

```html

<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>

		body {

			background-image: url('puppy.jpg'); /*배경 반복해서 (화면 가득) 나온다.*/
			background-repeat: no-repeat;	/*배경사진 반복x*/
		}
		
		#button {
			width: 120px;
			height: 25px;
			padding: 8px;
			background-color: blue;
		text-align: center;

		}

	</style>

</head>
<body>



<h3>축제명 : 제주마을박람회 축제</h3>

<ul>
	<li>일 시 : 2018년 9월 중</li>
	<li>장 소 : 원대천 및 외도동 일대</li>
	<li>주요 프로그램 : 어린이 사생대회, 뜸돌들기, 은어 낚시, 소원빌기  </li>

</ul>

<div id = 'button'>
	자세히 보기 &gt;

</div>

</body>
</html>



```





### 테이블

**경계선 그리기**

```html

<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>

		table, th, td {
			border: solid 1px #000000;
		}

		table {

			border-collapse;
		}
	</style>

</head>
<body>

<table>
  <tr>
    <th colspan='4'>서울 &lt=&gt 대전 2020.9.6 수</th>
  </tr>
  <tr>
    <th>출발</th>
    <th>버스회사</th>    
    <th>등급</th>  
    <th>예약가능</th>    
  </tr>
  <tr>
    <td>11:50</td>
    <td>한진고속</td>
    <td>우등</td>
    <td><img src='full.png'></td>
  </tr>
  <tr>
    <td>12:50</td>
    <td>천일고속</td>
    <td>고속</td>
    <td><img src='empty.png'></td>
  </tr>
  <tr>
    <td>13:50</td>
    <td>한진고속</td>
    <td>우등</td>
    <td><img src='full.png'></td>
  </tr> 
</table>


</body>
</html>



```





**테이블 크기**

```ht

<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>

		table, th, td {
			border: solid 1px #000000;
		}

		table {

			border-collapse;
		}


		th {
			width: 80px;
			padding: 6px;

		}

		td {
			padding: 6px
			text-align: center;
		}
	</style>

</head>
<body>

<table>
  <tr>
    <th colspan='4'>서울 &lt=&gt 대전 2020.9.6 수</th>
  </tr>
  <tr>
    <th>출발</th>
    <th>버스회사</th>    
    <th>등급</th>  
    <th>예약가능</th>    
  </tr>
  <tr>
    <td>11:50</td>
    <td>한진고속</td>
    <td>우등</td>
    <td><img src='full.png'></td>
  </tr>
  <tr>
    <td>12:50</td>
    <td>천일고속</td>
    <td>고속</td>
    <td><img src='empty.png'></td>
  </tr>
  <tr>
    <td>13:50</td>
    <td>한진고속</td>
    <td>우등</td>
    <td><img src='full.png'></td>
  </tr> 
</table>


</body>
</html>



```





**테이블 셀에 색상지정**



```html

<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>

		table, th, td {
			border: solid 1px #000000;
		}

		table {

			border-collapse;
		}


		th {
			width: 80px;
			padding: 6px;

		}

		td {
			padding: 6px
			text-align: center;
		}

		#day {
			background-color: #adf0f4;
		}
		#title {
			background-color: #adcff4;
		}
	</style>

</head>
<body>

<table>
  <tr>
    <th id ='day' colspan='4'>서울 &lt=&gt 대전 2020.9.6 수</th>
  </tr>
  <tr id='title'>
    <th>출발</th>
    <th>버스회사</th>    
    <th>등급</th>  
    <th>예약가능</th>    
  </tr>
  <tr>
    <td>11:50</td>
    <td>한진고속</td>
    <td>우등</td>
    <td><img src='full.png'></td>
  </tr>
  <tr>
    <td>12:50</td>
    <td>천일고속</td>
    <td>고속</td>
    <td><img src='empty.png'></td>
  </tr>
  <tr>
    <td>13:50</td>
    <td>한진고속</td>
    <td>우등</td>
    <td><img src='full.png'></td>
  </tr> 
</table>


</body>
</html>



```







**레이아웃**



```html

<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>

		span,

	</style>

</head>
<body>
<h2>인라인과 블록의 차이점</h2>

<h3>1. 인라인(수평 방향 레이아웃)</h3>
<img src="cheese.jpg">
<span>치즈</span>
<img src="juice.jpg">
<span>오렌지 주스</span>

<h3>2. 블록(수직 방향 레이아웃)</h3>
<p>이것은 단락입니다.</p>
<div>박스 A</div>
<div>박스 B</div>

<h3>1. 세로 메뉴</h3>
<ul id='v_menu'>
	<li>CEO 인사말</li>
	<li>조직도</li>
	<li>전화번호 안내</li>
	<li>찾아오시는 길</li>
</ul>

<h3>2. 가로 메뉴</h3>
<ul id='h_menu'>
	<li class='menus'>회사소개</li>
	<li>|</li>
	<li class='menus'>제품안내</li>
	<li>|</li>
	<li class='menus'>고객센터</li>
	<li>|</li>
	<li class='menus'>매장안내</li>
</ul>




</body>
</html>



```





**기본속성 무시하고 인라인과 블록 사용하기**

```html

<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>

		li{
			list-style-type: none;
		}

		#v_menu {
			width: 150px;
		}

		#v_menu li {
			padding: 5px;
			border-bottom: dotted 1px black;

		}

		#h_menu li {
			display: inline;
		}

		.menu {
			margin: 0 20px 0 20px;
			color: green;
		}

	</style>

</head>
<body>
<h2>인라인과 블록의 차이점</h2>

<h3>1. 인라인(수평 방향 레이아웃)</h3>
<img src="cheese.jpg">
<span>치즈</span>
<img src="juice.jpg">
<span>오렌지 주스</span>

<h3>2. 블록(수직 방향 레이아웃)</h3>
<p>이것은 단락입니다.</p>
<div>박스 A</div>
<div>박스 B</div>

<h3>1. 세로 메뉴</h3>
<ul id='v_menu'>
	<li>CEO 인사말</li>
	<li>조직도</li>
	<li>전화번호 안내</li>
	<li>찾아오시는 길</li>
</ul>

<h3>2. 가로 메뉴</h3>
<ul id='h_menu'>
	<li class='menus'>회사소개</li>
	<li>|</li>
	<li class='menus'>제품안내</li>
	<li>|</li>
	<li class='menus'>고객센터</li>
	<li>|</li>
	<li class='menus'>매장안내</li>
</ul>




</body>
</html>



```





**float속성**

```html

<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>

		*{
			padding: 0;
			margin: 0;
			}

		body {
			margin: 10px;

		}
		li {
			list-style-type: none;
		}

		#image {
			float: left;
			border : solid 1px red;
		}

		#desc {
			float: left;
			width: 300px;
			margin-left: 30px;
			border: solid 1px red;


		}

		#menu {
			float: right;
			border: solid 1px red;
			padding: 20px;
			font-weight: bold;

		}

		#menu li {
			padding: 5px;
			border-bottom: dashed 1px gray;

		}


	</style>

</head>
<body>
<div id='image'>
	<img src='foxtail.jpg'>
</div>
<div id='desc'>
	<h3>강아지풀</h3>
	<p>길가나 들에서 자라는 풀로써 꽃은 9월에 피고 연한 녹색 또는 자주색입니다.</p>
</div>
	<ul id='menu'>
	<li>강아지풀</li>
	<li>패랭이꽃</li>
	<li>할미꽃</li>
	<li>코스모스</li>
</ul>



</body>
</html>



```





### 실습1

**이미지 갤러리**

```html

<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>



		#image {
			width: 960px;
			padding: 30px;
			border : solid 1px #cccccc;
			border-radius: 10px;
			background-color: gray;
			width="1130" height="500px";
			


			
		}

		li{
			list-style-type: none;
			display: inline;
			margin-left: 20px;
		}


	</style>

</head>
<body>

<h3>이미지 갤러리</h3>

<div id='image'>
	<li><img src='고양이1.jpg' width="250px" height="200px" >
	<li><img src='고양이2.jpg' width="250px" height="200px">
	<li><img src='고양이3.jpg' width="250px" height="200px">


</div>

</body>
</html>



```



### 연습2

**수목원**

```html



<!DOCTYPE html>
<html>
<head>

	

	<meta charset="utf-8">
	<style>
li {
	list-style-type: none;

}
#logo {
	float: left;
}

#menu {
	float: right;
	font-size: 14px;
	margin-top: 20px;
}


#menu li {
display: inline;

}
.item {
	margin: 0 20px 0 20px;
}

#main_image {
	clear: both;
	padding-top: 20px
}

</style>





</head>
<body>

<div id='logo'>
	<img src='logo2.png'>
</div>
<ul id='menu'>
	<li class='item'>수목원소개</li>
	<li>|</li>
	<li class='item'>방문안내</li>
	<li>|</li>
	<li class='item'>고객센터</li>
	<li>|</li>
	<li class='item'>공지사항</li>
</ul>
<div id='main_image'>
	<img src='main.jpg'>
</div>


</div>

</body>
</html>



```





연습3

**책 쇼핑**

```html



<!DOCTYPE html>
<html>
<head>

	

<meta charset="utf-8">
<style>
* {
    margin:0;
    padding:0;
}
ul {
    list-style-type: none;
}
#main_title {
    font-family:'맑은고딕';
    margin:10px;
    padding-bottom:6px;
    border-bottom:solid 2px #aaaaaa;
}
.list_item {
    clear: both;
    height: 130px;
    margin: 10px;
    border-bottom: solid 1px #cccccc;
}
.bool1 {
    float:left;
    width: 100px;
	height: 100px;
}
.intro {
    float:left;
    width: 300px;
    margin-left:20px;
}
.price {
    float:left;
    width: 150px;
}
.red {
    font-weight: bold;
    color: red;
}
.small {
    font-size: 12px;
    margin-top:5px;
}
.writer {
    float:left;
    width: 100px;
}

.book1 {
	 width: 100px;
     height: 120px;	 
}

</style>





</head>
<body>
<h2 id = 'main_title'>판매 도서 목록</h2>

<div id='list_item'>
	<div class='book1'>
		
		<img src="책1.jpg" width="250px" height="200px">
	</div>

	<div class='intro'>[갤리온]신경끄기 기술</div>
	    <div class='intro'>[문학동네]여행의 이유</div>

	<ul class = 'price'> 
		<li class='red'>13,500</li>
		<li class='smail'>배송비 2,500</li>


	 </ul>
	 <div class='writer'>작가 </div>

</div>


<div id='list_item'>
	<div class='book1'>
		
		<img src="책1.jpg" width="250px" height="200px">
	</div>

	<div class='intro'>[갤리온]신경끄기 기술</div>
	    <div class='intro'>[문학동네]여행의 이유</div>

	<ul class = 'price'> 
		<li class='red'>13,500</li>
		<li class='smail'>배송비 2,500</li>


	 </ul>
	 <div class='writer'>작가 </div>

</div>

</body>
</html>



```





**속성선택자**

```html



<!DOCTYPE html>
<html>
<head>
<title>CSS3 Selector Basic Page</title>
	
<style>

img[src$=jpg] {
	border:5px solid red;
}

img[src|=강아지1] {
	border : 5px solid green ;

}

img[src|=햄스터1] {
	border : 5px solid  blue;

}



</style>





</head>
<body>

	<img src="고양이1.jpg" width="200" height="250">
	<img src="강아지1.jpg" width="200" height="250">
	<img src="햄스터1.jpg" width="200" height="250">
</body>
</html>



```





**반응선택자**

```html



<!DOCTYPE html>
<html>
<head>
<title>CSS3 Selector Basic Page</title>
	
<style>

h1:hover {
	background-color: black;
	color: white;}

h1:active {
	background-color: yellow;
	color: red;

} 





</style>





</head>
<body>
	<h1>User Action Selector</h1>


</body>
</html>



```



**상태선택자**



```html



<!DOCTYPE html>
<html>
<head>
<title>CSS3 Selector Basic Page</title>
	
<style>

input:enabled {
	background-color: white;
}

input:disabled {
	background-color: gray;
}

input: focus {
	background-color: orange;
}

input: checked {
	background-color: orange;
}


</style>





</head>
<body>

	<h2>Enabled</h2>
	<input />
	<h2>Disabled</h2>
	<input disabled="disabled"/>
	<h2>Focus</h2>
	<input />
	<h2>Checked</h2>
	<input />

</body>
</html>



```



**구조선택자**

```html



<!DOCTYPE html>
<html>
<head>
<title>CSS3 Selector Basic Page</title>
	
<style>

ul {overflow: hidden;}
li {
	list-style: none;
	float: left;
	padding: 15px;
}

li:first-child {border-radius: 10px 0 0 10px;}
li:last-child {border-radius: 0 10px 10px 0;}

li:nth-child(2n) {background-color: #ff0003;}

li:nth-child(2n+1) {background-color: #800000;}


</style>





</head>
<body>
<ul>
	<li>First</li>
	<li>Second</li>
	<li>Third</li>
	<li>Fourth</li>
	<li>Fitrh</li>
	<li>Sixth</li>
	<li>Seventh</li>



</ul>
</body>
</html>



```



**문자선택자**



```html



<!DOCTYPE html>
<html>
<head>
<title>CSS3 Selector Basic Page</title>
	
<style>
	p::first-letter {font-size: 2em;}
	p::first-line {color: red;}



</style>






</head>
<body>
<ul>
<h1>짱구 - 개미송</h1>
<p>개미는(뚠뚠)🐜🐜오늘도(뚠뚠)🐜🐜열심히 일을 하네(뚠뚠)🐜🐜개미는(뚠뚠)🐜🐜언제나(뚠뚠)🐜🐜열심히일을하네(뚠뚠)🐜🐜개미는아무말도하지않지만(띵가띵가)🐜🐜땀을뻘뻘흘리면서(띵가띵가)🐜🐜매일매일을살기위해서열심히일하네(띵가띵가)🐜🐜</p>

<p>한치앞도(뚠뚠)🐜🐜모르는(뚠뚠)🐜🐜험한이세상개미도배짱이도알수없지만그렇지만오늘도행복하다네(뚠뚠)🐜 개미는(뚠뚠)🐜🐜오늘도(뚠뚠)🐜🐜열심히 일을 하네(뚠뚠)🐜🐜개미는(뚠뚠)🐜🐜언제나(뚠뚠)🐜🐜열심히일을하네(뚠뚠)🐜🐜개미는아무말도하지않지만(띵가띵가)🐜🐜땀을뻘뻘흘리면서(띵가띵가)🐜🐜매일매일을살기위해서열심히일하네(띵가띵가)🐜🐜한치앞도(뚠뚠)🐜🐜모르는(뚠뚠) </p>

</ul>
</body>
</html>



```



**반응문자 선택자**

```html



<!DOCTYPE html>
<html>
<head>
<title>CSS3 Selector Basic Page</title>
	
<style>
	p::first-letter {font-size: 2em;}
	p::first-line {color: red;}
	p::selection {background-color: orange; color: red;}



</style>






</head>
<body>
<ul>
<h1>짱구 - 개미송</h1>
<p>개미는(뚠뚠)🐜🐜오늘도(뚠뚠)🐜🐜열심히 일을 하네(뚠뚠)🐜🐜개미는(뚠뚠)🐜🐜언제나(뚠뚠)🐜🐜열심히일을하네(뚠뚠)🐜🐜개미는아무말도하지않지만(띵가띵가)🐜🐜땀을뻘뻘흘리면서(띵가띵가)🐜🐜매일매일을살기위해서열심히일하네(띵가띵가)🐜🐜</p>

<p>한치앞도(뚠뚠)🐜🐜모르는(뚠뚠)🐜🐜험한이세상개미도배짱이도알수없지만그렇지만오늘도행복하다네(뚠뚠)🐜 개미는(뚠뚠)🐜🐜오늘도(뚠뚠)🐜🐜열심히 일을 하네(뚠뚠)🐜🐜개미는(뚠뚠)🐜🐜언제나(뚠뚠)🐜🐜열심히일을하네(뚠뚠)🐜🐜개미는아무말도하지않지만(띵가띵가)🐜🐜땀을뻘뻘흘리면서(띵가띵가)🐜🐜매일매일을살기위해서열심히일하네(띵가띵가)🐜🐜한치앞도(뚠뚠)🐜🐜모르는(뚠뚠) </p>

</ul>
</body>
</html>



```

**링크선택자**

```html
<!DOCTYPE html>
<html>
<head>
<title>CSS3 Selector Basic Page</title>
	
<style>
a { text-decoration: none; }
a:visited {color: green;}

a:link::after{content: '-'attr(href);}


</style>

</head>
<body>
<h1><a>Nothing</a></h1>
<h1><a href="http://hanb.co.kr">Hanbit Media</a></h1>
<h1><a href="http://www.w3.org/">W3C</a></h1>
<h1><a href="https://github.com/">Github</a></h1>

</body>
</html>



```

**visibility**

**대상을보이거나 보이지 않게 지정하는 속성이다.**

```html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
    <title>CSS3 Style Property Basic</title>
    <style>
        p:nth-child(1) { }
        p:nth-child(2) { font-size: 100%; }
        p:nth-child(3) { font-size: 150%; }
        p:nth-child(4) { font-size: 200%; }

        table {
        	visibility: collapse;
        }
    </style>
</head>
<body>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <table>
        <tr><td>Test</td><td>Test</td></tr>
        <tr><td>Test</td><td>Test</td></tr>
        <tr><td>Test</td><td>Test</td></tr>
    </table>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
</body>
</html>
```



**opacity**

대상의 투명도를 지정하는 속성이다.

```html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
    <title>CSS3 Style Property Basic</title>
    <style>
        p:nth-child(1) { }
        p:nth-child(2) { font-size: 100%; }
        p:nth-child(3) { font-size: 150%; }
        p:nth-child(4) { font-size: 200%; }

        table {
        	background-color: black;
        	color: white;

        	opacity: 0.1;
        }



    </style>
</head>
<body>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <table>
        <tr><td>Test</td><td>Test</td></tr>
        <tr><td>Test</td><td>Test</td></tr>
        <tr><td>Test</td><td>Test</td></tr>
    </table>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
</body>
</html>
```





**position**

```html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
    <title>CSS3 Style Property Basic</title>
    <style>
        .box {
        	width: 100px; height: 100px;
        	position: absolute;
        }

        .box:nth-child(1) {
        	background-color: red;
        	left: 10px; top: 10px;
        }

    	.box:nth-child(2) {
        	background-color: green;
        	left: 50px; top: 50px;
        }
    	.box:nth-child(3) {
        	background-color: blue;
        	left: 90px; top: 90px;
        }

    </style>
</head>
<body>
  <div class="box red"></div>
  <div class="box green"></div>
  <div class="box blue"></div>

</body>
</html>
```





**z-index속성**

HTML 태그는 아래 입력한 태그가 위로 올라온다.

큰 값을 입력할 수록 위로 올라온다.



```html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
    <title>CSS3 Style Property Basic</title>
    <style>
        .box {
        	width: 100px; height: 100px;
        	position: fixed;
        }

        .box:nth-child(1) {
        	background-color: red;
        	left: 10px; top: 10px;

        	z-index: 100;
        }

    	.box:nth-child(2) {
        	background-color: green;
        	left: 50px; top: 50px;
        	z-index: 10;
        }
    	.box:nth-child(3) {
        	background-color: blue;
        	left: 90px; top: 90px;
        	z-index: 1;
        }

    </style>
</head>
<body>
  <div class="box red"></div>
  <div class="box green"></div>
  <div class="box blue"></div>

</body>
</html>
```





**overflow속성**

내부의 요소가 부모의 범위를 벗어날 때 어떻게 처리할지 지정하는
속성이다.

hidden 영역을 벗어나면 자른다.

scroll 영역을 벗어난 부분은 스크롤처리 한다.



```html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
 <style>
        .box {
            width: 100px; height: 100px;
            position: absolute;
        }
        .box:nth-child(1) {
            background-color: red;
            left: 10px; top: 10px;

            z-index: 100;
        }
        .box:nth-child(2) {
            background-color: green;
            left: 50px; top: 50px;

            z-index: 10;
        }
        .box:nth-child(3) {
            background-color: blue;
            left: 90px; top: 90px;

            z-index: 1;
        }
        
        body > div {
            width: 400px; height: 100px;
            border: 3px solid black;

            position: relative;
            overflow: scroll;
        }
    </style>
</head>
<body>
    <h1>Lorem ipsum dolor amet</h1>
    <div>
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
    </div>
    <h1>Lorem ipsum dolor amet</h1>
</body>
</html>
```





**벤더 프리픽스**



```html
<!DOCTYPE html>
<html>
<head>
<style> 
div {
  width: 100px;
  height: 100px;
  background: red;
  -webkit-transition: width 2s; /* For Safari 3.1 to 6.0 */
  transition: width 1s;
}

div:hover {
  width: 600px;
}
</style>
</head>
<body>

<h1>The transition Property</h1>

<p>Hover over the div element below, to see the transition effect:</p>
<div></div>

<p><b>Note:</b> This example does not work in Internet Explorer 9 and earlier versions.</p>

</body>
</html>

```

