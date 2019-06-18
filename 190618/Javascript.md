# Javascript

## 특징

프로토타입 기반이다

객체를 생성한 후에도 메서드를 추가가능

동적타입언어

실행되기전에 변수타입 결정

함수를 객체취급

클로저

클로저를 이용해서 변수를 은닉 영속성 보장





## 기술적 요소

ECMAScript로 규정되어있다.

웹브라우저의 API로 구성되어있다

Window인터페이스 : 자바스크립트로 브라우저 또는 창을 조작하는기능

2010년도 서버사이드에서도 자바스크립트 가능

클라이언트 자바스크립트

서버사이드 자바스크립트





## HTML문서에 자바스크립트 포함 위치

```html
<head>
    <script>
    //자바스크리트 코드 - 전역변수선언, 함수 선언
    //body의 요소를 참조하거나, 사용하는 자바스크립트 실행문장은 오류발생
    </script>
</head>
<body>
    <script>
    //자바스크립트 코드 - 즉시 실행 문장 코드
    </script>
    
</body>

//HTML 문서와 자바스크립트를 분리하는 것을 권장합니다.
<head>
    <script type="text/javascript" src = "경로/파일.js">
    </script>
</head>
<body>
    
</body>

```





## Javascript 불러오기

```html
<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8">
 <script src="./first.js">
 
 </script>

</head>
<body>
	외부 javascript파일 로딩시 실행합니다.

 
</body>
</html>

```



```javascript
window.alert("first.js파일에 저장된 javascript코드 실행");
```



# 변수

## 타입선언 없이

```javascript
var sum;
var sum, a;

```

## 데이터 타입

```javascript
<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8">
 

</head>
<body>
#자바스크립트의 데이터 유형<br>
primitive type - string, number, boolean <br>
객체(reference type) - function, object <br>
<script>
	var a = 1; //정수와 실수 구분
	document.write("a변수의 타입 :" +typeof(a) + "<br>");
	var b = 0.5;
	document.write("b변수의 타입 :" +typeof(b) + "<br>");
	a = "javascript";
	document.write("a변수의 타입 :" +typeof(a) + "<br>");
	b = "ECMAScript";
	document.write("b변수의 타입 :" +typeof(b) + "<br>");

	a=function(){};
		document.write("a변수의 타입 :" +typeof(a) + "<br>");
	b = new Object(); //생성자 호출
		document.write("b변수의 타입 :" +typeof(b) + "<br>");
	a = true;
	document.write("a변수의 타입 :" +typeof(a) + "<br>");

	a={}; //JSON객체
		document.write("a변수의 타입 :" +typeof(a) + "<br>");

	b=[]; //자바스크립트에서는 배열은 객체로 취급
		document.write("b변수의 타입 :" +typeof(b) + "<br>");




</script>


</body>
</html>

```



## 숫자

```javascript
<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8">
 

</head>
<body>
#자바스크립트의 데이터 유형<br>
primitive type - string, number, boolean <br>
객체(reference type) - function, object <br>
<script>


	a=0x2a; //JSON객체
		document.write("a변수의 10진수값 :" +a + "<br>");

	b=0o73; //자바스크립트에서는 배열은 객체로 취급
		document.write("b변수의 10진수값 :" +b + "<br>");

	a=0b101
		document.write("a변수의 10진수값 :" +a + "<br>");
	a=1.161425E-11;
		document.write("a변수의 10진수값 :" +a + "<br>");


</script>


</body>
</html>

```







# 연산자

자바스크립트는  결과갚이 소수점이면 자동으로 부동소수점으로 계산

1+null은 null을 자동으로 0으로 취급 결과는 1이된다.

1+undefined는  undefined을 nan값으로 바꾼다 결과는 nan







### 주사위 랜덤

```javascript
<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8">
 <title>자바스크립트 연산자</title>

</head>
<body>
<h1>자바스크립트 연산자</h1>

<script>
var num =  Math.round(Math.random()*5)+1;
document.write("주사위 숫자: "+num);



</script>

</body>
</html>

```







### 자바스크립트 연산자 예제

