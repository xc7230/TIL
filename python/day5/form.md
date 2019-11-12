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

