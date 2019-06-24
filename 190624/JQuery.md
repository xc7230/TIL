



# 체이닝



```javascript

<!doctype html>
<html lang="ko">
 <head>
  <meta charset="UTF-8">  
  <title>jQuery 기본</title>
  <style>  
   
</style>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script>  
  $(document).ready(function(){	 
	  $('h3').css('background', 'Orange').filter(':even').css('color', 'Green').end().filter(':odd').css('color', 'Blue');
	 
});

//filter 'h3'에서 인덱스 번로 기준으로 짝수번째의 색을.css를 이용해 바꾼다.  홀수는 odd
  </script>
 </head>
 <body>
 <h3>item - 0</h3>
<h3>item - 1</h3>
<h3>item - 2</h3>
<h3>item - 3</h3>
<h3>item - 4</h3>
<h3>item - 5</h3>

 
 </body>
</html>

```



eq() 메서드

```java

<!doctype html>
<html lang="ko">
 <head>
  <meta charset="UTF-8">  
  <title>jQuery 기본</title>
  <style>  
   
</style>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script>  
  $(document).ready(function(){	 
	  //$('h3').css('background', 'Orange').filter(':even').css('color', 'Green').end().filter(':odd').css('color', 'Blue');
	 $('h3').eq(0).css('color', 'Green');
	 $('h3').eq(-1).css('color', 'Blue');

	 $('h3').first().css('color', 'Cyan');
	 $('h3').last().css('color', 'magenta');
//h3에서 .위치를 지정하고. 스타일을 바꾼다.
});

  </script>
  
	 <!--  $()는 jQuery에서 함수를 호출한다.
	 .eq(index) index는 0이 초기값 위치를 표시한다. -->
 </head>
 <body>
 <h3>item - 0</h3>
<h3>item - 1</h3>
<h3>item - 2</h3>
<h3>item - 3</h3>
<h3>item - 4</h3>
<h3>item - 5</h3>
 </body>
</html>

```





## add() 메서드

is는 판별할때

$() 메서드의 매개 변수에 생성한 XML 문서 객체 입력
$() 메서드에는 문서 객체를 곧바로 넣을 수 있음
find() 메서드를 사용해 friend 태그 선택
friend 태그는 총 세 개이므로 each() 메서드 사용

```javascript

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
 div{  margin:10px;
       border:3px Solid Black;
       border-radius:10px;
       float:left;
       width:120px; height:120px;
       text-align:center;
        }
    </style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

<script>
$(document).ready(function() {

	var xmlDoc = $.parseXML(xml); //xml문서를 객체로 가져와 사용 가능
	$(xmlDoc).find('friend').each(function(index) {
        //each는 배열 관리하는 메서드이다.  선택자를 사용하여 생성된 배열을 사용한다.

		var output = '';
		output += '<div>';
		output += '      <h1>' + $(this).find('name').text() + '</h1>';
		output += '      <p>' + $(this).find('language').text() + '</p>';
		output += '</div>';

		document.body.innerHTML +=output;

	})
})


</script>

<script>
        // 변수를 선언합니다.
        var xml = '';
        xml += '<friends>';
        xml += '    <friend>';
        xml += '        <name>연하진</name>';
        xml += '        <language>Ruby</language>';
        xml += '    </friend>';
        xml += '    <friend>';
        xml += '        <name>윤명월</name>';
        xml += '        <language>Basic</language>';
        xml += '    </friend>';
        xml += '    <friend>';
        xml += '        <name>윤하린</name>';
        xml += '        <language>C#</language>';
        xml += '    </friend>';
        xml += '</friends>';

        $(document).ready(function () {
           
        });
    </script>
</head>
<body>

</body>
</html>
```









# attr() 메서드

```javascript

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
 div{  margin:10px;
       border:3px Solid Black;
       border-radius:10px;
       float:left;
       width:120px; height:120px;
       text-align:center;
        }
    </style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script> 

        // $(document).ready(function () {
        //   $('img').attr('width', function(index) {
        //     return (index + 1)*100;
        //   })
           
        // });
    
    	///attr()은 요소의 속성의 값을 가져오거나 속성을 추가한다. 'img' 요소의 'width'속성의 값을 가져온다. 속성의 값은 function(index)으로 한다.

  $(document).ready(function() {
    $('img').attr({
      width: function (index) {
        return (index + 1 )* 100;
      },
      height: 100
    })
  })
    </script>
</head>
<body>
   <img src="Koala.jpg">
   <img src="Jellyfish.jpg">
   <img src="Penguins.jpg">
</body>
</html>
```









