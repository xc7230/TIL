// const PRODUCTS = [
//   { name : 'cucumber', type:'vegetable'},
//   { name : 'banana', type:'fruit'},
//   { name : 'carrot', type:'vegetable'},
//   { name : 'apple', type:'fruit'},
// ]


//before
// var selectProducts = []
// for (var i=0; i<PRODUCTS.length; i++){
//   if(PRODUCTS[i].type === 'vegetable'){
//     selectProducts.push(PRODUCTS[i])
//   }
// }
// console.log(selectProducts)

// let selectProducts = PRODUCTS.filter(function(prod){
//   return prod.type === 'vegetable'
// })

// console.log(selectProducts)
// console.log(PRODUCTS)


//실습 #1
//80점 이상인 결과만 따로 배열로 만들어봅시다.
const testResults = [90, 85, 70, 78, 58, 86, 99, 82]
let results = testResults.filter(function (test){
  return test > 80
})

console.log(results)
console.log(testResults)
