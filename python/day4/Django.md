# Django

웹서비스를 만드는 프로그램

flask보다 무겁다. 큰 프로젝트를 하면 결국 Django와 유사

## MTV패턴

Model, Template, view

MVC와 같다.



```pip
pip install django
```





## Django 환경 만들기

```python
django-admin startproject config .
```



### Server만들기

기본 8000번 포트

```python
python manage.py runserver
```

## settings.py

ALLOWED_HOSTS[] : 배포할때 사용도메인 입력

만들때 먼저 바꾼다.

```python
LANGUAGE_CODE = 'ko-kr'



TIME_ZONE = 'Asia/Seoul'
```





## app

page app 만들기

```python
python manage.py startapp pages
```

### models.py

클래스명 = 테이블 명

설정하는 변수들이 컬럼



### tests.py



### views.py

주요 동작 기능

함수구현

settings.py 에서 INSTALLED_APPS에 내가 만든 app("pages")를 입력 해야한다.(상단부터 ,를 찍어야함 urls에서 관리하는 app은 하단부터)



```python
@app.route('/index') => urls.py

#밑에 부분은 views.py
def index():
    return render_template('index.html')
```



초기 설정

urls.py

```python
from django.contrib import admin
from django.urls import path
from . import pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages.views.index),
]

```



views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello Django")
```







### Templates 적용



views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

```



index.html

```html
<h1>Index Page</h1>
<p>Hello Django!!!!</p>
```

urls > views > templates 순서로 작성



### 동적부분

```python
@app.route('/index/<int:num>') => urls.py

#밑에 부분은 views.py
def index():
    return render_template('index.html')
```



int : 0또는 양의 정수 매치

 str : / 를 제외한 모든 문자열과 매치, 디폴트 값

slug : slug 형식( ASCII, 숫자, 하이픈, 밑줄)과 매치

uuid : uuid 형식의 문자열과 매치



urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('<int : age>/', views.age),
]
```

 views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def age(request, age):
    context = {
        'age' : age
        }
    return render(request, 'age.html', context)
```

age.html

```html
<h1>{{ age }}</h1>
```





실습1

사칙연산

ursl.py

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
    path('', views.index),
    path('<int:age>/age', views.age),
    path('<int:squared>/squared', views.squared),
    path('<int:num>/<int:num2>/plus', views.plus),
    path('<int:num>/<int:num2>/minus', views.minus),
    path('<int:num>/<int:num2>/division', views.division),
    path('<int:num>/<int:num2>/mult', views.mult),
    
]

```



views.py

```python
from django.shortcuts import render
from django.http import HttpResponse
import random
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def age(request, age):
    context = {
        'age' : age
        }
    return render(request, 'age.html', context)

def squared(request, squared):

    context = {
        'squared':squared**2
        }
    return render(request, 'squared.html', context)

def plus(request, num, num2):

    result = {
        'result':num + num2
        }
    return render(request, 'num.html', result)

def minus(request, num, num2):

    result = {
        'result':num - num2
        }
    return render(request, 'num.html', result)

def division(request, num, num2):

    result = {
        'result':num / num2
        }
    return render(request, 'num.html', result)

def mult(request, num, num2):

    result = {
        'result':num * num2
        }
    return render(request, 'num.html', result)
```





num.html

```html
<h1>{{ result }}</h1>
```





실습

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
    path('', views.index),
    path('<int:age>/age', views.age),
    path('<int:squared>/squared', views.squared),
    path('<int:num>/<int:num2>/plus', views.plus),
    path('<int:num>/<int:num2>/minus', views.minus),
    path('<int:num>/<int:num2>/division', views.division),
    path('<int:num>/<int:num2>/mult', views.mult),
    path('<str:name>/<int:age>/profile', views.profile),
    
]

```



views.py

```python
from django.shortcuts import render
from django.http import HttpResponse
import random
import requests


def profile(request, name, age):

    list_1 = ['말 많은', '푸른', '어두운', '웅크린', '조용한', '용감한', '지혜로운']
    list_2 = ['늑대', '태양','양', '매', '황소', '불꽃']
    list_3 = ['와 함께 춤을', '의 기상', '은 그림자 속에', '의 환생', '의 죽음', '아래에서', '을 보라', '의 그림자']
    l1 = random.choice(list_1)
    l2 = random.choice(list_2)
    l3 = random.choice(list_3)
    indian = l1 + l2 + l3

    #로또
    num = range(1,47) # range(시작값, 끝값) : 시작값<= x <끝값  범위의 숫자를 List 형태로 반환함.
    lotto = sorted(random.sample(num, 6))

    l_num = [str(l) for l in lotto ]


    
   
    result = {
        'name':name,
        'age':age,
        'indian': indian,
        'lotto': ", ".join(l_num)

        }
    return render(request, 'profile.html', result)

```





profile.html

