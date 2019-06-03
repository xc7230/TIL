

# Calendar

날짜 데이터처리하면 날짜 데이터 표현



현재월

```java
Calendar cal = Calendar.getInstance();
cal.get(Calendar.MONTH);
```



5월 31일 설정

```java
cal.set(2019, 4, 31);
```



날짜 데이터를 특정 형식으로 문자열화하려면 : yyyy-MM-dd hh:nn:ss

```java
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
Date d = new Date();
sdf.format(d);
```



숫자 데이터를 특정 형식으로 문자열화하려면

```java
double won = 12345.678
DecimalFormat df = new DecimalFormat("\u00A4##,###.");
String s = df.format(won);
```



특정 형식으로 문자화된 데이터 숫자로 변환하려면



```java
df.parse
```



jdk 8 java.time 패키지가 추가

```java
LocalDate today = LocalDate.now();
get()으로 Month값 변환받때 1~12값 반환
LocalTime = LocalTime.now();
```







# Collection

데이터 집합 , 자료구조

# Framework

표준화된 설계

배열 - 생성시에 배열의 크기를 반드시 설정해야하고, 저장된 요소의 크기가

collection - 생성시에 저장될 요소의 크기를 설정하지 않아도 되고, 동적으로



## Collection - List, Set

**List** <Book>  - 저장한 순서 보장, 중복된 객체 저장,인덱스(offset)으로 저장된요소

​		ArrayList(단일스레드환경), Vector(멀티스레드), LinkedList, Stack

​		add(), add(index, 객체)

​		clear(), removeAll()

​		remove(객체), remove(index)

​		size()

​		contains()

​		get(index)

**Iterator**<book> - iterator()

​			while(iterator.hashNext()) {

​				Book b = iterator.next();	

​				}

**Enumeration** - hasMoreElement(), nextElement()

**Stack** - LIF0구조, push(객체),pop(),peak()

**Queue** - 인터페이스(1.5) - FIF0

**Set** - 중복 객체 저장 불가, 순서 보장 안됨



**Hachset**

**Treeset**

add()

remove(), removeAll(), clear()

constains()

toArray()

size()

Iterator로 요소 접근 - iterator()

​		While(iterator.hasNext()) {

​			Book b = iterator.next();

}



**Map** - key객체와 value객체를 매핑해서 저장

**put**(key객체, value객체)

**keySet()** - Set타임

**entrySet** - Map에 저장된 Key-Value 쌍으로 Map.Entry타입 리턴



Map의 요소를 꺼내서 처리하면

1.키집합을 리턴받고 -keySet()

2.키집합에 대한 Iterator 생성

3.Iterator로 키를 꺼내서 map에 저장된 Value객체를 꺼냅니다. get(Key)

