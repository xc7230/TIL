# 인터페이스

```
용도 - 사용자(User)와 제공자(Provider)사이에서 매개체(연결) 역할
구성요소 - public static final 상수속성, abstract 메서드(구현 body없음),  static메서드, default 메서드
설계시, 서로 다른 시스템을 통합할때 표준화를 위해서 활용
클래스는 일원화된 구조(선언+구현)라고 볼 수 있습니다.
인터페이스는 이원화된 구조 - 인터페이스(선언)는 반드시 인터페이스 구현 클래스가 있어야만 인터페이스에서 선언한 서비스  제공이 가능합니다.

public interface 이름 [extends 인터페이스, 인터페이스,..] {...}

public class 이름 implements 인터페이스, 인터페이스,.. {...}

인터페이스는 reference 변수(객체명) 타입으로 선언 가능합니다.

인터페이스는 new를 사용해서 객체 생성 가능하려면 구현한 클래스로 객체 생성 가능 => 다형성 객체
```



## 연습문제

###  인터페이스를 먼저 만든다.



~~~java
public interface Instrument {
	public abstract void Start();
	public abstract void Stop();

}

~~~

시작과 끝 메소드를 선언해줍니다.



### 동물 분류 클래스 만들기1(Dog)

1.Instrument 인터페이스를 implements 한다.

```java
public class Dog implements Instrument {

}
```







2.start(),stop() 메소드를 오버라이딩 합니다.

```java
	@Override
	public void Start() {
		System.out.println(this.toString()+"출발");

	}

	@Override
	public void Stop() {
		System.out.println(this.toString()+"종료");
	}

```





3.toString()메소드를 오버라이딩 합니다.

Dog 클래스에 "개" 리턴, 

```java
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "개";
	}
```

###  동물 분류 클래스 만들기2(Bird)





1.Instrument 인터페이스를 implements 한다.

```java
public class Bird implements Instrument {

}
```







2.start(),stop() 메소드를 오버라이딩 합니다.

```java
	@Override
	public void Start() {
		System.out.println(this.toString()+"출발");

	}

	@Override
	public void Stop() {
		System.out.println(this.toString()+"종료");
	}

```





3.toString()메소드를 오버라이딩 합니다.

Bird 클래스에 "새" 리턴, 

```java
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "새";
	}
```

### 

### 동물 분류 클래스 만들기3(Cat)





1.Instrument 인터페이스를 implements 한다.

```java
public class Cat implements Instrument {

}
```







2.start(),stop() 메소드를 오버라이딩 합니다.

```java
	@Override
	public void Start() {
		System.out.println(this.toString()+"출발");

	}

	@Override
	public void Stop() {
		System.out.println(this.toString()+"종료");
	}

```





3.toString()메소드를 오버라이딩 합니다.

Cat 클래스에 "고양이" 리턴, 

```java
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "고양이";
	}
```

### 동물 클래스 만들기

상위클래스를 상속받고(class  Poodle )

toString() 메소드를 오버라이딩 한다.



class Dog  <-상위클래스

class  Poodle 

```java

public class Poodle extends Dog {

	@Override
	public String toString() {
		return super.toString()+" : 푸들";
	}

	
}

```

class Bird  <-상위클래스

class  Duck, Swan 

```java


public class Duck extends Bird {

	@Override
	public String toString() {
		return super.toString()+" : 오리";
	}

	
}
public class Swan  extends Bird {

	@Override
	public String toString() {
		return super.toString()+" : 백조";
	}

	
}

```

class Cat  <-상위클래스

class  Persian, Munchkin

```java


public class Persian extends Cat {

	@Override
	public String toString() {
		return super.toString()+" : 페르시안";
	}

	
}
public class Munchkin  extends Cat {

	@Override
	public String toString() {
		return super.toString()+" : 먼치킨";
	}

	
}

```





### 동물Test

main() :  Instrument 배열을 생성한 후 playAll() , summary() 메소드를 호출합니다.



```java

public class AnimalTest {

	public static void main(String[] args) {

		Instrument[] e =new Instrument[] {
				new Poodle(),
				new Duck(),
				new Swan(),
				new Persian(),
				new Munchkin()
				
		};
		
		playAll(e);
		summary(e);
	}
	
```



playAll() : Instrument 배열 건수 만큼 for loop을 반복해서 Start(),Stop() 메소드를 호출합니다.

```java
private static void playAll(Instrument[] e) {
		System.out.println("=========== 시작 ============");
		for(Instrument instrument : e) {
			instrument .playStart();
		}
		System.out.println();
		System.out.println("=========== 종료 ============");
		for(Instrument instrument : e) {
			instrument .playStop();
		}
		System.out.println();
	}
	
```



summary() : Instrument 배열 건수 만큼 for loop을 반복해서 각 동물유형별 개수를 카운터하고 출력합니

```java
private static void summary(Instrument[] e) {
		int Dog = 0, Bird = 0, Cat = 0;
		for(Instrument instrument : e) {
			System.out.println(instrument);
			if(instrument instanceof Dog) {
				Dog +=1;
			}else if(instrument instanceof Bird) {
				Bird += 1;
			}else if(instrument instanceof Cat) {
				Cat +=1;
				
			}
		}


		System.out.println();
		System.out.println("===========동물 ===========");
		System.out.println("##개 :"+Dog);
		System.out.println("##새 :"+ Bird);
		System.out.println("##고양이 :"+Cat);
		
		System.out.println("=============================");

	}

}
```

### 결과



```java
===========출발============
개 : 푸들출발
새 : 오리출발
새 : 백조출발
고양이 : 페르시안출발
고양이 : 먼치킨출발

===========종료============
개 : 푸들종료
새 : 오리종료
새 : 백조종료
고양이 : 페르시안종료
고양이 : 먼치킨종료

개 : 푸들
새 : 오리
새 : 백조
고양이 : 페르시안
고양이 : 먼치킨

===========동물 ===========
##개 :1
##새 :2
##고양이 :2
=============================

```