```html

<h3>안녕! 난 불꽃 열정을 가진[{{name}}]!</h3>
<h3>겁없는 [{{age}}]살 이지.</h3><br>

<h3>내 인디언 스승인 <{{indian}}>님이 로또를 점지해 줄거야!!</h3>
<h3>이번주 로또는 {{lotto}}!!!</h3>
<h3>행운이 있길 바래 - 씇!</h3>

```





### Faker

pip install faker

usls.py

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
    path('faker/<str:name>', views.faker), 
]

```



views.py

```python
from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
from faker import Faker


def faker(request, name):
   
    fake = Faker('ko_KR')
    job = fake.job()

    context = {
        'name':name,
        'job':job

    }
    return render(request, 'faker.html', context)
```



faker.html

```html
<h1>내 이름은 {{name}}</h1>
<h1>내직업은 {{job}}</h1>
```







for문 if문

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
    path('', views.index),
    path('dtl/', views.dtl),
    
    
]

```





views.py

```python
from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
from faker import Faker
from datetime import datetime

# Create your views here.

def dtl(request):
    foods = ["짜장면","탕수육","짬뽕","양장피","군만두","고추잡채","볶음밥"]
    my_sentence = 'life is short, you need pythin'
    messages = ['apple', 'banana', 'cucumber','mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        "foods":foods,
        "my_sentence":my_sentence,
        "messages":messages,
        "timenow":datetimenow,
        "empty_list":empty_list
    }

    return render(request, 'dtl.html',context)
```





dtl.html

```html
<!-- templates/dtl.html -->
<h3>1. 반복문</h3>
{% for f in foods %}
    <p>{{f}}</p>
{% endfor %}
<hr>
{% for f in foods %}
    <p>{{forloop.counter}} {{ f }}</p>
{% endfor %}
<hr>


{% for user in empty_list %}
    <p>{{ user }} 입니다.</p>
{% empty %}
    <p>현재 가입한 유저가 없습니다.</p>
{% endfor %}
<hr>

<h3>2.조건문</h3>
{% if '짜장면' in foods %}
    <p>짜장면엔 단무지 최고</p>

{% endif %}
<hr>
{% for f in foods %}
    {{ forloop.counter }}번쨰 ..
    {% if forloop.first %}
        <p>짜장면 + 고추가루</p>
    {% else %}
        <p>{{ f }}</p>
    {% endif %}
{% endfor %}

<hr>

<h3>3. lorem ipsum</h3>
{% lorem %}
<hr>
{% lorem 3 w %}
<hr>
{% lorem 2 p %}
<hr>

<h3>4. length filter 활용</h3>
{% for message in messages %}
    {% if message|length > 5 %}
        <p>글씨가 너무 길어요.</p>
    {% else %}
        <p>{{message }}, {{ message|length }}</p>
    {% endif %}
{% endfor %}

<hr>

<h3>5. 글자수 제한(truncate)</h3>
<p>{{ my_sentence }}</p>
<p>{{ my_sentence|truncatewords:3 }} 단어 단위로 제한</p>
<p>{{ my_sentence|truncatechars:5 }} 글자 단위로 제한</p>
<p>{{ my_sentence|truncatechars:15 }} 글자 단위로 제한(15번째 부터)</p>
<hr>
<h3>6. 글자 관련 필터</h3>
<p>{{ 'abc'|length }}</p>
<p>{{ 'ABC'|lower }}</p>    
<p>{{ my_sentence|title }}</p>
<p>{{ foods|random }}</p>
<hr>


<h3>7. 연산</h3>
<p>{{ 4|add:6 }}</p>


<h3>8. 날짜표현</h3>
{{ timenow }} <br>
{% now "DATEIME_FORMAT" %} <br>
{% now "SHORT_DATETIME_FORMAT" %} <br>
{% now "DATE_FORMAT" %} <br>
{% now "SHORT_DATE_FORMAT%} <br>
<hr>
{% now "Y년 m월 d일 (D) h:i"%}
<hr>
{% now "Y" as current_year %}
Copyright {{ current_year }}
<hr>
{{ timenow|date:"SHORT_DATE_FORMAT" }}
<hr>
<h3>9. 하이퍼링크 </h3>
{{ 'google.com'|urlize }}



```



### birth_day

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
    path('', views.index),
    path('birth', views.birth),
    
    
]

```





view.py

```python
from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
from faker import Faker
from datetime import datetime

# Create your views here.

def birth(request):
    today = datetime.now()

    if today.month == 6 and today.date ==12:
        res = True
    else:
        res = False

    birth = datetime(today.year+1, 7, 22)

    d_day = abs((today-birth).days)


    context = {
        'result':res,
        'd_day':d_day
    }

    return render(request, 'birth.html', context)
```



birth.html

```html
{% if res %}
<h1>네</h1>

{% else %}
<h2>아니오</h2>
{% endif%}
<h2>{{d_day}} 남았습니다.</h2>



```

