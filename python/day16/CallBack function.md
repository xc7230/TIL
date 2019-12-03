# CallBack function

- 다른 함수에 인수로 넘겨지는 함수



## 인스톨

Live Server



```js
function doSomething(task, callback){
    alert('자, ${task} 준비를 해봅시다!!')
    callback()
}

doSomthing('탕수육 먹을', function(){
    alert('누가 뿜빠이로 맛난 탕수육 먹으러 갑시다!')
})
```



