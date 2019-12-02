//배열의 총합을 구하시오.
// const numbers = [1, 2, 3, 4]

// //before
// for(let i=0; i<numbers.length; i++){
//   total += numbers[i]
// }

//using reduce

// let sum = numbers.reduce(function(total, num){
//   return total += num
// }, 0)
// console.log(sum)
// console.log(numbers)



//실습 1
//평균을 구하시오
const testResults = [90, 85, 70, 78, 58, 86, 99, 82]

let average = testResults.reduce(function(total, result){
  return total += result
}, 0) /testResults.length

console.log(average)



//실습 2
// 배열에 담긴 이름의 중복을 확인해서 {이름: 중복 횟수 ,이름: 중복횟수}
// 예상 답안 {"pengsu":2, "bbung": 2, "pororo":1, "bungeaman":1}
const names = ['pengsu', 'bbung', 'pororo', 'bbung','bungeaman','pensu']

let nameResults = names.reduce(function (allNames, name){
  if (name in allNames){
    allNames[name] += 1
  } else {
    allNames[name] = 1
  }
  return allNames
}, {})


console.log(nameResults)
