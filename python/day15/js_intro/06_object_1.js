//before

var books = ['Learning JS', 'Learning Django']
var comics = {
  DC: ['AquaMan', 'SuperMan'],
  Marvel: ['IronMan', 'AntMan']
}

var magazines = null;


//bofore
// var bookShop = {
//   books: books,
//   comics: comics,
//   magazines: magazines
// }

//after
let bookShop = {
  books,
  comics,
  magazines
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])
