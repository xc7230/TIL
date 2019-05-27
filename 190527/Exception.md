# 예외처리



compile error - 문법적 문제, 언어 규칙에 맞지 않는 문제
runtime error - 실행시에 발생되는 오류 - 논리 오류, 로직 오류
자바의  runtime error - XXXError (프로그램적으로 수정할 수 없음, 무겁고, 치명적0
                        RuntimeException의 하위 Exception은 프로그램적으로 수정하면 정상적으로 프로그램 흐름을 유도 가능

자바의 Exception - checked exception - 실행 범위가 JRE를 벗어나는 경우의 코드에 대해서 컴파일시에 check를 해주므로(IOException, Socket..., SQLException..)
                   unchecked exception - 실행 범위가 JRE를 벗어나지 않고, 사용자 부주의 또는 논리 오류에 의해서 발생될 수 있는 Exception (NullPointerException, ArrayIndexOutOfBoundsException, NumberFormatException,..)

예외 처리 방식 - declare, handle

declare방식 -throws 예외클래스이름을  메서드 선언부에 선언합니다.
             예외처리 대신에 메서드를 호출한 곳으로 예외처리를 떠 넘깁니다.

handle - try~catch~finally

try{
    예외 발생될 가능성이 있는 문장;
    문장;
   }catch(예외클래스타입  객체) {
     예외 처리 문장;
   }catch(예외클래스타입 객체) {
     예외 처리 문장;
   }finally{
      예외 발생과 무관한 반드시 수행해야 할 코드 문장;
      ex)사용했었던 자원 정리   .close() => checed exception
      try~catch 사용 가능

   }


catch를 여러개 정의할 경우 하위 Exception클래스부터 ~ 상위 Exception클래스 순으로 정의합니다.

프로그램 구현시 의도적으로 예외를 발생시켜서 호출한쪽(caller)에게 메시지를 전달해서 
호출한쪽(caller)에서 흐름을 제어할 수 있도록 throw new 예외클래스(메시지) 처리합니다.



프로그램 구현시 의도적으로 예외를 발생시켜서 호출한쪽(caller)에게 메시지를 전달해서 
호출한쪽(caller)에서 흐름을 제어할 수 있도록 throw new 예외클래스(메시지) 처리합니다.

API에서 
java.lang.Throwable - java.lang.Error

                    - java.lang.Exception

사용자 정의 예외클래스
AccessModifier class XXXException extends 구체적 Exception(API) {
   //속성
   //생성자
   //기능
}



# java.lang 유용한 클래스

## 얕은 복사

객체에 저장된 값을 그대로 복제할 뿐, 객체가 참조하고 있는 객체까지 복제하지 않습니다. 원본을 변경하면  복사본도 영향을 받습니다.



## 깊은 복사

원본이 참조하고 있는 객체까지 복사합니다. 서로 다른 객체를 참조하기 때문에 원본이 변경 되어도 복사본에 영향을 끼치지 않습니다.



## 연습

clone()을 이용하여 얕은복사와 깊은복사의 차이를 알아봅니다.



```java
class Circle implements Cloneable {
	
	Point p;  //원점
	double r; //반지름

	
	Circle(Point p, double r) {
		
		this.p = p;
		this.r = r;	
	}
	public Circle shallowCopy() { //얕은 복사
		Object obj = null;
		
		try {
			obj = super.clone();
		} catch(CloneNotSupportedException e) {}
		return (Circle)obj;
	}
	
	public Circle deepCopy() { //깊은 복사
		Object obj = null;
		try {
			obj = super.clone();
		} catch (CloneNotSupportedException e) {}
		
		Circle c = (Circle)obj;
		c.p = new Point(this.p.x, this.p.y);
		return c;
	}
	
	public String toString() {
		return "[p=" + p + ", r="+ r + "]";
	}	
}

class Point {
	int x, y;
	Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public String toString() {
		return "("+ x + ", "+ y+")";
	}
}
public class ShallowDeCircle {
	

	public static void main(String[] args) {
		
		Circle c1 = new Circle(new Point(1,1), 2.0);
		Circle c2 = c1.shallowCopy();
		Circle c3 = c1.deepCopy();
		
		System.out.println("c1 = c1");
		System.out.println("c2 = c2");
		System.out.println("c3 = c3");
		
		c1.p.x = 9;
		c1.p.y = 9;
		System.out.println("= c1의 변경 후 = ");
		System.out.println("c1="+ c1);
		System.out.println("c2="+ c2);
		System.out.println("c3="+ c3);
	}

}
```



### 결과



```java
c1 = c1 //기본값p= (1,1), r= 2.0
c2 = c2
c3 = c3
= c1의 변경 후 = 
c1=[p=(9, 9), r=2.0] //기본값 
c2=[p=(9, 9), r=2.0] //얕은 복사
c3=[p=(1, 1), r=2.0] //깊은 복사

```

