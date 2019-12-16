# form

- form : action - 데이타가 전송될 URL, method - GET/POST
- input : name: key / value: value
- label : for 옵션 input 에 id값이랑 매치



## GET

- data가 body 통한게 아니라 쿼리스트링
- 데이터를 조회할때





내가 저장한 라이브러리 저장

pip freeze > requirments.txt

내가 저장한 라이브러리 불러오기

pip install -p requirments.txt





### message GET방식으로 보내고 받기

urls.py

```python
from django.shortcuts import render

# Create your views here.

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # print(request)
    # print(request.path)
    # print(request.method)
    # print(request.META)
    print(request.GET)
    message = request.GET.get('message')
    message2 = request.GET.get('message2')

    context = {
            'msg':message,
            'msg2':message2
        }

    return render(request, 'catch.html', context)
```



views.py

```python
from django.shortcuts import render

# Create your views here.

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # print(request)
    # print(request.path)
    # print(request.method)
    # print(request.META)
    print(request.GET)
    message = request.GET.get('message')
    message2 = request.GET.get('message2')

    context = {
            'msg':message,
            'msg2':message2
        }

    return render(request, 'catch.html', context)
```



throw.html

```html
<form action="/catch/" method="GET">
    <label for="msg">메세지</label>
    <input type="text" name="message" id="msg">
    <label for="msg2">메세지2</label>
    <input type="text" name="message2" id="msg2">
    <input type="submit">
</form>
```

catch.html

```html
<h1>받을 내용 : {{msg}} / {{msg2}}</h1>
```





### 로또 몇개 살거?

urls.py

```python
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('lotto/', views.lotto),
    path('lotto_result/', views.lotto_result),
]

```



views.py

```python
from django.shortcuts import render
import random

# Create your views here.


def lotto(request):
    return render(request, 'lotto.html')

def lotto_result(request):
    count = int(request.GET.get('count'))
    lotto_num = []
    for i in range(count):
       
        lotto_num.append(random.sample(range(1,47),6))
    
    context = {
        'count':count,
        'lotto_num':lotto_num
    }
    
    return render(request, 'result.html', context)
```



lotto.html

```html
<form action="/lotto_result/" method="GET">
    <label for="count">몇개 살거?</label>
    <input type="text" name="count" id="count">
    <input type="submit">
</form>
```

result.html

```html
<h1>{{count}} 개 구매함.</h1>


<ol>
{% for lotto in lotto_num %}
    <li>{{ lotto }}</li>
{% endfor %}
</ol>
```





### ARTII

