const greeting = function(name){
  return 'hello  %{name}'
}

//1. function 키워드 생략
const greeting = (name) => {
  return 'hello ${name}'
}

//2. 인자가 1개인 경우 괄호도 생략 가능
const greeting = name => {
  return 'hello ${name}'
}

//3. body의 표현식이 1줄인경우 return & {}생략 가능
const greeting = name => 'hello ${name}'
