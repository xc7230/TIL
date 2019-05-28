# String

문자열 표현, 불변객체



```java
String s2 = "java";
byte[] bytes = s2.getByte();
s2.charAt(0)
s2.substring(1,3);
String newStr =	s.concat(s2); //s객체 출력하면 "abc"
contains()
//문자열객체.equals(비교할 문자열객체) - 문자열의 내용을 비교
//equalslngoreCase()

```





**contains** 특성의 순서를 검색합니다.





**split**(구분자 또는 정규 표현식)  - 문자열을 구분자로 쪼개어 문자열 배열로 리턴

**join**(결합문자,문자열배열) - 문자열 배열의 요소를 하나씩 결합문자를 사용



가변문자열 **StringBuffer: **문자열을 추가하거나 변경 할 때 주로 사용하는 자료형입니다.

**equals(): ** 객체끼리 내용을 비교할 수 있도록 합니다.

StringBuffer

```java
public static void main(String[] args) {
	StringBuffer sb1 = new StringBuffer("java");
	StringBuffer sb2 = new StringBuffer("java");
	System.out.println(sb1.equals(sb2));
	}
	sb1.append("& sql"); // sb1의 출력내용은 "java& sql"
	sb1.insert(4, "web");	
```

```java
//출력내용
false

```



**remove(): ** 특정 인덱스에 위치한 엘리먼트를 삭제할 때
**length(): ** 문자의 길이
**substring():** 문자열 자르기



수학계산에 유용한 메서드를 가지고 있는 클래스 java.lang.Math

생성자

모든 속성과 메서드는 static



모두 객체로 구현해야 할경우,primitive data type을 객체로 wrapping

boolean -> Boolean -> booleanValue()  문자열 "true" -> Boolean.parseBoolean()
byte -> Byte          byteValue()     문자열 "100" -> Byte.parseByte()
short -> Short        shortValue()
char -> Character     charValue()
int -> Integer        intValue()
long -> Long          longValue()
float -> Float        floatValue()
double -> Double      doubleValue()

객체가 null 또는 null이 아닌지 체크하거나 반드시 null이 아니어야 함을 메서드로 제공해주는 클래스 : java.util.Objects

String s = null;
s==null?
s!=null?

시스템의 현재시간을 utc기준 milli second로 리턴하는 메서드 : System.currentTimeMillis()

난수 생성 : Math.random()
            Random r = new Random()
ex) (int)(Math.random()*100 +1)
     Random r = new Random()
     r.nextInt(100)+1
     Random r = new Random(seed값)


정규표현식을 이용해서 데이터 처리해야 할 경우, 특정 패턴을 객체로 생성
1. java.util.regex.Pattern.compile("패턴") => Pattern 인스턴스 생성
2. Matcher m =  Pattern 인스턴스.matcher(처리할 대상 데이터) => Matcher 인스턴스 생성
3. m.matches() => true or false로 리턴



하나의 모든 문자

[a-zA-Z0-9] 범위

en$

^ab

[^0-9]

[0-9]? zero or one

[0-9]+ one or more

[0-9]* zero or more

{2, 5 }최소횟수, 최대횟수

{3}





표준출력

1.5버전 이전에 한글을 포함한 키보드 입력을 받으려면

java.io.InputStream 바이트 최상위 스트림은 추상클래스

System.in 운영체제에 맞게 InputStream 구현 객체

문자 스트림은 XXXXReader, XXXWriter



```java
try {
    BufferedReader br = new Buffered(new InputStreamReader(System.in))
    String s = br.readLine();
    //Integer.parseInt(s)
} catch(IOException e) {
    
}finally{
    
    try{
        
    
    br.close(IOException e);
	}
}    

Scanner scan = new Scanner(System.in)
scan.next()
scan.next
```

