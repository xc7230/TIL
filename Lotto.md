# 로또 번호 자동생성(연습문제)

랜덤으로 6개의 숫자를 ***중복없이***  배열하고 숫자 오름차순으로 정렬 했습니다.



## 로또 클래스 만들기

### 상수선언

```java
	public final static int LOTTO_NUM = 6;//final값 초기화

```



로또는 항상 6개의 번호를 뽑기때문에 배열은 6개가 돼야하고, 변경되면 안됩니다.

상수를 선언을 해서 변동되지 않게 합니다.



### 난수생성

로또는 총 45개의 번호로 되어있습니다. 1-45범위내에 난수를 생성해줍니다.

```java
private int getRandNumber() {
		Random rand = new Random();
		int randNumber = rand.nextInt(45)+1;
		return randNumber;
	}
```

접근지정자로 private를한 이유는 다른 클래스에서 변경하지 못하게 하기 위해서입니다.

(45)+1을한 이유는 난수가 0부터 시작해 0-44이기때문에 1을 더해 1-45로 만들기 위해서입니다. 



###  로또번호 배열

난수를 중복되지 않게  생성하고, 배열해줍니다.



```java
	public int[] makeLottoNumbers() {
		int[] lotto = new int[LOTTO_NUM]; //로또 배열방 준비
		for(int i=0;i<lotto.length;i++) {
			lotto[i] = getRandNumber(); //getRandNumber 불러온다
			for(int j=0; j<i;j++) {	//
				if(lotto[i] == lotto[j]) {//i값과 j값이 같으면 i배열 -1을 해서 뒤에 배열을 불러온다.
					i--;
					break;
				}
			}
		}
		return lotto;
	}
```



### 로또번호 배열

생성된 로또번호를 오름차순으로 정렬해줍니다.



```java
	public void sortLottoNumbers(int[] lottoNumbers) {
		for(int i=0; i<lottoNumbers.length-1; i++) {
			boolean changed = false;
			for(int j=0; j<lottoNumbers.length-1-i;j++) {
				if(lottoNumbers[j]>lottoNumbers[j+1]) {
					int temp = lottoNumbers[j];
					lottoNumbers[j] = lottoNumbers[j+1];
					lottoNumbers[j+1] = temp;
					changed = true;
				}
			}
		}
		
		
	}
```









### 로또번호 출력

생성한 배열을 출력합니다.



```java
public void printLottoNumbers(int[] lottoNumbers) {
		System.out.println("<<Lotto>>");
		for(int i=0;i<lottoNumbers.length;i++) {
			System.out.print(lottoNumbers[i]+" ");
		}
			
	}
```





# 테스트클래스

생성한 메소드 클레스를 출력하는 클레스를 만든다.





```java
public static void main(String[] args) {

		Lotto lotto = new Lotto();
		int[] lottoNumbers = lotto.generateLottoNumbers();
		lotto.sortLottoNumbers(lottoNumbers);
		lotto.displayLottoNumbers(lottoNumbers);
		
	}
```



# 결과



```java
<<Lotto>>
10 20 35 37 39 40 
```



난수이므로 숫자가 달라진다.