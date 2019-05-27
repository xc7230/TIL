```
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

API에서 
java.lang.Throwable - java.lang.Error
                    - java.lang.Exception

사용자 정의 예외클래스
AccessModifier class XXXException extends 구체적 Exception(API) {
   //속성
   //생성자
   //기능
}



package com.workshop5.biz;

import java.util.ArrayList;

import com.workshop5.entity.Customer;
import com.workshop5.util.CustomerUtil;

public class CustomerBiz implements ICustomerBiz{
    private ArrayList<Customer> customers;
	@Override
	public void initializeCustomer() {
		customers = new ArrayList();		 
		insertCustomer();		 
	}

	@Override
	public void printAllCustomer() {
		System.out.println("-----------------고객 정보------------------------");
		for(int i=0;i<customers.size();i++) {
			System.out.print(i+1+".[이름]"+customers.get(i).getName()+"\t");
			System.out.print("[나이]"+customers.get(i).getAge()+"\t  ");
			System.out.print("[전화번호]"+customers.get(i).getPhone()+"\n");			
		}		
		System.out.println("--------------------------------------------------");
	}

	@Override
	public void insertCustomer() {
		customers.add( new Customer("Lee", 28, "010-5678-1234"));
		customers.add( new Customer("Park", 31, "010-4567-9876"));
		customers.add( new Customer("Choi", 25, "010-1111-2222"));
	}

	@Override
	public void insertCustomer(Customer customer) {
		customers.add(customer);		
	}

	@Override
	public void deleteCustomer() {
		System.out.println("-------------------------------");
		System.out.println("고객 정보를 삭제합니다.");
		System.out.println("삭제할 고객의 번호를 입력하세요");
		System.out.println("-------------------------------");
		System.out.print(">번호:");
		int num = Integer.parseInt(CustomerUtil.getUserInput());
		customers.remove(num-1);
		System.out.println("@"+num+"번 고객 정보를 삭제하였습니다.");
	}

}







package com.workshop5.test;

import com.workshop5.biz.CustomerBiz;
import com.workshop5.biz.ICustomerBiz;
import com.workshop5.entity.Customer;
import com.workshop5.util.CustomerUtil;
 

public class CustomerTest {
	public static void main(String[] args) {
		ICustomerBiz  biz = new CustomerBiz();
		biz.initializeCustomer();
		int menu = 0;
		while(true) {
			printMenu();
			System.out.print("## 메뉴 입력:");
			try {
			     menu = Integer.parseInt(CustomerUtil.getUserInput());
			}catch(NumberFormatException e) {
				System.out.println("[에러] 메뉴는 숫자만 입력해야 합니다.");
				continue;
			}
			if (menu==9) {
				System.out.println("-------------------------------");
				System.out.println("프로그램을 종료합니다. Bye~ ");
				System.out.println("-------------------------------");
				break;
			}
			switch(menu) {
			case 1 : biz.printAllCustomer(); ; break;
			case 2:
				System.out.println("-------------------------------");
				System.out.println("새로운 고객 정보를 추가합니다.");
				System.out.println("새로운 고객의 정보를 입력하세요");
				System.out.println("-------------------------------");
				System.out.print(">이름:");
				String name= CustomerUtil.getUserInput();
				System.out.print("나이:");
				int age = Integer.parseInt(CustomerUtil.getUserInput());
				System.out.print(">전화번호:");
				String phone= CustomerUtil.getUserInput();
				Customer cust = new Customer(name, age, phone);
				biz.insertCustomer(cust);
				System.out.println("@ 고객 정보를 추가하였습니다");
                break;
			case 3 : biz.deleteCustomer(); break;
			default: System.out.println("[에러]메뉴를 잘못 입력하였습니다.");
			}
			 
		}
	}
	
	public static void printMenu() {
		System.out.println("===== <<고객 관리 프로그램>> ======");
    	System.out.println("1. 전체 고객 정보 조회");
    	System.out.println("2. 고객 정보 추가");
    	System.out.println("3. 고객 정보 삭제");
    	System.out.println("9. 시스템 종료");
    	System.out.println("=======================");
	}
}
```