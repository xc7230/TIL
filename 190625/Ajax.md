# Ajax(Asynchronous JavaScript)

XMLHttpRequest 라는 자바스크립트의 객체를 이용하여 웹서버와 비동기 통신하고 DOM을 이용 하여 웹 페이지를 동적으로 갱신하는 프로그램 기법



## Ajax - 사용자 요청 처리 과정

- 사용자가 이벤트(마우스 클릭 등)를 발생
- 자바스크립트는 DOM을 사용해서 필요한 정보를 구함
- XMLHttpRequest 객체를 통해서 웹 서버에 요청을 전달
- 웹 서버는 XMLHttpRequest로부터의 요청을 알맞게 처리
- 웹 서버는 결과를 XML이나 단순 텍스트로 생성해서
- XMLHttpRequest에 전송
- 클라이언트 브라우저로 서버로부터의 응답이 도착하면
- XMLHttpRequest 객체는 자바스크립트에 도착 사실을 알림
- 자바 스크립트는 응답 데이터와 DOM을 조작해서 사용자 화면에 반
  영

## XMLHttpRequest(XHR)객체

1.XMLHttpRequest  객체를 생산한다.

2.서버와 통신할 때 사용할 처리 방법을 등록한다.

3.요청을 전송하고 통신을 시작한다.





**open("Get", url, "true")** 첫번째 파라미터는 HTTP 요구 방식 GET,POST,HEAD 중의 하나를 쓴다.

두번째 파라미터는 요구하고자하는 URL  

세번째 파라미터가 true이면 비동기식(  어떤 작업을 요청했을 때 그 작업이 종료될 때까지 기다린 후 다음(다른) 작업을 수행하는 방식) 으로 수행

   

**send()** 메소드는 작성된 Ajax 요청을 서버로 전달

send() GET방식

send(문자열)  POST방식



```html

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8"> 
  <title>Ajax처리</title> 
</head>
 

<script>
window.onload = function(){         //이벤트 발생

  var req = new XMLHttpRequest(); //XMLHttpRequest객체의 생성
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
  req.onreadystatechange = function(){  //onreadystatechange 응답이 왔을때 수행해야 하는 함수를 넣는다.
    if(req.readyState==4){
        
        //readyState : 0 open메서드가 호출된 상태가 아니다.
        //			   1 로드중:open메서드는 호출되었지만 send 메서드가 호출되지 않았다.
        //			   2 로드완료:send메서드는 호출되었지만 응답이 되돌아오지 않았다.
        //			   3 응답수신중:응답 행과 응답 헤더는 가져왔지만 메시지 본문을 가져오지 못했다.
        //			   4 수신완료:모든 응답 메시지 수신한다.
        
        
        
       if(req.status ==200){
    document.getElementById("view").innerHTML = req.responseText; 
         }
    }
  } //응답 처리 함수
  req.open("GET", "data.txt"); //2. 요청 보낼 준비
  req.send(null); //3. 요청 보냄
  					//data.txt를 불러온다.
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
	 
	<script src="ajax_json.js"></script> //ajax_json.js을 불러온다.
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
		var script = document.createElement("script")//엘리먼트 생성
		script.setAttribute("src", url); //선택한 요소의 속성을 부여해준다. setAttribute(속성이름, 속성값)
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





### 부분페이지 갱신, POST요청, XML응답처리



```html

<!DOCTYPE html>
<html>
  <head>
    <meta  charset="utf-8">
    <title>부분페이지 동적 갱신</title>     
    <link rel="stylesheet" href="partPage.css" type="text/css" />
    <script src="partPage.js"></script>
  </head>
  <body>
    <h3>부분페이지 갱신, POST요청, XML응답처리</h3>
    <table border="1">
      <tr><td colspan="2" align="center"><font size=15><b>우리회사</b></font></td></tr>
      <tr>
         <td><form action="#">
               <div id="confirmed">
                 <table>
                    <tr>
                      <td>아이디</td>
                      <td><input type="text" id="userid" size="15" maxlength="12"/></td>
                    </tr>
                    <tr>
                      <td>비밀번호</td>
                      <td><input type="password" id="userpwd" size="15" maxlength="12"/></td>
                    </tr>
                    <tr><td colspan="2" align="center">
                        <input type="button" id="login" value="로그인" /></td>
                    </tr>
                </table>
              </div>
             </form>
         </td>
         <td width="400"><img src="images/img1.jpg"></td>
      </tr>
      <tr><td colspan="2" align="center">찾아오시는길 |회사소개|정보보호정책</td></tr>
    </table>
  </body>
