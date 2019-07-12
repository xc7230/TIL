#Spring Framework 특성

경량 컨테이너 지원(제공)

Factory패턴이 적용된 IoC컨테이너는 DI(의존하는 객체를 직접 생성하지 않고,)

AOP(관점지향 프로그래밍) 지원 - 핵심 로직과 공통 로직을 분리해서 핵심 로직수행할때 공통 로직을 적용POJO로 Bean을 정의해서 사용 할 수 있도록 지원

영속성과 관련된 다양한 API(Hibernate, MyBatis, JDO, ....) 지원

트랜잭션 처리를 위한 일관된 방법으로 처리, 관리 지원

배치처리, 메시지 처리, ...다양한 API지원

Framework를 위한 Framework



#Spring Framework 모듈

Spring Core 모듈 - IoC 기능 지원 (Spring Container 클래스 : BeanFactory)

Spring Context 모듈 - Core에서 지원하는 기능외에 추가적인 기능들 지원(JNDI, EJB를 위한 Adapte)

(ApplicationContext-Spring Container 클래스 : BeanFactory)

Spring AOP 모듈 - 관점 지향 프로그래밍 지원

Spring DAO 모듈 - JDBC 보다 더 쉽고, 간결하게 개발 가능

Spring ORM 모듈 - Hibernate, MyBatis, JDO,...와의 결합, 통합을 지원

Spring Web 모듈 - MVC 패턴이 적용된 Web App 개발 지원, struts , Webwork와 같은 프레임워크와 통합

Spring Web MVC모듈 - 다양한 Web UI, 기술 등의 API 지원



#의존객체를 생성, 주입 방식

1. 생성자를 통해 주입
2. setxxxx메서드를 이용해서 주입





#Bean 설정 발식

1. xml 설정방식

   ```java
   <bean id=""
       	name=""
       		class="">
    <constructor-arg ref="빈이름" />
                   <property type = " " index = "" ref=" 빈이름 " />
   ```

   

2. 자바 클래스와 Anntation

   ```java
   @Configuration
   @빈을 리턴하는 메서드 선언부에 @Bean 선언, 빈의 이름은 메서드 이름
   소스코드에서 빈 요청 할 때 - 컨테이너객체.getBean("빈이름", 빈타입.class)
   String 컨테이너와 default 빈 Scope는 Singleton입니다.
   ```







------------------------------------------실습------------------------------------------------------



**메이븐 프로젝트 생성**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:p="http://www.springframework.org/schema/p"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<bean id = "firstMessage"
		class = "lab.spring.di.persist.SimpleMessage" />

<bean id = "hello"
		class="lab.spring.di.service.HelloServiceImpl"
		scope="prototype" >
		<constructor-arg ref="firstMessage" /> 
		
//bean선언		 
		
		<!--  <property name="message" ref="firstMessage" />  -->
	</bean>		
<bean id = "messageSource"
class="org.springframework.context.support.ResourceBundleMessageSource">
<property name="basenames">
<value>messages.notice</value>
</property>
</bean>




<!-- 

<bean id="service"
		class = "lab.spring.di.service.HelloServiceLifeCycle"
		p:name = "Spring5.0!!!"
		p:myMessage-ref="firstMessage"
		init-method="custom_init"
		destroy-method="custom_end"/>
		 -->
		
<bean id="oracleDBUtil"
		class="lab.spring.util.JdbcUtil"
		p:driver="oracle.jdbc.OracleDriver"
		p:url="jdbc:oracle:thin:@localhost:1521:orcl"
		p:user ="hr"
		p:pwd="oracle"/>
		
<bean id="userDao"
		class="lab.spring.di.persist.UserManageDAO"
		p:dbUtil-ref="oracleDBUtil" />

<bean id="loginService"
		class="lab.spring.di.service.UserServiceImpl"
		p:dao-ref="userDao" />



</beans>

```



**클래스 만들기**



```java
package lab.spring.di.persist;

import org.springframework.stereotype.Component;

@Component("simple")  // @Component : 일반적인 용도의 컴포넌트들을 표시하는 기본 스테레오 타입
public class SimpleMessage implements Message{
	public String getMessage() {
	//	return "Annotation 설정";
		return "Simple Message";

	}

}
```







```java
package lab.spring.di.service;

import javax.annotation.Resource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import lab.spring.di.persist.Message;


@Service("hello")  //서비스 레이어의 서비스 컴포넌트
public class HelloServiceImpl implements HelloService {
		@Autowired
		//@Qualifier("simple")
		@Resource(name="detail")
	private Message message;
		
		
		
		public HelloServiceImpl() {
			super();
		}
		
		
		public void setMessage(Message message) {
			this.message = message;
		}

//		public HelloServiceImpl(Message message) {
//			super();
//			this.message = message;
//			System.out.println("생성자를 이용해서 Bean 주입함");
//		}



		public void sayHello() {
			System.out.println(message.getMessage());
		}
		

		
	}



```







```java

```

