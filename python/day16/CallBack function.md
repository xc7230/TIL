# CallBack function

- 다른 함수에 인수로 넘겨지는 함수



## 인스톨

Live Server



```js
function doSomething(task, callback){
    alert('자, ${task} 준비를 해봅시다!!')
    callback()
}

doSomthing('탕수육 먹을', function(){
    alert('누가 뿜빠이로 맛난 탕수육 먹으러 갑시다!')
})
```





```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <p id="para">어떤 휴지 줄까</p>
  <button onclick="changeColor('red', _=>alert('빨간휴지'))">빨간 휴지</button>
  <button onclick="changeColor('blue',()=>alert('파란휴지'))">파란 휴지</button>

  <script>
  function changeColor(newColor, callback) {
    const elem = document.getElementById('para')
    elem.style.color = newColor
    callback()
    }
  </script>
</body>
</html>

```



## EventListener

- EventTarget.addEventListener(type, callback)
  - EventTarget : 이벤트 리스너를 등록할 대상
  - type : 이벤트 유형을 뜻하는 문자열.
  - 이벤트종류 : http://www.ktword.co.kr/word/abbr_view.php?m_temp1=2744&id=1356
  - callback : 이벤트가 발생했을때 처리를 담당, e (event객체)
    - 이벤트가 발생했을때 실행되는 절차\
      - 무엇을 EventTarget 을
      - 언제 type 이벤트가 발생했을때
      - 어떻게 callback 함수에 구현된 내용을 실행한다.



## BOM & DOM

### BOM(Browser Object Model)

- JS 브라우저와 소통하기 위한 모델

  - 브라우저에 따라 다르게 구현되기도 하고 한정적임.

- 웹 브라우저의 버튼, URL 주소 입력, 타이틀바 같은 브라우저 일부분을 제어할 수 있다.

- window 객체로 접근가능

  - 전역 JS 객체, 함수, 변수들은 자동으로 window 객체의 맴버가 됨.

  - HTML DOM 역시 window 객체의 속성

    ```js
    window.print()//인쇄창 오픈
    window.open() //탭 오픈
    window.document // document도 브라우저 종속 -> window 전역객체에 포함.
    window.confirm() // 확인&취소 버튼이 있는 대화상자를 표시
    ```

    

### DOM(Document Object Model)

- HTML 파일에 작성된 요소(Element)들을 조작할 수 있다.
- 요소에 이벤트를 등록해서, 특정 이벤트가 발생할시 특정 함수를 실행하도록 할 수 있다.
- HTML 문서에 작성하지 않은 내용도 새로운 요소를 생성해서 추가할 수 있다.

#### DOM Tree

![img](https://miro.medium.com/max/960/1*aYBX0u4He3VThBSVLJ7BJA.jpeg)

요소를 선택하여 변수를 할당

- document의 querySelector (getElementById, .....)
- querySelector : 위에서 부터 css 선택자 요소를 찾으면 가장 먼저 찾아지는 요소를 반환
- querySelectorAll : 일치하는 모든 요소를 반환

```js
const bg = document.querySelector('.bg')
```

부모에서 자식요소 선택하기

```js
const movcon = bg.querySelector('#movcon')
```

요소를 선택하여 변수를 할당

- document의 querySelector (getElementById, .....)
- query







## 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>My Wish List</h1>
  내가 원하는건 : <input type="text" id="wish-input">
  <button id="add-button">추가하기</button>

  <ol id="wish-list">


  </ol>

  <script>
    //1. input 태그를 선택하여 변수에 담는다.
    const input = document.querySelector('#wish-input')
    //2. button 태그를 선택하여 변수에 담는다.
    const button = document.querySelector('#add-button')
    //3. ol 태그를 선택하여 변수에 담는다.
    const ol = document.querySelector('#wish-list')

    //4. 버튼을 클릭했을떄
    button.addEventListener('click', function(){
      //5. input 태그에 value를 변수에 담는다.
      const wish = input.value
      //6. input 태그에 입력되어진 value를 초기화 한다.
      input.value = ''
      //7. li 태그를 생성해서 변수애 담는다.
      const item = document.createElement('li')
      //8. li 태그가 저장된 변수에 input value를 담는다. innerText
      item.innerText = wish

      // 2-1 delete 버튼 태그 생성
      const delButton = document.createElement('button')

      // 2-2 delete 버튼에 버튼이름 지정
      delButton.innerText = "요거 했음"

      // 2-3 delete 버튼을 item에 마지막 요소로 추가
      item.append(delButton)

      // 2-4 버튼을 누르면 해당 아이템을 삭제
      delButton.addEventListener('click', function(){
        item.remove()
      })

      //9. ol 태그에 li 요소를 추가한다.
      ol.append(item)
    })
  </script>
</body>
</html>


```

