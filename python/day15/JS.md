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