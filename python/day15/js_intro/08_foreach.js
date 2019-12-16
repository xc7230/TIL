//예전 방식
var colors = ['red','orange','yello']
for(var i = 0; i <colors.length; i++){
  console.log(colors[i])
}

const COLORS = ['red','orange','yellow']
//use forEach
COLORS.forEach(function(color){
  console.log(color)
})

let result = COLORS.forEach(color=> console.log(color))
console.log(result)

//실습 넘버 1
// function hendlePosts() {[{
//   id: 23,
//   title: "오늘의 뉴스"
// },
// {
//   id:78,
//   title: "오늘의 연예"

// }]

//   // for(let i = 0; i < posts.length ; i++){
//   //   console.log(posts[i])
//   //   console.log(posts[i].id)
//   //   console.log(posts[i].title)
//   // }
//   posts.forEach(function(post){
//     console.log(post)
//     console.log(post.id)
//     console.log(post.title)
//   })
// }

// hendlePosts()


//실습 2
//image 배열 안에 있는 정보를 가지고
//넓이를 구하고 그 값을 areas에 저장해보자
const IMAGES = [
  {hight:10, width:30},
  {hight:22, width:37},
  {hight:54, width:42},
]
let areas = []

IMAGES.forEach(img =>  areas.push(img.hight * img.width))
console.log(areas)
