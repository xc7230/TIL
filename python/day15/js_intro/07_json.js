//JSON -> Object
// let jsonStr = JSON.parse('{"name": "pengsu", "age":"10"}');
// console.log(typeof jsonStr)


//Object -> JSON
let obj = {
  name: 'pengsu',
  age: '10'
}
console.log(typeof obj)
let jsonObj = JSON.stringify(obj);
console.log(typeof jsonObj)
console.log(jsonObj)