# 문서 객체의 스타일 추가

```javascript

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>

    </style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script> 
  $(document).ready(function() {
    var color = ['Red', 'White', 'Purple'];


  $('h1').css({
    color: function(index) {
      return color[index];
    },
    //h1을 불러오고 color에 속성 값을 function(index)를 이용해 지정해준다. color 배열만들걸 리턴해준다.      
      
    backgroundColor: 'Black'
  });  
  });

    </script>
</head>
<body>
  <h1>Header - 0</h1>
  <h1>Header - 1</h1>
  <h1>Header - 2</h1>

</body>
</html>
```





# 문서 객체의 내부 검사, 문서 객체의 내부 추가 ,

```javascript

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
 div{  margin:10px;
       border:3px Solid Black;
       border-radius:10px;
       float:left;
       width:120px; height:120px;
       text-align:center;
        }
    </style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script> 
 $(document).ready(function () {
  //변수를 선언 합니다.
  var headers = $('h1').html();
    	//.html은 h1의 내용을 headers에 저장합니다.
	//$( 'div' ).html( '<h1>Lorem</h1>' );이면 div의 요소의 내용을 <h1>Lorem</h1>로 바꾼다.
  //출력합니다.
  alert(headers);
	//Header - 0을 출력한다.
  //   var html = $('h1').text();
  // //출력합니다.
  // alert(texts);
  

 //  $('div').html(function(index) {
 //    return("<h3>Header-"+index+"</h3>");
 // });
  $('div').text(function(index){
    return("<h3>Header-" + index + "</h3>");
	///.text은 선택한 요소 안의 내용을 가져오거나 다른 내용으로 바꾼다. .html()과 비슷하지만 태그의 처리가 다르다 문자열만 출력한다. 

  }) ;  
    });
    </script>
</head>
<body>
    
   <h1> Header-0 </h1>
   <h1> Header-1 </h1>
   <h1> Header-2 </h1>
   <div></div>
   <div></div>
   <div></div>
</body>
</html>
```





# 문자객체의추가

```javascript

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
div { border: 1px solid black;
      width : 300px;
      height : 300px;}
</style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script> 
 $(document).ready(function () {

 	$('<p></p>').html('<mark>appendTo</mark>').appendTo('div');
  	$('<p></p>').html('<mark>prependTo</mark>').prependTo('div');
 	$('<p></p>').html('<mark>insertAfter</mark>').insertAfter('div');
 	$('<p></p>').html('<mark>insertBefore</mark>').insertBefore('div');


 	$('div').append(function(){
 		return $('<p></<p>').html('<mark>append</mark>');
 	})
 	$('div').prepend(function(){
 		return $('<p></<p>').html('<mark>prepend</mark>');
 	})
 	$('div').before(function(){
 		return $('<p></<p>').html('<mark>before</mark>');
 	})
 	$('div').after(function(){
 		return $('<p></<p>').html('<mark>after</mark>');
 	})


    });
    </script>
</head>
<body>
 <h3>문서 객체를 추가<h3>
 A.appendTo(B) : B의 마지막 자식 요소로 A요소를 추가 <br>
 A.prependTo(B) : B의 첫번째 자식 요소로 A요소를 추가 <br>
 A.insertAfter(B) : B의 형제노드로서 A요소를 B의 다음에 추가<br>
 A.insertBefore(B) : B의 형제노드로서 A요소를 B의 앞에 추가<br>
 A.append(B) : A의 마지막 자식 요소로 B요소를 추가 <br>
 A.prepend(B) : A의 첫번째 자식 요소로 B요소를 추가 <br>
 A.after(B) : A의 형제노드로서 B요소를 A의 다음에 추가<br>
 A.before(B) : A의 형제노드로서 B요소를 A의 앞에 추가<br> 
 <div>내용</div>
   
    
</body>
</html>
```



# 문서 객체의 이동

