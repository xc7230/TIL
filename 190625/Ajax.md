Ajax(Asynchronous JavaScript)

Ajax - 사용자 요청 처리 과정

사용자가 이벤트(마우스 클릭 등)를 발생
자바스크립트는 DOM을 사용해서 필요한 정보를 구함
XMLHttpRequest 객체를 통해서 웹 서버에 요청을 전달
웹 서버는 XMLHttpRequest로부터의 요청을 알맞게 처리
웹 서버는 결과를 XML이나 단순 텍스트로 생성해서
XMLHttpRequest에 전송
클라이언트 브라우저로 서버로부터의 응답이 도착하면
XMLHttpRequest 객체는 자바스크립트에 도착 사실을 알림
자바 스크립트는 응답 데이터와 DOM을 조작해서 사용자 화면에 반
영

XMLHttpRequest(XHR)객체

```html

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8"> 
  <title>Ajax처리</title> 
</head>
 

<script>
window.onload = function(){         //이벤트 발생

  var req = new XMLHttpRequest(); //1. XMLHttpRequest
  req.onloadstart= function(){
    console.log("loadstart : 요청을 보낼때");
    }
  req.onload = function(){
    console.log("load : 요청 성공, 응답 가져올 수 있을 때");
    }
  req.onloadend = function(){
    console.log("loadend : 요청 완료");
    }
  req.onprogress = function(){
    console.log("progress : 데이터를 주고 받을 때");
    }
  req.onreadystatechange = function(){
    if(req.readyState==4){
       if(req.status ==200){
    document.getElementById("view").innerHTML = req.responseText; 
         }
    }
  } //응답 처리 함수
  req.open("GET", "data.txt"); //2. 요청 보낼 준비
  req.send(null); //3. 요청 보냄
  };



</script>

<body>
  <p id = "view"></p>
</body>
</html>
```

 

```html

<!DOCTYPE html>
<html>
<head>
<meta  charset="UTF-8">
	<title></title>
	<style>
		.image_panel{
			border:1px solid eeeeee;
			text-align:center;
			margin:5px;
		}
		.image_panel .title{
			font-size:9pt;
			color:#ff0000;
			
		}
		
	</style>
	 
	<script src="ajax_json.js"></script>	 
</head>

<body>
	<div>
		<button id="btn_load">이미지 읽어들이기</button>
	</div>
	<div id="image_container">
		<!-- 1. 이곳에 이미지를 넣어주세요-->
	</div>
	
	<!-- 2. 이 내용은 이미지 패널 템플릿입니다. -->
	<div style="display:none;" id="image_panel_template">
		<div class="image_panel">
			<img >
			<p class="title"></p>
		</div>
	</div>
</body>
</html>

```



```html
var req;
window.onload=function() {
	document.querySelector("#btn_load").onclick =function(){	 
	var url = "images.jsp" ; // 요청 URL설정	 
	req = new XMLHttpRequest(); // XMLHttpRequest객체 생성
	req.onreadystatechange =createImages;
	req.open("Get", url, "true");	     
	req.send(null);// 서버로 요청을 보냄	 
  };
}

function createImages(){
  if(req.readyState == 4){ // 요청객체의 상태가 모든 데이터를 받을 수 있는 상태로 완료된 경우
	if(req.status == 200){ // 서버로부터 응답받는 HTTP상태가 정상인 경우 수행	
		console.log(req.responseText)
 		var obj = JSON.parse(req.responseText);
 		var images = obj["rows"];
		var strDOM = "";
		for(var i=0;i<images.length;i++){
			// 2. N번째 이미지 정보를 구합니다.
			var image = images[i];			
			// 3. N번째 이미지 패널을 생성합니다.
			strDOM +='<div class="image_panel">'
			strDOM +='    <img src="'+image.url+'">';
			strDOM +='    <p class="title">'+image.title+'</p>';
			strDOM +='</div>';						
		}		
		document.querySelector("#image_container").innerHTML =
			strDOM;
	 }else{
			alert("처리중 에러가 발생했습니다.");
	 }
  }
}	

```



```html
<%@ page contentType = "text/plain; charset=utf-8"
pageEncoding = "utf-8"%>

{"rows":[
	{"title":"img1","url":"images/img1.jpg"},
	{"title":"img2","url":"images/img2.jpg"},
	{"title":"img3","url":"images/img3.jpg"},
	{"title":"img4","url":"images/img4.jpg"},
	{"title":"img5","url":"images/img5.jpg"}
	
]}

```

# 크로스 오리진

## JSONP

```html

<!DOCTYPE html>
<html>
<head>
<meta  charset="UTF-8">
<script>
	function show(data) {
		console.log("name: " + data.name);
		console.log("price: " + data.price);
	}

	window.onload = function() {
		var url = "http://70.12.50.130:9000/jsonp.js";
        //다음 사이트에서 자료를 불러온다.
		var script = document.createElement("script");
		script.setAttribute("src", url);
		document.getElementsByTagName('head')[0].appendChild(script);
	}

</script>
	<style>
	
		
	</style>
	 
	 
</head>

<body>
	
</body>
</html>

```

jsonp.js

```html
show({"name" : "apple", "price" : 100});
```





CORS

postMessage

