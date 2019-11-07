# CSS

- em 배수 단위로 상대 단위 이다. 요소에 지정된 사이즈에 상대적인 사이즈를 설정한다.
- rem 최상위 요소(html)의 사이즈를 기준으로 삼는다. rem 의 r은 root를 의미한다.
- 색상
- box model
  - margin = Padding 상하좌우
  - border 테두리

- absolute 절대위치 부모또는 조상 요소를 기준으로 위치가 결정
- fixed 고정위치



box.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="box.css">
</head>
<body>
        <div class="base-box">
                <div class="box pink">
                    <div class="box orange"></div>
                </div>
                <div class="box blue"></div>
                <div class="box green">
                    <div class="box purple"></div>
                </div>
                <div class="box yellow"></div>
                <div class="box red"></div>
        
                </div>
        
            </div>
        </div>
        
</body>
</html>
```



box.css

```css
.base-box {
    width: 500px;
    height: 500px;
    border: solid 2px black;
}

.box {
    width: 100px; 
    height: 100px;
}

.pink {
    background-color : pink;
    position : relative;
}

.blue {
    background-color: blue;
    position: relative;
    left: 100px
}

.green {
    background-color: green;
    position: relative;
    left: 200px;
}

.yellow {
    background-color: yellow;
    left: 700px;
    top: 300px;
    position: relative;
}

.red {
    background-color : red;
    left: 400px;
    position: relative;
}

.orange {
    background-color: orange;
    left: 200px;
    position: absolute;
}

.purple {
    background: purple;
    left: 100px;
    top: 100px;
    position: absolute;
}
```





boostrap

 https://getbootstrap.com/docs/4.3/getting-started/introduction/ 

css js 설정하기



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <h1>Hello bootstrap</h1>
    <a href="http://getbootstrap.com"> GO to bootstrap</a> 
    <button type="button" class="btn btn-secondary">Secondary</button>
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
        Launch demo modal
      </button>
      
      <!-- Modal -->
      <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              ...
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary">Save changes</button>
            </div>
          </div>
        </div>
      </div>




      <div class="container">
            <!-- Stack the columns on mobile by making one full-width and the other half-width -->
            <div class="row">
              <div class="col-12 col-md-8">.col-12 .col-md-8</div>
              <div class="col-6 col-md-4">.col-6 .col-md-4</div>
            </div>
          
            <!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop -->
            <div class="row">
              <div class="col-6 col-md-4">.col-6 .col-md-4</div>
              <div class="col-6 col-md-4">.col-6 .col-md-4</div>
              <div class="col-6 col-md-4">.col-6 .col-md-4</div>
            </div>
          
            <!-- Columns are always 50% wide, on mobile and desktop -->
            <div class="row">
              <div class="col-6">.col-6</div>
              <div class="col-6">.col-6</div>
            </div>
          </div>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```



animate.css





 https://github.com/daneden/animate.css 



animate.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css">

</head>
<body>
        <h1 class="animated infinite bounce delay-2s">Example</h1>


</body>
</html>
```



# 파이썬

 https://wikidocs.net/book/1 



```python
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9]
}

#도시별 최근 3일의 온도 평균은?


for name, temp in city.items():
    avg_temp = sum(temp)/len(temp)
    print(f'{name} : 평균기온은 {avg_temp} 입니다.')
```



```python
$ python a.py
서울 : 평균기온은 -3.6666666666666665 입니다.
대전 : 평균기온은 -2.0 입니다.
광주 : 평균기온은 2.6666666666666665 입니다.
부산 : 평균기온은 3.0 입니다.
```



```python
#3-2위에서 서울은 영상 2도였던 적이 있나요??
# A if 조건문 else B : 조건문이 참이면 A 거짓이면 B
print("있어요") if 2 in city["서울"] else print("없어요") 



$ python a.py
없어요
```







## 플라스크

독립적인 환경 구축 버전충돌 방지

$ pip install virtualenv

$ virtualenv venv 가상환경 구축

$ source venv/Scripts/activate 가상환경 진입
(venv) 

$ env Flask_APP=hello.py flask run





app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    name = "World!!"
    return f'Hello {name}!'


if _name_="_main_":
    app.run(debug=True, port=8000)
    

python app.py

```





