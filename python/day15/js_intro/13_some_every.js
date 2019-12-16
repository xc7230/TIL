const NUMBERS = [1,2,3,4,5]

//some
const everu_result = NUMBERS.some(function(elem){
  return elem % 2 === 0
})
console.log(everu_result)

//every
const every_result = NUMBERS.every(function(elem){
  return elem % 2 === 0
})
console.log(every_result)
