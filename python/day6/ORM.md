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





