const greeting = function(name){
  return 'hello  %{name}'
}

// //1. function 키워드 생략
// const greeting = (name) => {
//   return 'hello ${name}'
// }

// //2. 인자가 1개인 경우 괄호도 생략 가능
// const greeting = name => {
//   return 'hello ${name}'
// }

// //3. body의 표현식이 1줄인경우 return & {}생략 가능
// const greeting = name => 'hello ${name}'



//=> 화살표 함수로 변환시켜 보자.
//1. function 이름
// let square = (num) => {
//   return num **2
// }

// //2인자가 1개인 경우
// let square = num => {
//   return num **2
// }

// //3.body 부분이 1개로 되어 있을때
// let square = num => num**2

// //인자가 없다면

// let noArgs = function(){
//   return 'no Args'
// }

// let noArgs = () => 'no Args'
// let noArgs = _ => 'no Args'

// //object 형식으로 반환 된다면?
// let returnObj = () => {
//   return {key:'value'}
// }

// let returnObj = () => ({key:'value'})
// console.log(returnObj())

// 인자가 기본값을 성정했을 경우
// let sayHi = function(name="pengsu") {
//   return 'hi ${name}'
// }

// let sayHi = (name="pengsu") => `hi ${name}`
// console.log(sayHi(`bbung`))

//즉시 실행 함수


// 기명 함수 일때 즉시 실행
const cube = function(num){
  return num ** 3
}

console.log(cube(2))

//익명함수 즉시 실행
console.log(function(num){return num ** 3}(3))


