function doSomething(task, callback){
  alert('자, ${task} 준비를 해봅시다!!')
  callback()
}

doSomething('탕수육 먹을', function(){
  alert('누가 뿜빠이로 맛난 탕수육 먹으러 갑시다!')
})

function whereGO(){
  alert('탕수육 어디가 맛나나요??')
}

doSomething('탕수육 먹을', whereGO)