```javascript
<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8">
 <title>자바스크립트 연산자</title>

</head>
<body>
<h1>자바스크립트 연산자</h1>

<script>
var num =  Math.round(Math.random()*5)+1;
document.write("주사위 숫자: "+num+"<br>");
//() - JSON 객체는 Object 내장객체를 상속받습니다.

document.write("1 + () :"+ (1 + {}) +"<br>"); 
document.write("true + (new Date())" + (true + (new Date())) +"<br>");
var msgObj = new String("Everything is practice");
document.write("msgObj.length : " + msgObj.length + "<br>");
document.write("msgObj.charAt(3) : " + msgObj.charAt(3) + "<br>");
document.write("msgObj.substring(7, 10) : " + msgObj.substring(7, 10) + "<br>");
document.write("msgObj.slice(7, 10) : " + msgObj.slice(7, 10) + "<br>");
document.write("msgObj.slice(-3) : " + msgObj.slice(-3) + "<br>");
document.write("msgObj.slice(-9, -6) : " + msgObj.slice(-9, -6) + "<br>");
document.write("msgObj.indexOf('t')) : " + msgObj.indexOf("t") + "<br>");
document.write("msgObj.indexOf('i', 10) : " + msgObj.indexOf("i", 10) + "<br>");
document.write("msgObj.split( )  : " + msgObj.split(" ") + "<br>");
document.write("msgObj.replace('p', 'P') : " + msgObj.replace("p", "P") + "<br>");
document.write("msgObj.includes('thing') : " + msgObj.includes("thing") + "<br>");
document.write("msgObj.charCodeAt(0) : " + msgObj.charCodeAt(0) + "<br>");
document.write("mmsgObj.codePoint(0) : " + msgObj.codePointAt(0) + "<br>");
document.write("null == undefined : " + (null == undefined) + "<br>");
document.write("1 == '1' : " + (1 == "1") + "<br>");
document.write("255 == '0xff' : " + (255 == 0xff) + "<br>");
document.write("true == 1 : " + (true == 1) + "<br>");
document.write("true == '1' : " + (true == '1') + "<br>");
document.write("new String('a') == a' : " + (new String('a')=='a') + "<br>");
document.write("new Number(2) == 2' : " + (new Number(2)==2) + "<br>");
//==은 값만 비교



document.write("null === undefined : " + (null === undefined) + "<br>");
document.write("1 === '1' : " + (1 === "1") + "<br>");
document.write("255 === '0xff' : " + (255 === 0xff) + "<br>");
document.write("true === 1 : " + (true === 1) + "<br>");
document.write("true === '1' : " + (true === '1') + "<br>");
document.write("new String('a') === a' : " + (new String('a')==='a') + "<br>");
document.write("new Number(2) === 2' : " + (new Number(2)===2) + "<br>");
//===값과 타입을 비교합니다.

document.write("10<20<30 : " + (10<20<30)+"<br>")
document.write("10>20>30 : " + (10>20>30)+"<br>")
document.write("10>20>30 : " + (10>20>0)+"<br>")

var a = "window.alter('eval은 문자열 자바스크립트 코드로 실행합니다 ')";
//eval(a);

var student = { "name":"Kim", "ko":85, "en": 90, "math":80};

document.write("typeof(student) : " + typeof(student) +"<br>");
document.write("student instanceof Object : " + (student instanceof Object) +"<br>");

document.write("ko in student : " + ('ko' in student) +"<br>");






</script>

</body>
</html>

```





## 형변환

```javascript
<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8">
 <title>자바스크립트 형변환</title>

</head>
<body>
<h1>자바스크립트 형변환</h1>

<script>

var n = 26;
n.toString();
document.write("n.toString() :"+n.toString()+"<br>");
document.write("n.toString(2) :"+n.toString(2)+"<br>");
document.write("n.toString(16) :"+n.toString(16)+"<br>");
document.write("(26).toString(16) :"+(26).toString(16)+"<br>");

var x = 1234.567;
document.write ("x.toString()");
document.write("x.toString() :"+x.toString()+"<br>");
document.write("x.toString(16) :"+x.toString(16)+"<br>");
document.write("x.toFixed(0) :"+x.toFixed(0)+"<br>");
document.write("x.toFixed(2) :"+x.toFixed(2)+"<br>");
document.write("x.toFixed(4) :"+x.toFixed(4)+"<br>");
document.write("x.toExponential(3) :"+x.toExponential(3)+"<br>");
document.write("x.toPrecision(3) :"+x.toPrecision(3)+"<br>");
document.write("x.toPrecision(6) :"+x.toPrecision(6)+"<br><br>");

document.write("String"+"<br>");
document.write("String(26) :"+String(26)+"<br>");
document.write("String(1234.567) :"+String(1234.567)+"<br>");
document.write("String(0x1a) :"+String(0x1a)+"<br>");

document.write("String('ABC') :"+String("ABC")+"<br>");
document.write("String(true) :"+String(true)+"<br>");
document.write("String(false) :"+String(false)+"<br>");
document.write("String(NaN) :"+String(NaN)+"<br>");
document.write("String(null) :"+String(null)+"<br>");
document.write("String(undefined) :"+String(undefined)+"<br>");
document.write("String({x:1,y:2}) :"+String({x:1,y:2})+"<br>");
document.write("String([1,2,3]) :"+String([1,2,3])+"<br><br>");
//String 함수에는 모든 데이터 타입을 문자열 타입으로 바꾸는 기능이 있다.


document.write("parseInt"+"<br>");
document.write("parseInt('3.14') :"+parseInt("3.14")+"<br>");
document.write("parseFloat('3.14') :"+parseFloat("3.14")+"<br>");
document.write("parseInt('3.14 meters') :"+parseInt("3.14 meters")+"<br>");
document.write("arseFloat('3.14 meters') :"+parseFloat("3.14 meters")+"<br>");
document.write("parseInt('0xFF') :"+parseInt("0xFF")+"<br>");
document.write("parseInt('0.5') :"+parseInt("0.5")+"<br>");
document.write("parseInt('.5') :"+parseInt(".5")+"<br>");
document.write("parseInt('abc') :"+parseInt("abc")+"<br>");
document.write("parseFloat('\100') :"+parseFloat("\100")+"<br>");


document.write("parseInt('101',2) :"+parseInt("101",2)+"<br>");
document.write("parseInt('ff',16) :"+parseInt("ff",16)+"<br><br>");
//perseInt 함수는 문자열을 정수로바꿔준다.
//perseFloat 함수는 문자열을 부동소수점으로 바꿔준다.
//두 함수는 첫번째 문자를 숫자로 바꾼값을 반환하고, 이 후 등장하는 문자열은 무시한다.
//첫번째 문자를 해석못하면 NaN을 반환한다.




document.write("Number"+"<br>");
document.write("Number(123) :"+Number(123)+"<br>");
document.write("Number(true) :"+Number(true)+"<br>");
document.write("Number(false) :"+Number(false)+"<br>");
document.write("Number(NaN) :"+Number(NaN)+"<br>");
document.write("Number(undefined) :"+Number(undefined)+"<br>");
document.write("Number(null) :"+Number(null) +"<br>");
document.write("Number({x:1, y:2}) :"+Number({x:1, y:2})+"<br>");
document.write("Number([1, 2, 3]) :"+Number([1, 2, 3])+"<br>");

//Number함수에는 모든 데이터 타입을 숫자 타입으로 변경한다.

</script>

</body>
</html>

```





