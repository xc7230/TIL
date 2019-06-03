## Equals

두 객체가 같은 객체인지 확인하는 Method입니다.



```java
package lab.java.core;

public class EqualsTest {

	public static void main(String[] args) {

		
		Object obj1 = new Object();
		Object obj2 = new Object();
				
		boolean result1 = obj1.equals(obj2);
				
		boolean result2 = (obj1 == obj2);
				
		System.out.println("equals결과 :"+result1); // 결과 false
		System.out.println("==연산결과 :"+result2); // 결과 false
	}

}


//false로 나옴
```



### HashCode

두 객체가 같은 객체인지 확인하는 Method입니다.



```java

```

