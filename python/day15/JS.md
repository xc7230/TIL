# JS

## 인스톨 EXTENTIONS

1. Auto Close Tag
2. Rainbow Brackets
3. indent-rainbow
4. Beautify
5. Code Runner
6.  ESLint




file 

![image-20191202103905960](C:%5CUsers%5Cstudent%5CDocuments%5CGitHub%5CTIL%5Cpython%5Cday15%5CJS.assets%5Cimage-20191202103905960.png)



```json
{
    "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
    "editor.snippetSuggestions": "top",
    "editor.tabCompletion": "on",
    "[html]": {
        "editor.tabSize": 2
        },
        "[css]": {
        "editor.tabSize": 2
        },
        "[python]": { // 추가!
        "editor.tabSize": 4,
        },
        "terminal.integrated.fontSize": 16,
        "editor.tabSize": 2,
        
        
        
        "beautify.language": {
        "js": {
        "type": ["javascript", "json"],
        "filename": [".jshintrc", ".jsbeautifyrc"]
        // "ext": ["js", "json"]
        // ^^ to set extensions to be beautified using the javascript beautifier
        },
        "css": ["css", "scss"],
        "html": ["htm", "html", "django-html"]
        // ^^ providing just an array sets the VS Code file type
        },
        
        
        "files.insertFinalNewline": true,
        
        "terminal.integrated.cwd": "${workspaceFolder}",
}
```



![image-20191202104147770](C:%5CUsers%5Cstudent%5CDocuments%5CGitHub%5CTIL%5Cpython%5Cday15%5CJS.assets%5Cimage-20191202104147770.png)

체크 확인



![image-20191202104239884](C:%5CUsers%5Cstudent%5CDocuments%5CGitHub%5CTIL%5Cpython%5Cday15%5CJS.assets%5Cimage-20191202104239884.png)





단축키 지정

![image-20191202104350583](C:%5CUsers%5Cstudent%5CDocuments%5CGitHub%5CTIL%5Cpython%5Cday15%5CJS.assets%5Cimage-20191202104350583.png)



## Naming Convention

- lowerCamelCase : 일반적인 Camel case
- UpperCamelCase
- snake_case
- Hugarian notation : u16number / s32num
- kebab-case



## JS의 변수

### let 

선언은 1번만 가능. 재할당은 계속가능. block scope

![image-20191202111249892](C:%5CUsers%5Cstudent%5CDocuments%5CGitHub%5CTIL%5Cpython%5Cday15%5CJS.assets%5Cimage-20191202111249892.png)



### **const** 

선언도 1번만 가능, 재할당은 불가능. block scope

![image-20191202111604539](C:%5CUsers%5Cstudent%5CDocuments%5CGitHub%5CTIL%5Cpython%5Cday15%5CJS.assets%5Cimage-20191202111604539.png)

### **var** 

ES6 이전에 문제가 많이 발생했다.

- hoisting

  ![image-20191202111936973](C:%5CUsers%5Cstudent%5CDocuments%5CGitHub%5CTIL%5Cpython%5Cday15%5CJS.assets%5Cimage-20191202111936973.png)

```
function text() {
var n ;
console.log(n)
n = 2
console.log(n)
}
```



## 조건문

### if else if

```js
const userName = prompt("니 이름이 뭐?");

let message = ""

if(userName === "pengsu") {
  message = "우주 대스타";
}else if(userName === "bbung"){
  message = "냄세.......";
}else {
  message = "<h1>어서오세요. ${userName}</h1>";
}

message;
document.write(message)

```



### loop문



### while

```js
let i = 0;

while (i < 10) {
  console.log(i);
  i++;
}

//Ctrl + Alt + n으로 실행
```



### for

```js
let i = 0;

for( let j = 10; j > 0; j--){
  console.log(j)
}

```



#### for of

```js
const numbers = [1,2,3,4,5,6,7]

for(let num of numbers){
  console.log(num)
}

```



for in