```javascript

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<style>
 div{  margin:10px;
       border:3px Solid Black;
       border-radius:10px;
       float:left;
       width:120px; height:120px;
       text-align:center;
        }
    </style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script> 
$(document).ready(function() {
  $('img').css('width', 250);
//img 스타일 크기를 250 px로 맞춘다.


  setInterval(function() {
//setInterval은 반복동작을 시키는데 쓰인다.

    $('img').first().appendTo('body');
  }, 200);
//img의 요소를 (.css('width', 250))을 body 첫번째 요소에 이동 시킨다 2초동안. 
})
    </script>
</head>
<body>
   <img src="Koala.jpg">
   <img src="Jellyfish.jpg">
   <img src="Penguins.jpg">
</body>
</html>
```





# 문서 객체의 복제

```javascript

<!doctype html>
<html lang="ko">
 <head>
  <meta charset="UTF-8">  
  <title>jQuery 문서 조작</title>
  <style>  
   
</style>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script>  
  $(document).ready(function(){	
  $('img').css('width', 200);
        //img안에 있는 요소의 스타일을 바꾼다 

  $('div').append($('img').clone());	 
  //img의 클론을 만들어서   div에 넣는다. 

});
  </script>
 </head>
 <body>
<h3>문서 객체 복제</h3>
clone() : 객체 복제<br> 
 <img src="Koala.jpg" />
 <div></div>
 </body>
</html>

```



# 이벤트

```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<style>
.reverse {
   background:black;
   color:white;
}
</style>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function(){

	$("h1").on("click", function() {
		$(this).html(function(index, html) {
			return html +"+";
		})

		//.on은 이벤트 객체 특정요소를 바인딩 하기 위해 사용한다.
		$(this).off(click);
		///off 이벤트 해제하기 click이벤트를 해제한다.
	});  //+누를떄마다 생김 




// $("h1").one("click", function() {
// 	$(this).html(function(index, html) {
// 		return html + "+";
// 	})

// })//한번 생성


// $("h1").on( {
// 	mouseenter : function()  {$(this).addClass("reverse");},

// 	//mouseenter : 마우스 진입 감지 
// 	//addClass : 클래스를 추가한다.
// 	//reverse : 종료문
// 	mouseleave : function() {$(this).removeClass("reverse");}
// 	//mouseleave : 요소에서 마우스가 떠날때 특정 이벤트 발생
// 	//removeClass : 선택한 요소의 클래스 값을 제거한다.
// });  //마우스 포인터를 대면 검은색 바탕으로
	
})
</script>
</head>
<body>
<h1>Click</h1>
</body>
</html>
```





# 이벤트 제거하기

```javascript


<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>javascript:event</title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
	$('a').click(function(event) {
		event.preventDelfault();
	});
	$('#f1').submit(function(event) {
		event.preventDelfault();
	})
	
});
 
</script>
</head>
<body>
 

<a href="http://www.multicampus.co.kr">www.multicampus.co.kr</a><br>
<form  id = "f1" method="get" action="data.jsp">
email : <input type=email name="email" id="email"><br>
<input type="submit">
</form>
</body>
</html>



```







# 키보드 이벤트

```javascript


<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>javascript:event</title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function(event){
	$('textarea').keyup(function() {
		//keyup은이벤트 객체로 키보드의 키를 눌렀다 뗄때 발생
		var inputLength = $(this).val().length;
		//$(this) 는 $('textarea')를 의미한다. $('textarea')의 문자의 길이 length를 나타낸다.
		var remain = 150 - inputLength;
		//$(this) 는 $('textarea')를 의미한다.
		//150에 문자 길이를 빼준다.
		$('h1').html(remain);


		if(remain >= 0) {
			$('h1').css('color', 'Black');
		} else {
			$('h1').css('color', 'Red');
		}
	})
	 
});
 
</script>
</head>
<body>
<div>
        <p>지금 내 생각을</p>
        <h1>150</h1>
        <textarea cols="70" rows="5"></textarea>
    </div>
</body>
</html>



```



# jQuery 이벤트 사용해 간단하게 무한 스크롤 구현