```
$ env Flask_APP=hello.py flask run
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [07/Nov/2019 13:14:59] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [07/Nov/2019 13:14:59] "GET /favicon.ico HTTP/1.1" 404 -
```

http://127.0.0.1:5000/   접속





```python
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = "World!!"
    return f'Hello {name}!'


#  @app.route('/mulcam')
#  def mulcam():
#     return 'Hello mulcamp'

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'{name}님 안녕하세요'

@app.route('/lunch/<int:num>')
def lunch(num):
    menu = ["짜장면", "짬뽕", "라면", "스파게티", "스테이크", "삼겹살"]
    order = random.sample(menu, num)
    return str(order)

if __name__=="__main__":
    app.run(debug=True, port=8000)

```



 http://127.0.0.1:8000/lunch/3 





Lotto

```python
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = "World!!"
    return f'Hello {name}!'


# 로또 번호
@app.route('/lotto')
def lotto():
    RandomNum = random.sample(range(1,47),6)
    return str(RandomNum)

if __name__=="__main__":
    app.run(debug=True, port=8000)
```

 http://127.0.0.1:8000/lotto





html

```python
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = "World!!"
    return f'Hello {name}!'


@app.route('/html')
def html():
    multiline = '''
    <h1> This is H1 Tag </h1>
    <p> This is P Tag </p>
    '''
    return multiline


@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', name=name)


if __name__=="__main__":
    app.run(debug=True, port=8000)
```



 [http://127.0.0.1:8000/hi/%EC%A0%95%ED%98%84](http://127.0.0.1:8000/hi/정현) 





fake_search

```python
from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')

@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')

if __name__=="__main__":
    app.run(debug=True, port=8000)
```

fake_naver.html

```html
<form action="https://search.naver.com/search.naver">
    <input type="text" name="query">
    <input type="submit">
</form>
```

fake_google.html

```html
<form action="https://www.google.com/search">
    <input type="text" name="q">
    <input type="submit">
</form>
```







쓰고 받기

app.py

```python
@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('receive.html', name=name, msg = message)
```



send.html

```html
<form action="/receive" method="GET">
    이름: <input type="text" name="name"><br>
    메세지: <input type="text" name="message">
    <input type="submit" value="보내기">
</form>
```

receive.html

```html
<h1>{{name}} : {{msg}}</h1>
```







indian

app.py

```python
#인디언
@app.route('/indian')
def indian_send():
    return render_template('indian_send.html')


@app.route('/indian_receive')
def indian_receive():
    date = request.args.get('date')
    year = date[3:4]
    month = date[5:7]
    day = date[8:10]


    year_arr = ['시끄러운, 말 많은', '푸른', '어두운', '조용한', '웅크린', '백색', '지혜로운', '용감한', '날카로운', '욕심 많은']
    month_arr = ['늑대','태양','양','매','황소','불꽃','나무','달빛','말','돼지','하늘','바람']
    day_arr  = ["의 환생","의 죽음","아래에서","를(을) 보라","이(가) 노래하다","그림자","의 일격","에게 쫒기는 남자","의 행진 ","의 왕","의 유령","을 죽인자","는(은) 맨날 잠잔다","처럼","의 고향","의 전사","은(는) 나의친구","의 노래","의 정령","의 파수꾼","의 악마","와(과) 같은 사나이","를(을) 쓰러트린자","의 혼 ","은(는) 말이 없다"]

    name= year_arr[int(year)-1] + month_arr[int(month)-1] + day_arr[int(day)-1]

    return render_template('indian_receive.html', name=name, date = date)
```



indian_send.html

```html
<form action="/indian_receive" method="GET">
    이름: <input type="text" name="name"><br>
    날짜: <input type="date" name="date">
    <input type="submit" value="보내기">
</form>
```



indian_receive.html

```html
<h1>{{date}} : {{name}}</h1>
```

