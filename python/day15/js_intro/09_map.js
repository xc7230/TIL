//배열에 모든 요소에 2를 곱하여 새로운 배열로 만들기.
//befor
// var numbers = [1,2,3]
// var doubleNumber = []

// for(var i = 0; i < numbers.length; i++){
//   doubleNumber.push(numbers[i]*2)
// }

// map을 사용
// let numbers = [2,4,6]
// let doubleNum = numbers.map(function(num){
//   return num*2
// })

// let doubleNum = numbers.map(num=>num*2)
// console.log(numbers)
// console.log(doubleNum)


//실습 #1
//숫자가 담긴 배열을 받아서
//각 숫자들의 제곱근이 들어있는 새 배열로 만들어 보자

// const newNum = [4, 9, 16]

// let roots = newNum.map(function(num){
//   return num**0.5
// })
// console.log(roots)


//실습 #2
//images 배열안에 Object 들의
//height만 저장되어 있는 배열을 만들어 보자
const IMAGES = [
  {height: '34px', width: '39px'},
  {height: '54px', width: '22px'},
  {height: '48px', width: '22px'},
]

let heights = IMAGES.map(function (img){
  return img.height
})
console.log(heights)


//실습 #3
//{name : brand, movie: 영화}
//[{name:Marvel, movie:Avengers}, {name:DC, movie:Batman}]

const brands = ["Marvel","DC"]
const movies = ["Avengers", "Batman"]

// const Heroes = brands.map(function (brand, idx){
//   return {name: brand, movie:movies[idx]}
// })

const Heroes = brands.map((brand, idx) => ({name:brand, movie:movies[idx]}))

console.log(Heroes)