</html>
```





```html

var req; //XMLHttpRequest객체를 저장할 변수를 전역변수로 선언
window.onload= function(){ //브라우저가 로드 되었을 때 처리를 실행하는 메소드(이벤트 핸들러)를 정의
	req = new XMLHttpRequest(); //XMLHttpRequest객체 생성
	document.getElementById("login").onclick = startMethod;
};

function startMethod(){ 
	var uid = document.getElementById("userid").value;  
    var upwd = document.getElementById("userpwd").value;  
    var url = "part.jsp"; //요청 URL설정
	req.onreadystatechange = resultProcess; //응답결과를 처리메소드인 resultProcess()메소드 설정 
    req.open("post", url, "true");//서버의 요청설정 - url변수에 설정된 리소스를 요청할 준비
    req.setRequestHeader("Content-type", 
    		"application/x-www-form-urlencoded"); 
	req.send("userid="+uid+"&userpwd="+upwd);//서버로 요청을 보냄
};

function resultProcess(){//partPageDBUse.jsp페이지에서 응답결과가 오면 자동으로 실행
	if(req.readyState == 4){ //요청객체의 상태가 모든 데이터를 받을 수 있는 상태로 완료된 경우
	  if(req.status == 200){ //서버로부터 응답받는 HTTP상태가 정상인 경우 수행
		 cofirmedProcess(); //cofirmedProcess()메소드 호출
	  }
	}
}

function cofirmedProcess(){//로그인의 성공과 실패에 따라 표시되는 내용을 결정하는 메소드
    var result =req.responseXML.getElementsByTagName("result")[0].firstChild.data;
    var name = req.responseXML.getElementsByTagName("id")[0].firstChild.data;
     
    if (result == 1){//사용자 인증성공시
      var str="<table><tr><td align='center'><b>"+name+"</b> 님 오셨구려..</td></tr>"
      str+="<tr><td align='center'><input type='button' id='logout' value='로그아웃' onclick ='logoutMethod()'/></td></tr></table>"
    	  document.getElementById("confirmed").innerHTML = str;
    }else if(result==0){//사용자 인증실패시 - 비밀번호가 틀림
      alert("비밀번호가 맞지 않습니다.\n다시 입력해 주시기 바랍니다.");
      document.getElementById("userid").value=name;
      document.getElementById("userpwd").value="";
      document.getElementById("userpwd").focus();
    }else{//사용자 인증실패시 - 아이디가가 틀림
      alert("아이디가 맞지 않습니다.\n다시 입력해 주시기 바랍니다.");
      document.getElementById("userid").value="";
      document.getElementById("userpwd").value="";
      document.getElementById("userid").focus();
    }
}



function logoutMethod(){	 
	var url = "partPagelogout.jsp?timestamp="+ new Date().getTime(); //요청 URL설정
	xhr.onreadystatechange = logoutProcess; //응답결과를 처리메소드인 logoutProcess()메소드 설정 
    xhr.open("Get", url, "true");//서버의 요청설정 - url변수에 설정된 리소스를 요청할 준비
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded"); 
	xhr.send(null);//서버로 요청을 보냄
}


function logoutProcess(){//partPageDBUselogout.jsp페이지에서 응답결과가 오면 자동으로 실행
	if(xhr.readyState == 4){ //요청객체의 상태가 모든 데이터를 받을 수 있는 상태로 완료된 경우
	  if(xhr.status == 200){ //서버로부터 응답받는 HTTP상태가 정상인 경우 수행
	       
		 var str="<table><tr><td>아이디</td><td><input type='text' id='id' size='15' maxlength='12'/></td></tr>";
         str+="<tr><td>비밀번호</td><td><input type='password' id='passwd' size='15' maxlength='12'/></td></tr>";
         str+="<tr><td colspan='2' align='center'><input type='button' id='login' value='로그인' onclick ='startMethod()'/></td></tr></table>" ;          
         
         document.getElementById("confirmed").innerHTML = str;
	  }
	}
}
```

