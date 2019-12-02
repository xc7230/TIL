//배열에 모든 요소에 2를 곱하여 새로운 배열로 만들기.
//befor
// var numbers = [1,2,3]
// var doubleNumber = []

// for(var i = 0; i < numbers.length; i++){
//   doubleNumber.push(numbers[i]*2)
// }

// map을 사용
let numbers = [2,4,6]
let doubleNum = numbers.map(function(num){
  return num*2
})

console.log(numbers)
console.log(doubleNum)