```js
let sampleObj = {
  a: 1,
  b: "hello",
  c: [3, 4]
}

for ( let obj in sampleObj){
  console.log(obj)
  console.log(sampleObj[obj])
}
```



## 함수



### 선언식

```js
function add(num1, num2){
  return num1 + num2
}

let sum = add(5, 7)
console.log(sum)

```



### 표현식

```js
const sub = function(num1, num2){
  return num1- num2
}

let val = sub(12, 5)
console.log(val)
```



```js
console.log(typeof add)
console.log(typeof sub)


function
function
```





## 화살표 함수

- 익명 함수
- function 표현에 비해 구문이 짧다.
- 생성자로 사용할수가 없음.
- 사용법:
  - function을 생략
  - 인자가 1개인 경우 괄호도 생략할 수 있다.
  - return 이랑 {}도 생략이 가능



```js
let square = (num) => {
  return num **2
}

//2인자가 1개인 경우
let square = num => {
  return num **2
}

//3.body 부분이 1개로 되어 있을때
let square = num => num**2

//인자가 없다면

let noArgs = function(){
  return 'no Args'
}

let noArgs = () => 'no Args'
let noArgs = _ => 'no Args'

//object 형식으로 반환 된다면?
let returnObj = () => {
  return {key:'value'}
}

let returnObj = () => ({key:'value'})
console.log(returnObj())


인자가 기본값을 성정했을 경우
let sayHi = function(name="pengsu") {
  return 'hi ${name}'
}

let sayHi = (name="pengsu") => `hi ${name}`
console.log(sayHi(`bbung`))


//즉시 실행 함수


// 기존
const cube = function(num){
  return num ** 3
}

console.log(cube(2))

//익명함수
console.log(function(num){return num ** 3}(4))


//익명함수 즉시 실행
console.log(function(num){return num ** 3}(3))
```



## 배열



```js
const numbers = [1, 2, 3, 4, 5, 6, 7]
console.log(numbers[1]) //양의 정수만 가능
console.log(numbers.length)

//뒤의 값 출력
console.log(numbers.reverse())
//reverse를 하면 원본값이 뒤집힘
console.log(numbers[0])

```





### push

배열의 마지막에 push 값을 넣어줌

```js
numbers.push('peng') //return 값은 배열의 길이
console.log(numbers)
console.log(numbers.push('su'))
```



### pop

```js
const numbers = [1, 2, 3, 4, 5, 6, 7]
console.log(numbers.pop())
console.log(numbers)
```





### unshift

```js
console.log(numbers.unshift("pengsu"))
console.log(numbers)
```



### shift

```js
console.log(numbers.shift())
console.log(numbers)
```





### include

```js
const numbers = [1, 2, 3, 4, 5, 6, 7]


//포함 유뮤 확인
console.log(numbers.includes(1))
console.log(numbers.includes(0))

// index 정보를 알아보는 친구
console.log(numbers.indexOf(2))
numbers.push('peng', 'peng')
console.log(numbers)
console.log(numbers.indexOf('peng'))
```



### join

```js
const numbers = [1, 2, 3, 4, 5, 6, 7]
console.log(numbers.join('-'))
console.log(numbers.join())
console.log(numbers.join(''))
console.log(numbers) //원본을 지킨다.
```



## object

```js
const pengsu = {
  name : "팽수",
  "phone number" : "01012345678",
  profile:{
    dream: "우주대스타",
    age:'10살',
    speciality:"요들송"
  }
}
console.log(pengsu.name)
console.log(pengsu['name'])

let bookShop = {
  books,
  comics,
  magazines
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])

```





## JSON

- 문자열이기에 object로 쓰기위해 변환과정이 필요



JSON -> Object

```js
let jsonStr = JSON.parse('{"name": "pengsu", "age":"10"}');
console.log(typeof jsonStr)
```



Object -> JSON

```js
let obj = {
  name: 'pengsu',
  age: '10'
}
console.log(typeof obj)
let jsonObj = JSON.stringify(obj);
console.log(typeof jsonObj)
console.log(jsonObj)
```

