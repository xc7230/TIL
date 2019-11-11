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

