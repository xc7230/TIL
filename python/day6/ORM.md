virtualenv venv

source venv/Scripts/activate

django-admin startproject config .

python manage.py startapp boards

python manage.py runserver



# ORM

MTV

모델(모델)/템플릿(뷰)/뷰(컨트롤러)

쿼리 : 데이터를 질의 하는 조회하는 명령어

db : 체계화된 데이터의 모임

스키마 : 디비 자료의 구조, 표현방법, 관계 정의한 구조

테이블

- 필드 : 컬럼
- 레코드 : 데이터



장점

sql을 몰라도 사용이 가능하다.

코드의 가독성이 증가한다.

객체 지향적인 접근으로 생산성이 증가한다.

매핑 정보가 명확하여 ERD를 보는것에 대한 의존도를 낮출 수 있다.

ORM은 독립적으로 작성되어 있고, 해당객체들을 재활용 할 수 있다.

그렇기 때문에 모델에서 가공된 데이터를 컨트롤러(views.py)에 의해 뷰(templates)와 합쳐지는 형태로 디자인 패턴을 견고하게 다지는데 유리



단점

모든것을 ORM으로 구현하기 어려움

사용은 편하나 설계에는 신중해야함

구조가 복잡해지면 난이도가 상승 할 수 있다.







python manage.py shell

```
>>> class Person:
...     name = "사람의 고유한 이름"
...     age = "출생 이후로 부터 삶을 마감할 때까지의 기간"
...     def greetin(self):
...             print(f'{self.name}이 인사합니다') 
...     def eating(self):
...             print(f'{self.name}이 밥을 먹고 있습니다.') 
...     def aging(self):
...             print(f'P{self.name}은 현재 {self.age}살이지만 점점 나이를 더 먹겠죠.')
... 
>>> justin = Person()
>>> print(justin.name)
사람의 고유한 이름
>>> justin.age = 19
>>> print(justin.age)
19
>>> print(Person.name)
사람의 고유한 이름
>>> print(Person.age)
출생 이후로 부터 삶을 마감할 때까지의 기간
>>> print(justin.age)
19
>>> justin.name = "수능보는 justin"
>>> justin.greetin()
수능보는 justin이 인사합니다
>>> justin.eating()
수능보는 justin이 밥을 먹고 있습니다.
>>> justin.aging()
P수능보는 justin은 현재 19살이지만 점점 나이를 더 먹겠죠.
```



## Model

모델은 단일 데이터에 대한 정보를 가지고 있어요. 필수적인 필드(컬럼)과 데이터(레코드)에 대한 정보를 포함 각각 모델은 단일 DB 테이블과 매핑

사용자가 저장하는 데이터들의 필수적인 필드(컬럼) 동작을 포함



models.py

```python
from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField() #db에서 글자수 제한이 안된다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



명세서

```shell
$ python manage.py makemigrations
Migrations for 'boards':
  boards\migrations\0001_initial.py
    - Create model Board
(venv)
```





변경순서

1. models.py 를 작성
2. makemigrations : migration 파일(명세서) 생성
3. migrate : 실제 적용되는 부분

데이터 객체를 만드는 3가지 방법

1. 첫번째

   board = Board()

   board.title = "값"

   board.save()

2. 두번째 방식

   board = Board(title="값", content="값")

   board.save()

3. 세번째 방식

   board = Board.objects.create(title="값",content="값")

```shell
python manage.py showmigrations
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
boards
 [ ] 0001_initial
 [ ] 0002_board_updated_at
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
sessions
 [ ] 0001_initial
(venv) 
```





```shell
python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, boards, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying boards.0001_initial... OK
  Applying boards.0002_board_updated_at... OK
  Applying sessions.0001_initial... OK
(venv) 
```





```shell
vim ~/.bashrc

alias sqlite="c:/sqlite/sqlite3.exe" #입력

source ~/.bashrc

sqlite db.sqlite3
SQLite version 3.30.1 2019-10-10 20:19:45
Enter ".help" for usage hints.
sqlite> .tables
auth_group                  boards_board
auth_group_permissions      django_admin_log
auth_permission             django_content_type
auth_user                   django_migrations
auth_user_groups            django_session
auth_user_user_permissions