```javascript


<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>javascript:event</title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
	$(document).ready(function() {
		for(var i = 0; i< 20 ; i++) {
			$('<h1>Infinity Scroll</h1>').appendTo('body');
		}


	$(window).scroll(function() {

		var scrollHeight = $(window).scrollTop() + $(window).height();

		var documentHeight = $(document).height();

		if(scrollHeight == documentHeight) {
			for(var i = 0; i < 10; i++) {

				$('<h1>Infinity Scroll</h1>').appendTo('body');
			}
		}
	});
	});

 
</script>
</head>
<body>

</body>
</html>



```



# 저수준의 시각적 효과

```javascript


<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>javascript:event</title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script> 
<script>
//테스트를 위해 내부에 공간을 채워둡니다.
$(document).ready(function () {
	$("#show").click(function() {$("img").show();});
	$("#hide").click(function() {$("img").hide();});
	$("#toggle").click(function() {$("img").toggle(3000, "linear", function() {
		alert("END!");
	});});

	$("#slideD").click(function() {$("img").slideDown();});
	$("#slideU").click(function() {$("img").slideUp();});
	$("#slideToggle").click(function() {$("img").slideToggle(3000, "swing", function() {
		alert("END!");
			});});
     //slideToggle : 	선택한 요소에 .slideUp() 메소드와 .slideDown() 메소드를 번갈아가며 적용한다.

});

</script>
</head>
<body>
<button id="show">show</button>
<button id="hide">hide</button>
<button id="toggle">toggle</button>
<button id="slideD">slideDown</button>
<button id="slideU">slideUp</button>
<button id="slideToggle">slideToggle</button>
<button id="fadein">fadeIn</button>
<button id="fadeout">fadeOut</button>
<button id="fadetoggle">fadeToggle</button>
<br>
<img src="cat.jpg" />
</body>
</html>
```







# innerFade 플러그인



# animate() 메서드

```javascript

<!DOCTYPE html>
<html>
<head>
<style>
div{ width:50px;
     height:50px;
     background:orange;
     position:relative;
     }
</style>
<meta charset="utf-8">
<title>Insert title here</title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function () {
	$("div").hover(function() {
		$("div").animate({left:500}, 'slow'); //요소1
}, function() {
	$(this).animate({left:0}, 'slow');
	//요소2
	//마우스 포인터가 요소들에 올라오거나 떠날때 실행되는 두개의 핸들러를 바인딩합니다.


});
});	

</script>
</head>
<body>
<div></div>
<div></div>
<div></div>
<div></div>
<div></div>
<div></div>
</body>
</html>
```





# 상대적 애니메이션

```javascript

<!DOCTYPE html>
<html>
<head>
<style>
div{ width:50px;
     height:50px;
     background:orange;
     position:relative;
     }
</style>
<meta charset="utf-8">
<title>Insert title here</title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function () {
	$('div').click(function() {
		var width = $(this).css('width');
		var height = $(this).css('height');


		$(this).animate({
			width: parseInt(width) + 50,
			height : parseInt(height) + 50
		}, 'slow');
	})


});	

</script>
</head>
<body>
<div></div>
<div></div>
<div></div>
<div></div>
<div></div>
<div></div>
</body>
</html>
```





# 애니메이션 큐

```javascript

<!DOCTYPE html>
<html>
<head>
<style>
div{ width:50px;
     height:50px;
     background:orange;
     position:relative;
     }
</style>
<meta charset="utf-8">
<title>Insert title here</title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function () {
	$('button').click(function () {
		var html = $(this).html();
		var html eval(evalText);

	})

	$('div').animate({
		left: '500'
	},5000).animate({

		left: '0'
	},5000);

});	

</script>
</head>
<body>
<button>stop()</button>
<button>stop(true)</button>
<button>stop(false, true)</button>
<button>stop(truem true)</button>
<div></div>



</body>
</html>
```





# 애니메이션 지연

```javascript

```





JQuery - 모든 브라우저에서 동작하는 (클라이언트 side에서 실행) 자바 스크립트

#html의 문서요소를 간결하게 처리할 수 있다.





load이벤트와 유사한 jquery의 이벤트는 ready 이벤트

$(document).ready(이벤트 핸들러 함수);

$("css select문법")



$("태그명")

$("#id값")

$("태그.class속성값")

$("부모태그 > 자식태그")

$("부모태그   자식태그")

$("태그 ,태그, 태그")

$("태그[속성명 = 속성명]")







가상샐랙터

#jquery는 메서드 체인형태로 사용합니다.

