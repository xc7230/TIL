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

