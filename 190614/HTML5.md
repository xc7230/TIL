```html
<!DOCTYPE html>
<html>

<head>
	<meta   charset="utf-8" />
	<title> embed </title>
</head>


<body>

<iframe src="https://www.naver.com">
  <p>Your browser does not support iframes.</p>
</iframe>

<em>Emphasized text</em><br>
<strong>Strong text</strong><br>
<code>A piece of computer code</code><br>
<samp>Sample output from a computer program</samp><br>
<kbd>Keyboard input</kbd><br>
<var>Variable</var>


<p>Do not forget to buy <mark>milk</mark> today.</p>

<p><strong>Note:</strong> The mark tag is not supported in Internet Explorer 8 and earlier versions.</p>


<p>Display a gauge:</p>
<meter value="2" min="0" max="10">2 out of 10</meter><br>
<meter value="0.6">60%</meter>

<p><strong>Note:</strong> The &lt;meter&gt; tag is not supported in Internet Explorer, Edge 12, Safari 5 and earlier versions.</p>

<img src="navi.jpg" alt="" usemap="#Map1" /> 
<map name = "Map1">
	<area shape="rect" coords="0, 0, 40, 35"
	href=https://mail.naver.com" alt="메일" border = "0" />
	<area alt="까페" href="https://section.cafe.naver.com/"
	shape="rect" border ="0" coords="40, 0, 70, 35"  />
	<area alt="블로그" href="https://section.blog.naver.com/"
	shape="rect" border ="0" coords="40, 0, 115, 35"  />


</map>





<p>뮤직 비디오</p>
<embed src="https://www.youtube.com/embed/kOHB85vDuow" width="640" height="360" allowfullscreen>
<p>구글로 이동하기</p>
<a href="https://www.google.com/"><img src="google.png"></a>
<br>
<br>
<form>
	<label>점심 메뉴를 고르시오.
		<select>
			<optgroup label="한식">
				<option>비빔밥</option>
				<option>갈비탕</option>
				<option>김치찌게</option>
				<option>된장찌게</option>



			</optgroup>

			<optgroup label="중식">
				<option>짜장면</option>
				<option>짬뽕</option>
				<option>탕슉</option>


			</optgroup>


			<OPTGROUP label="양식">
				<option>돈가스</option>
				<option>파스타</option>

			</OPTGROUP>

		</select>


	</label>

</form>





<h2>국내 주요 사이트</h2>
<p><a href="https://www.naver.com/" target="site"> 네이버</a></p>
<p><a href="https://www.daum.net/" target="site"> 다음</a></p>
<p><a href="https://www.google.com/" target="site"> 구글</a></p>

<iframe width ="800" height = "300" src="https://www.yes24.com/" name="site">

</body>
</html>

```



## 연습



## 강아지

```html

<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="utf-8">
	<title>강아지 키우기</title>
	<link href="style.css" rel="stylesheet" type="text/css">  
</head> 
<body>


	<header>
		<h1>입양하기</h1>
		<nav>
			<ul>
				<li><a href="#">애완견 종류</a></li>
				<li><a href="#">입양하기</a></li>
				<li><a href="#">건강돌보기</a></li>
				<li><a href="#">더불어살기</a></li>
			</ul>
		</nav>
	</header>
	<section>
		<h2>강아지 용품 준비하기</h2>
		<img src="puppy.jpg" id="puppy">
		강아지 집
		강아지가 편히 쉴 수 있는 포근한 집이 필요합니다. 강아지의 집은 강아지가 다 큰 후에도 계속 쓸 수 있는 집으로 구입하세요.집을 구입하실 때는 박음질이 잘 되어 있는지, 세탁이 간편한 제품인지 꼭 확인하시고 고르시는 것이 좋습니다.
		
		강아지 먹이
		강아지의 먹이는 꼭 어린 강아지용으로 나와있는 사료를 선택하세요. 강아지들은 사람에 비해 성장속도가 8배정도 빠르답니다. 따라서 강아지에게는 성장속도에 맞는 사료를 급여하셔야 합니다. 사람이 먹는 음식을 먹게 되면 양념과 향신료에 입맛이 익숙해지고, 비만이 될 가능성이 매우 높아집니다. 강아지용 사료는 생후 12개월까지 급여하셔야 합니다.
		
		밥그릇, 물병
		밥그릇은 쉽게 넘어지지 않도록 바닥이 넓은 것이 좋습니다.물병은 대롱이 달린 것으로 선택하세요. 밥그릇에 물을 주게 되면 입 주변에 털이 모두 젖기 때문에 비위생적이므로 대롱을 통해서 물을 먹을 수 있는 물병을 마련하시는 것이 좋습니다.
		
		이름표, 목줄
		강아지를 잃어버릴 염려가 있으니 산책할 무렵이 되면 이름표를 꼭 목에 걸어주도록 하세요. 그리고 방울이 달린 목걸이를 하고자 하실 때는 신중하셔야 합니다. 움직일 때마다 방울이 딸랑 거리면 신경이 예민한 강아지들에게는 좋지 않은 영향을 끼칠 수 있기 때문입니다.
	</section>
	<footer>
		<p>Copyright 2012 funnycom</p>
	</footer>
</body>
</html>
```



### css

```html

@charset="utf-8";
body {
	font-family : "맑은 고딕","고딕","굴림";
}


header {
	width: 620px;
	margin-right : auto;
	margin-left : auto;
	background-color : #069;
	padding: 10px;
	overflow: hidden;

}

header h1 {
	width:140px;
	float : left;
	color: #ffffff;
	}



header nav {
	width:460px;
	float : right;
	margin-top:15px;
}

nav ul{
	
	list-style-type : none;
}

nav ul li {
	display: inline;
	float: left;
	margin-top:10px;
}



nav ul li a{

	color: white;
	text-decoration: none;
}

p {
	font-size:15px;
	line-height:20px
}

h1 {
	font-size:2em;
}

section{

	width: 600px;
	margin-right : auto;
	margin-left : auto;
	border: 5px solid #333;
	padding: 15px;
	
}

img#puppy {
float: right;
margin-left: 10px;
border: 1px solid #ccc;
box-shadow: -2px 3px 5px #000;
-moz-box-shadow: -2px 3px 5px #000;
-webkit-box-shadow

}
```







## 회원가입

```html
<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>frame</title>
<style>
	body {
		background: #666;
	}
	#container {
		width: 450px;
		margin: 15px auto;
		padding: 10px;
		border:1px solid #666;
		border-radius: 10px;
		background: white;


	}

	ul {
		list-style-type: none;
	}

	ul li {
		line-height: 25px;
		margin-bottom: 10px;
	}

	label {
		width: 80px;
		float: left;
		text-align: right;
		padding-right: 5px;
		font-weight: bold;
	}
	.centered {
		text-align: center;
	}

</style>


</head>
<body>
<div id = "container"
<h1>가입정보</h1>
<form action ="register.jsp id = "reg_form">
	<ul>
		<li>
			<label for="uname">이름</label>
			<input type="text" id="uname" placeholder="홍길동">
		</li>
		<li>
			<label for="email">이메일 </label>
			<input type="email" id="email" placeholder="asdf@asdf.com">
		</li>
		<li>
			<label for="pw">비밀번호</label>
			<input type="password" id="pw" required>


		</li>
		<li>
			<label for="sex">성별</label>
			<select id = "sex">
				<option value="w">여성 </option>
				<option value="m">남성 </option>


			 </select>

		</li>



	</ul>
	<div class="centered">
		<input type="submit" value="가입하기 " class="centered">
		

	</div>
		




</form>


 
</body>
</html>
```