sqlite> .schema boards_board
CREATE TABLE IF NOT EXISTS "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
```







```shell
python manage.py shell

from boards.models import Board
>>> Board.objects.all()
<QuerySet []>

<QuerySet []>
>>> board = Board()
>>> board.title = "first" 
>>> board.content = "django !!!!!"
>>> board.save()
>>> board
<Board: Board object (1)>

>>> board = Board(title="second", content="django")
>>> board.save()
>>> board
<Board: Board object (2)>

>>> Board.objects.create(title="third", content="django3")
<Board: Board object (3)>

>>> Board.objects.all()
<QuerySet [<Board: Board object (1)>, <Board: Board object (2)>, <Board: Board object (3)>]>



```









admin 커스텀마이즈

admin 계정만들기

```
python manage.py createsuperuser
```





admin.py

```python
from django.contrib import admin
from .models import Board

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    fields = ['content', 'title']
    list_display = ["title", "updated_at","created_at"]
    list_filter = ["updated_at"]
    search_fields = ["title", "content"]

admin.site.register(Board, BoardAdmin)
```





실습) 서브웨이 폼에서 받은 데이터를 DB에 넣어보자

1. 서브웨이 폼에서 받은 데이터를 DB에 넣어보자.
2. DB 에서 데이터를 받아와 보여줘 보자.



1. 서브웨이 폼에 어떤 데이터가 저장되는지

   그 데이터를 models.py정의

   db에 데이터 생성(migrate)

   데이터를 받아서 저장하는 부분을 완성

2. DB에서 데이터 전체를 불러와 페이지에 간결하게 뿌려보자
3. URL에서 ID값을 받아와서 그 ID의 정보만 간결하게 뿌려보자







models.py

```python
from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField() #db에서 글자수 제한이 안된다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} : {self.title}'


class Subway(models.Model):
    title = models.CharField(max_length=10)
    name = models.TextField()
    date = models.TextField()
    sandwitch = models.TextField()
    size = models.TextField()
    bread = models.TextField()
    source = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} : 이름은:{self.name}, 샌드위치는:{self.sandwitch}, 사이즈는:{self.size}, 소스는:{self.source}'
```



```
python manage.py makemigrations
python manage.py migrate

```





urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('menu/', views.menu),
    path('subway/', views.subway),

]
```





views.py

```python
from django.shortcuts import render
from boards.models import Subway

# Create your views here.

def index(request):
    return render(request, "boards/index.html")


def menu(request):


    return render(request,'boards/menu.html')


def subway(request):
    name = request.POST.get("name")
    date = request.POST.get("date")
    sandwitch = request.POST.get("sandwitch")
    size = request.POST.get("size")
    bread = request.POST.get("bread")
    source = request.POST.getlist("source")

    Subway.objects.create(name=name,date=date,sandwitch=sandwitch,size=size,bread=bread,source=source)

    result = Subway.objects.all()

    context = {
        'name':name,
        'date':date,
        'sandwitch':sandwitch,
        'size':size,
        'bread':bread,
        'source':source,
        'result':result
    }


    return render(request, 'boards/subway.html', context)

def result_sub(request, number):
    result = Subway.objects.filter(id=number)

    context = {
        'result':result
    }
    return render(request, 'boards/result_sub.html', context)

```







menu.html

```html
{% extends 'base.html' %}
{% block title %}
subway-menu
{% endblock%}




{% block content %}
    <h1>FORM</h1>
   주문서를 작성해 주십시오 <br>
    <form action="/board/subway/" method="POST">
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
{% endblock%}
```



subway.html

```html
{% extends 'base.html' %}
{% block content %}

<h1>{{name}}님이 주문 하신 결과는</h1>

<p>{{sandwitch}} / {{size}} 크기로</p>
<p>{{bread}}에 {{source}}입니다</p>
<p>날짜는 {{date}} 입니다.</p>

{%for i in result%}
    <li>{{ i }}</li>
{% endfor %}


{% endblock%}

```



result_sub.html

```python
{% extends 'base.html' %}
{% block content %}


{%for i in result%}
    <li>{{ i }}</li>
{% endfor %}


{% endblock%}

```