1. 입력한 Text를 artii api 를 이용해서 화면에 출력
   - 텍스트를 입력받기 위해 form필요
   - 입력한 form data를 받이서 artii api에 요청
     - request모듈을 이용
     - import requests
     - requests.get("요청할 곳에 URL")
     - 요청할 URL 분석 ( http://artii.herokuapp.com/make?text=)
     - request로 받은 값을 그대로 html에 보여주면





#### GET



urls.py

```python
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('text/', views.text),
    path('text_result/', views.text_result),
]

```



views.py

```python
from django.shortcuts import render
import random
import requests

# Create your views here.


def text(request):
    return render(request, 'text.html')

def text_result(request):
    text = request.GET.get('text')

    f_url = "http://artii.herokuapp.com/fonts_list"
    fonts = requests.get(f_url).text
    fonts = fonts.split('\n')
    
    font = random.choice(fonts)

    url = f"http://artii.herokuapp.com/make?text={text}&font={font}"
    res = requests.get(url).text
    print(res)
    context = {
        'res':res
    }


    return render(request, 'text_result.html', context)
```





text.html

```html
<form action="/text_result/" method="GET">
    <label for="text">단어 입력</label>
    <input type="text" name="text" id="text">
    <input type="submit">
</form>
```



text_result.html

```html
<pre>{{res}}</pre>
```







#### POST

- 디비를 생성/변경 할때 주로사용하고 html body 정보를 담아 전송
- 원칙적으로 POST요청은 html 파일로 응답하면 안됨.
  - post요청이 오면 get요청 받는 페이지로 redirect (RESTful)

- Django는  post data를 그냥 보내지 않는다.
  - csrf_token
  - Cross Site Request Forgery
  - 토큰을 보내지 않으면
    - 403 forbidden error 넘어는갔는데 거절당함





urls.py

```python
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),

]

```



views.py

```python
from django.shortcuts import render
import random
import requests

# Create your views here.



def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    username = request.POST.get('name')
    pw = request.POST.get('pw')

    context = {
        'username':username,
        'pw':pw
    }

    return render(request,'user_create.html', context)
```



user_new.html

```html
<form action="/user_create/" method="POST">
    {% csrf_token %}
    <label for="name">이름</label>
    <input type="text" name ="name" id="name">
    <label for="pw">비밀번호</label>
    <input type="password" name="pw" id="pw">
    <input type="submit">
</form>
```



user_create.html

```html
<p>이름 : {{ username }}</p>
<p>패스워드 : {{ pw }}</p>
```





#### sandwitch

urls.py

```python
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_create/', views.user_create),
    path('menu/', views.menu),


]

```



##### 

views.py

```python
from django.shortcuts import render
import random
import requests

# Create your views here.


def menu(request):


    return render(request,'menu.html')


def subway(request):
    name = request.POST.get("name")
    date = request.POST.get("date")
    sandwitch = request.POST.get("sandwitch")
    size = request.POST.get("size")
    bread = request.POST.get("bread")
    source = request.POST.getlist("source")

    
    context = {
        'name':name,
        'date':date,
        'sandwitch':sandwitch,
        'size':size,
        'bread':bread,
        'source':source
    }


    return render(request, 'subway.html', context)        
```



menu.html

```html

    <h1>FORM</h1>
   주문서를 작성해 주십시오 <br>
    <form action="/subway/" method="POST">
        {% csrf_token %}

        이름: 
        <input type="text" name = "name" placeholder="이름을 입력하세요." autofocus> <br>
        날짜:
        <input type="date" name = "date"> <br>

        <h2>1. 샌드위치 선택</h2>
        <div>
                <input type="radio" name="sandwitch" value="에그마요"> 에그마요 <br>
                <input type="radio" name="sandwitch" value="이탈리안 비엠티">이탈리안 비엠티 <br>
                <input type="radio" name="sandwitch" value="터키 베이컨 아보카도"> 터키 베이컨 아보카도 <br>

        </div>

        <hr>

        <h2>2. 사이즈 선택</h2>
        <div>
            <input type="number" name="size" min="15" max="30" value="15" step="5">
        </div>
        <hr>

        <h2>3. 빵</h2>
        <select name="bread">
                <option value="허니오트">허니오트</option>
                <option value="블랫프래드">블랫프래드</option>
                <option value="이탈리안">이탈리안</option>
    
        </select>
        
        <hr>

        <h2>4. 야채/소스</h2>
            <div>
                    <input type="checkbox" name="source" val="1">토마토 <br>
                    <input type="checkbox" name="source" val="2">오이 <br>
                    <input type="checkbox" name="source" val="3">할라피뇨 <br>
                    <input type="checkbox" name="source" val="4">핫 칠리 <br>
                    <input type="checkbox" name="source" val="5">바베큐 <br>
          </div> <br>
          <input type="submit" value="submit">



    </form>

```



subway.html

```html
<h1>{{name}}님이 주문 하신 결과는</h1>

<p>{{sandwitch}} / {{size}} 크기로</p>
<p>{{bread}}에 {{source}}입니다</p>
<p>날짜는 {{date}} 입니다.</p>
```

#### static

urls.py

```python
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('static_ex/', views.static_ex),

]

```





views.py

```python
from django.shortcuts import render
import random
import requests

# Create your views here.


def static_ex(request):
    return render(request, 'static.html')          
```



static.html

```python
{% load static %}


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'stylesheet/style.css' %}">
</head>
<body>
    <h1>Static 파일 실습</h1>
    <img src="{% static 'images/bob.jpg' %}" alt="스폰지밥">
     
</body>
</html>
```







## urls.py 분류

app 별로 path를 관리

urls.py

```python
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]

```





pages.urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
    path('lotto_result/', views.lotto_result),
    path('text/', views.text),
    path('text_result/', views.text_result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('menu/', views.menu),
    path('subway/', views.subway),
    path('static_ex/', views.static_ex),


]
```









### views 재설정



views경로에 pages/를 붙인다.

```python
from django.shortcuts import render
import random
import requests

# Create your views here.

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    # print(request)
    # print(request.path)
    # print(request.method)
    # print(request.META)
    print(request.GET)
    message = request.GET.get('message')
    message2 = request.GET.get('message2')

    context = {
            'msg':message,
            'msg2':message2
        }

    return render(request, 'pages/catch.html', context)

def lotto(request):
    return render(request, 'pages/lotto.html')

def lotto_result(request):
    count = int(request.GET.get('count'))
    lotto_num = []
    for i in range(count):
       
        lotto_num.append(random.sample(range(1,47),6))
    
    context = {
        'count':count,
        'lotto_num':lotto_num
    }
    
    return render(request, 'pages/result.html', context)

def text(request):
    return render(request, 'pages/text.html')

def text_result(request):
    text = request.GET.get('text')

    f_url = "http://artii.herokuapp.com/fonts_list"
    fonts = requests.get(f_url).text
    fonts = fonts.split('\n')
    
    font = random.choice(fonts)

    url = f"http://artii.herokuapp.com/make?text={text}&font={font}"
    res = requests.get(url).text
    print(res)
    context = {
        'res':res
    }


    return render(request, 'pages/text_result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    username = request.POST.get('name')
    pw = request.POST.get('pw')

    context = {
        'username':username,
        'pw':pw
    }

    return render(request,'pages/user_create.html', context)

def menu(request):


    return render(request,'pages/menu.html')


def subway(request):
    name = request.POST.get("name")
    date = request.POST.get("date")
    sandwitch = request.POST.get("sandwitch")
    size = request.POST.get("size")
    bread = request.POST.get("bread")
    source = request.POST.getlist("source")

    
    context = {
        'name':name,
        'date':date,
        'sandwitch':sandwitch,
        'size':size,
        'bread':bread,
        'source':source
    }


    return render(request, 'pages/subway.html', context)

def static_ex(request):
    return render(request, 'pages/static.html')

def index(request):
    return render(request, 'pages/index.html')          
```



### templates 상속



setttings.py

​        'DIRS': [os.path.join(BASE_DIR, '프로젝트 셋팅즈에있는 폴더명', 'templates')],

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'config', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```





config폴더에 templates폴더에 작성

base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>{% block title %} {% endblock %}</title>
</head>
<body>
    <h1>장고 BASE HTML</h1>


    <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item active">
                  <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Features</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Pricing</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                </li>
              </ul>
            </div>
          </nav>

    {% block body %}
    {% endblock %}
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

{% block 블럭이름%} {% endblock %}을 html 파일안 원하는 곳에 둔다.





index.html

```html
{% extends 'base.html' %}

{% block body%}

<h1>여기는 PAGES INDEX 입니다.</h1>
{% endblock%}

```





text.html

```html
{% extends 'base.html' %}
{% block title %}
Artii
{% endblock%}

{% block body%}
<form action="/pages/text_result/" method="GET">
    <label for="text">단어 입력</label>
    <input type="text" name="text" id="text">
    <input type="submit">
</form>
{% endblock%}
```

