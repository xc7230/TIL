# 예외처리







### 예외처리 

declare, handle

### 예외발생 

 throw new 발생시킬예외클래스생성자()

### 사용자정의 Exception 정의, 생성, 사용



## 1. 예외처리(declare) - throws

## 2. 예외처리(handle) - try~catch~finally

try~catch~finally
try~finally
try~catch(0 or M)

catch가 여러번 선언될 경우, 예외클래스의 상속 계층구조의 역순으로 구체적인 예외클래스타입부터 선언해줍니다.

try{
    예외 발생 가능성 문장;
    문장;
   }catch(예외클래스타입 객체){
       예외 처리 문장;
   }catch(예외클래스타입 객체){
       예외 처리 문장;
   }finally{
     예외 발생과 무관한 반드시 수행해야 할 문장;
     ex) 사용했었던 resource들의 정리(close()) 코드문장
  }



사용자 정의 예외 클래스를 정의할때는 구체적인 예외 처리 관련 API의 Exception을 상속받아서
속성과 메서드를 추가해서 만듭니다.

사용자 정의 예외 클래스를 정의할때 Exception을 상속을 받아서 예외처리에 필요한 
속성과 메서드를 추가해서 만듭니다.

public class XXXException extends Exception {
   //속성
   //생성자
   //멤버 메서드
}



## 연습문제



### 옜날 남자들의 평균키



```java
public class AbonormalValueException extends Exception {
	private double oldTall = 163.2;
	
	public AbonormalValueException(String message) {
		super(message);
	}
	
	public double getOldTall() {
		return oldTall;
	}

}
```



## 현재 남자들의 키

극한값으로 가는 키들은 옜날 평균키로 바꾼다.

``` java
public class ExceptionHandleTest {
    
	public void manTall(double tall) throws AbnormalValueException {
		//키 범위가 140이상 180이하 여부를 체크해서
		//범위가 아니면예외를 던집니다
		if(tall<140) throw new AbnormalValueException("140보다 작습니다");
		if(tall>180) throw new AbnormalValueException("180보다 큽니다");
	}
	
	public static void main(String[] args) {
		double[] talls = new double[] { 150.5,162.2,173.4,148.9,
				125,164,188.5,166,162,169,158,173};
		ExceptionHandleTest  test = new ExceptionHandleTest();
        //키값의 범위를 체크해서
		//예외 발생하면 예외처리합니다. => 작년도 키 평균값으로 보정합니다.
		//올해의 중학생 평균 키값을 출력합니다.
		for(int i=0;i<talls.length;i++) {
			try {
			     test.manTall(talls[i]);
			}catch(AbnormalValueException e) {
				System.out.println(e.getMessage()+", 작년도 키값으로 보정합니다.");
				talls[i] = e.getOldTall();				
			}
		}
		double hap = 0.0;
		for(double tall : talls)
			hap += tall;
		System.out.println("올해 남자 평균 키는 "+(hap/talls.length)+"cm입니다.");
		
		}//main end

}//class 

```



## 결과



```java
140보다 작습니다, 작년도 키값으로 보정합니다. 
180보다 큽니다, 작년도 키값으로 보정합니다. 
올해 남자 평균키는162.78333333333333cm입니다.
```