## 제어문

#### 연습문제

```javascript
<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8">
 <title>자바스크립트 제어문</title>

</head>
<body>
<h1>자바스크립트 제어문</h1>
문1> if문을 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀 수 인지 맞추기
문2> 삼항연상자를 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀 수 인지 맞추기
문3> 논리연산자를 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀 수 인지 맞추기
문4> switch문을 사용하여 사용자로부터 입력받은 점수에 대한 학점 출력<br><br><br>

<script>
var input1 = window.prompt("점수를 입력하세요", 0);
document.write(input1 +"<br>")
if(parseInt(input1)%2 == 0) {
document.write("짝수" +"<br>")
}
else {
	document.write("홀수" +"<br>"+"<br>")
}
//문1> if문을 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀 수 인지 맞추기

parseInt(input1) % 2 == 0 ? document.write("짝수"+"<br>") : document.write("홀수"+"<br>");

//문2> 삼항연상자를 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀 수 인지 맞추기

parseInt(input1) % 2 == 0&&document.write("짝수"+"<br>");
parseInt(input1) % 2 == 0||document.write("홀수"+"<br>");



//문3> 논리연산자를 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀 수 인지 맞추기

switch( parseInt(parseInt(input1)/10)) {
	case 10:
	case 9 : document.write("A" + "<br>");
	break;
	case 8 : document.write("B" + "<br>");
	break;
	case 7 : document.write("C" + "<br>");
	break;
	case 6 : document.write("D" + "<br>");
	break;	
	default:  document.write("F" + "<br>")
}


switch(true) {
	
	case input1>89 : document.write("A" + "<br>");
	break;
	case input1>79 : document.write("B" + "<br>");
	break;
	case input1>69 : document.write("C" + "<br>");
	break;
	case input1>59 : document.write("D" + "<br>");
	break;	
	default:  document.write("F" + "<br>");
}

//문4> switch문을 사용하여 사용자로부터 입력받은 점수에 대한 학점 출력







</script>

</body>
</html>

```





```javascript
<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8">
 <title>자바스크립트 형변환</title>

</head>
<body>
<h1>자바스크립트 형변환</h1>
#문자열로 형변환 : 값+"" 또는 String(값)<br>
#숫자열로 형변환 : window.parseInt("123a")또는 window.parseFloat("0.123b") 또는 Number("123a")<br>

<script>
for(var i = 0; i<10; i++) {
	if(i%2==1) {
		document.write(i+"홀수"+"<br>")
	} else{document.write(i+"짝수"+"<br>")}



}

document.write("<hr>");

var i=0;
while(i <10) { 
	++i
	if(i%2==1) {
		document.write(i+"홀수"+"<br>");
	}



}

 do { 
 	if(i%2==1) 
		document.write(i+"홀수"+"<br>");

 } while(++i<10);
 document.write("<hr>");
var nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for (var n in nums) { 
	if(n%2==1) 
		document.write(n+"홀수"+"<br>");
	
 }
document.write("<hr>");

for(var su = 1; su<10; su++) {
	for(var dan = 2;dan<10; dan++) {
		document.write(`${dan}X${su} = ${dan*su}\t`);
	}
document.write("<br>");

}



 

 </script>

 </body>
 </html>

```

