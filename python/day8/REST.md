# REST

Roy Fielding 논문으로 아키텍쳐 발표

- http 설계의 우수성에 비해 제대로 활용하고 있지 않아 발표함



HTTP

- Request/ Response 로 서버와 클라이언트간에 Http로 통신

웹 서버는 웹 리소스를 관리하고 제공을 함.

1. 미디어 타입 : 수천가지 데이터 타입이 존재

   MIME

   html : text/html

   jpeg : image/jpeg

   ASCII : text/plain

2. URI (URL + URN)

   URL : 리소스 위치 (스킵://서버위치/경로) 스킵 : 리소스에 접근하기위한 프로 

   URN : 위치에 독립적임.

REST의 구성

자원 - URL

행위 - HTTP Method

표현



REST 디자인 가이드

'/'는 계층 관계를 나타나는데 사용

'_'대신 '-'를 활용

정보의 자원을 표현해야함.



GET /boards/show/1 show라는 행위가 있기떄문에 REST하지 않음.

GET /boards/1



GET/boards/create

POST /boards



GET /boards/1/update

GET /boards/1/delete (REST X)

DELETE / boards/1

POST/ boards/1/delete



Django 에서는 Http method 를 GET/POST

/boards/new

데이터를 생성하기위한 폼을 불러오는거기 때문에 GET

/boards/create

데이터를 생성하기때문에 POST

GET /boards/new

POST/boards/new



request.GET

request.POST

request.mr





## 실습

### subway

models.py

```python
from django.db import models

# Create your models here.

class Subway(models.Model):
    title = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    menu = models.CharField(max_length=20)
    bread = models.CharField(max_length=10)
    vegetalbe = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    drink = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}. {self.name} : {self.menu}'
```









#### urls.py

```python
from django.urls import path
from . import views

app_name = "subway"

urlpatterns = [
    # name 을 설정하면 url 관리가 수월하다.
    # python 파일에서는 'app_name:설정name'
    # template 에서는 {% url 'app_name:설정name' %} 
    # url이 바뀌어도 일일히 찾아서 바꿀 필요가 없다.
    path('', views.index, name='index'),
    path('new_order/', views.new_order, name='new_order'),
    # REST 이용으로 update부분 필요 없음. POST new/ 이용.
    # path('create/', views.create, name='create'),
    # redirect('app_name:설정name', 넘길 id)
    # {% url 'app_name:설정name' 넘길id %}
    path('detail/<int:id>/', views.detail, name='detail'),
    path('edit/<int:id>/', views.edit, name='edit'),
    # REST 이용으로 update부분 필요 없음. POST edit/id 이용.
    # path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
```





#### views.py

```python
from django.shortcuts import render, redirect
from .models import Subway

# Create your views here.
def index(request):
    subways = Subway.objects.all()

    context = {
        'subways': subways
    }
    return render(request, 'subway/index.html', context)

def new_order(request):

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        menu = request.POST.get('menu')
        bread = request.POST.get('bread')
        sauce = request.POST.get('sauce')
        veg = request.POST.getlist('veg')
        drink = request.POST.get('drink')

        subway = Subway()
        subway.name = name
        subway.address = address
        subway.phone = phone
        subway.menu = menu
        subway.bread = bread
        subway.sauce = sauce
        subway.vegetable = veg
        subway.drink = drink

        subway.save()

        return redirect('subway:index')
    else:
        return render(request, 'subway/new_order.html')

# def create(request):
#     name = request.POST.get('name')
#     address = request.POST.get('address')
#     phone = request.POST.get('phone')
#     menu = request.POST.get('menu')
#     bread = request.POST.get('bread')
#     sauce = request.POST.get('sauce')
#     veg = request.POST.getlist('veg')
#     drink = request.POST.get('drink')

#     subway = Subway()
#     subway.name = name
#     subway.address = address
#     subway.phone = phone
#     subway.menu = menu
#     subway.bread = bread
#     subway.sauce = sauce
#     subway.vegetable = veg
#     subway.drink = drink

#     subway.save()

#     return redirect('subway:index')

def detail(request, id):
    sub = Subway.objects.get(id=id)

    context = {
        "sub": sub
    }
    return render(request, 'subway/detail.html', context)

def edit(request, id):
    subway = Subway.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        menu = request.POST.get('menu')
        bread = request.POST.get('bread')
        sauce = request.POST.get('sauce')
        veg = request.POST.getlist('veg')
        drink = request.POST.get('drink')

        subway = Subway()
        subway.name = name
        subway.address = address
        subway.phone = phone
        subway.menu = menu
        subway.bread = bread
        subway.sauce = sauce
        subway.vegetable = veg
        subway.drink = drink

        subway.save()

        return redirect('subway:detail', subway.id)
    else:
        context = {
            'subway': subway
        }
        return render(request, 'subway/update.html', context)

# def update(request, id):
#     subway = Subway.objects.get(id=id)

#     name = request.POST.get('name')
#     address = request.POST.get('address')
#     phone = request.POST.get('phone')
#     menu = request.POST.get('menu')
#     bread = request.POST.get('bread')
#     sauce = request.POST.get('sauce')
#     veg = request.POST.getlist('veg')
#     drink = request.POST.get('drink')

#     subway = Subway()
#     subway.name = name
#     subway.address = address
#     subway.phone = phone
#     subway.menu = menu
#     subway.bread = bread
#     subway.sauce = sauce
#     subway.vegetable = veg
#     subway.drink = drink

#     subway.save()

#     return redirect('subway:detail', subway.id)


def delete(request, id):
    if request.method == "POST":
        sub = Subway.objects.get(id=id)
        sub.delete()
        return redirect('subway:index')    
    else:
        return redirect('subway:detail', id) 
```





#### detail.html

```html
{% extends 'base.html' %}
{% block body %}
    이름 : {{ sub.name }} <br>
    주소 : {{ sub.address }} <br>
    번호 : {{ sub.phone }} <br>
    메뉴 : {{ sub.menu }} <br>
    주문 사항:
    {{ sub.bread }} / {{ sub.sauce }} <br>
    {{ sub.vegetable }} / {{ sub.drink }} <br>

    <a href="{% url 'subway:edit' sub.id %}">수정하기</a>
    <!-- <a href="{#% url 'subway:delete' sub.id %}">삭제하기</a> -->
    <form action='{% url "subway:delete" sub.id %}' method='POST'>
        {% csrf_token %}
        <input type='submit' value="삭제하기">
    </form>
    {% endblock %}
```





#### index.html

```html
{% extends 'base.html' %}
{% block body %}
    <h1>Index page</h1>

    <ul>
        {% for sub in subways%}
        <li><a href="{% url 'subway:detail' sub.id %}">{{ sub.name }} : {{ sub.menu }}_{{ sub.updated_at }}</a></li>
        {% empty %}
        <h1>주문 내역이 없습니다.</h1>
        {% endfor %}
    </ul>
{% endblock %}
```



#### new_order.html

```html
{% extends 'base.html' %}
{% block body %}
    <form action='{% url "subway:new_order" %}' method='POST'>
        {% csrf_token %}
        <div>
            이름: <input type="text" name="name">
        </div>
        <hr>
        <div>
            주소: <input type="text" name="address">
        </div>
        <hr>
        <div>
            번호: <input type="tel" name="phone">
        </div>
        <hr>
        <div>
            메뉴:
            <select name="menu">
                <option value="치킨 데리야키">치킨 데리야키</option>
                <option value="이탈리안 BMT">이탈리안 BMT</option>
                <option value="로스트 치킨">로스트 치킨</option>
                <option value="서브웨이 클럽">서브웨이 클럽</option>
                <option value="참치">참치</option>
            </select>
        </div>
        <hr>
        <div>
            빵:
            <input type="radio" name="bread" value="위트">위트
            <input type="radio" name="bread" value="허니오트">허니오트
            <input type="radio" name="bread" value="파마산 오레가노">파마산 오레가노
            <input type="radio" name="bread" value="플랫 브레드">플랫 브레드
        </div>
        <hr>
        <div>
            소스:
            <input type="checkbox" name="sauce" value="스윗 언년">스위트 언년
            <input type="checkbox" name="sauce" value="허니 머스탇">허니 머스탇
            <input type="checkbox" name="sauce" value="스윗 칄리">스윗 칄리
            <input type="checkbox" name="sauce" value="사우전 아일랜">사우전 아일랜
            <input type="checkbox" name="sauce" value="핫 칄리">핫 칄리
        </div>
        <hr>
        <div>
            채소:
            <input type="checkbox" name="veg" value="양배추">양배추
            <input type="checkbox" name="veg" value="토마토">토마토
            <input type="checkbox" name="veg" value="오이">오이
            <input type="checkbox" name="veg" value="피망">피망
            <input type="checkbox" name="veg" value="양파">양파
            <input type="checkbox" name="veg" value="올리브">올리브
        </div>
        <hr>
        <div>
            음료
            <input type="radio" name="drink" value="사이다">사이다
            <input type="radio" name="drink" value="콜라">콜라
            <input type="radio" name="drink" value="환타">환타
        </div>
        <input type='submit' value="주문하기">
    </form>
{% endblock %}
```





#### update.html

```html
{% extends 'base.html' %}
{% block body %}
    <form action='{% url "subway:edit" subway.id %}' method='POST'>
        {% csrf_token %}
        <div>
            이름: <input type="text" name="name" value="{{ subway.name }}">
        </div>
        <hr>
        <div>
            주소: <input type="text" name="address" value="{{ subway.address }}">
        </div>
        <hr>
        <div>
            번호: <input type="tel" name="phone" value="{{ subway.phone }}">
        </div>
        <hr>
        <div>
            메뉴:
            <select name="menu">
                <option value="치킨 데리야키">치킨 데리야키</option>
                <option value="이탈리안 BMT">이탈리안 BMT</option>
                <option value="로스트 치킨">로스트 치킨</option>
                <option value="서브웨이 클럽">서브웨이 클럽</option>
                <option value="참치">참치</option>
            </select>
        </div>
        <hr>
        <div>
            빵:
            <input type="radio" name="bread" value="위트">위트
            <input type="radio" name="bread" value="허니오트">허니오트
            <input type="radio" name="bread" value="파마산 오레가노">파마산 오레가노
            <input type="radio" name="bread" value="플랫 브레드">플랫 브레드
        </div>
        <hr>
        <div>
            소스:
            <input type="checkbox" name="sauce" value="스윗 언년">스위트 언년
            <input type="checkbox" name="sauce" value="허니 머스탇">허니 머스탇
            <input type="checkbox" name="sauce" value="스윗 칄리">스윗 칄리
            <input type="checkbox" name="sauce" value="사우전 아일랜">사우전 아일랜
            <input type="checkbox" name="sauce" value="핫 칄리">핫 칄리
        </div>
        <hr>
        <div>
            채소:
            <input type="checkbox" name="veg" value="양배추">양배추
            <input type="checkbox" name="veg" value="토마토">토마토
            <input type="checkbox" name="veg" value="오이">오이
            <input type="checkbox" name="veg" value="피망">피망
            <input type="checkbox" name="veg" value="양파">양파
            <input type="checkbox" name="veg" value="올리브">올리브
        </div>
        <hr>
        <div>
            음료
            <input type="radio" name="drink" value="사이다">사이다
            <input type="radio" name="drink" value="콜라">콜라
            <input type="radio" name="drink" value="환타">환타
        </div>
        <input type='submit' value="주문하기">
    </form>
{% endblock %}
```







# 1대 N관계



python manage.py shell_plus





1대 1관계

OneToOneField



N:M관계

ManyToManyField



## 실습

### crud

#### install

```
pip install django-extensions
#settings에 INSTALLED_APPS 맨뒤에 'django_extensions', 추가
python manage.py shell_plus

```









#### models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} > {self.title}'


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    # ForeignKey(어떤테이블을 참조, 그 테이블이 삭제될때 어떻게 할지)
    # models.CASCADE : 부모테이블이 삭제시 같이 삭제하는 옵션
    # models.PROTECT : 부모테이블이 삭제 될때 오류 발생.
    # models.SET_NULL: 삭제 되었을때 부모 참고 값에 NULL값으로 채움. 단 NOT NULL 불가능.
    # models.SET_DEFAULT: 삭제 되었을때 설정된 default 값으로 설정. default 옵션 설정 필요!
    # models.SET() : 특정 함수를 호출. ()안에 함수명을 넣어주면 됨.
    # models.DO_NOTHING : 암것도 안함.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#     article = models.ManyToManyField(Article, through="ArticleComment")


# class ArticleComment(models.Model):
#     article = models.ForeignKey(Article)
#     comment = models.ForeignKey(Comment)
```







#### urls.py

```python
from django.urls import path
from . import views

app_name = "crud"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    # path('create/', views.create, name="create"),
    path('<int:art_id>/', views.detail, name="detail"),
    path('<int:art_id>/update/', views.update, name="update"),
    # path('<int:id>/save/', views.arti_save, name="save"),
    path('<int:art_id>/delete/', views.delete, name="delete"),
    path('<int:art_id>/comment/', views.comment, name="comment"),
    path('<int:art_id>/comment/<int:com_id>/edit/', views.comment_edit, name="comment_edit"),
    path('<int:art_id>/comment/<int:com_id>/del/', views.comment_del, name="comment_del"),
]
```



#### views.py

```python
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Article, Comment

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'crud/index.html', context)

def new(request):
    # print(f'new : {request.method}')
    # return render(request, 'crud/new.html') # 기존 new 함수
    
    # REST 하게 바꿨을때 폼이 새로 생성되는 부분.
    if request.method == "POST":
        article = Article(title=request.POST.get('title'), content=request.POST.get('content'))
        article.save()
        return redirect('crud:index')
    else:
    # 폼 html 을 불러오는 부분.
        return render(request, 'crud/new.html')

# RESTful 하게 수정 (POST /crud/new)
# def create(request):
#     print(f'create : {request.method}')
#     article = Article(title=request.POST.get('title'), content=request.POST.get('content'))
#     article.save()

#     return redirect('crud:index')

def detail(request, art_id):
    art = Article.objects.get(id=art_id)
    com = art.comment_set.all()
    comtext = {
        'art':art,
        'comment':com
    }

    return render(request, 'crud/detail.html', comtext)

def update(request, art_id):
    art = Article.objects.get(id=art_id)
    # print(f'update : {request.method}') # request method 확인
    if request.method == "POST":
        art.title = request.POST.get('title')
        art.content = request.POST.get('content')
        art.save()
        return redirect('crud:detail', art.id)
    else:
        return render(request, 'crud/update.html', {'art':art})

# RESTful 하게 수정 (POST crud/update/id)
# def arti_save(request, id):
#     art = Article.objects.get(id=id)
#     print(f'save : {request.method}')

#     art.title = request.POST.get('title')
#     art.content = request.POST.get('content')

#     art.save()
#     return redirect('crud:detail', art.id)

#---------------------------------------------
# delete 부분은 데이터를 삭제하는 동작이기에 GET으로 동작되어서는 안됨.
# GET으로 동작할 경우 브라우저 URL로도 데이터 삭제가 가능하게됨.
# DELETE method가 장고에서 지원이 안되기에 POST 방식으로 값을 넘겨 받음.
def delete(request, art_id):
    art = Article.objects.get(id=art_id)
    if request.method == "POST":
        art.delete()
        return redirect('crud:index')
    else:
        # GET인경우 상세정보 페이지
        return redirect('crud:detail', art_id)


# POST art_id/comment
def comment(request, art_id):
    article = Article.objects.get(id=art_id)

    if request.method == "POST":
        comment = request.POST.get('comment')

        com = Comment()
        com.comment = comment
        com.article = article
        com.save()

        return redirect('crud:detail', art_id)

def comment_edit(request, art_id, com_id):
    com = Comment.objects.get(id=com_id)


    if request.method == "POST":
        text = request.POST.get('comment')
        com.comment = text
        com.save()
        return redirect('crud:detail', art_id)
    else:
        context = {
            'comment':com
        }
        return render(request, 'crud/comment_edit.html', context)

def comment_del(request, art_id, com_id):
    com = Comment.objects.get(id=com_id)

    if request.method == "POST":
        com.delete()
       
    return redirect('crud:detail', art_id)

```



#### detail.html

```html
{% extends 'base.html' %}
{% block body %}
제목 : {{ art.title }} <br>
내용 : {{ art.content }} <br>

<a href="{% url 'crud:update' art.id %}">수정하기</a>
<form action='{% url "crud:delete" art.id %}' method='POST'>
    {% csrf_token %}
    <input type='submit' value="삭제하기">
</form>

<hr><br>

<form action='{% url "crud:comment" art.id %}' method='POST'> 
    {% csrf_token %}
    댓글달기: <input type="text" name="comment" >
    <input type='submit'>
</form>
<hr><br>
댓글갯수: {{comment|length}} 
<!-- / {#{art.comment_set.all|length}} / {#{comments.count}} -->

<hr><br>
<ul>
    {% for com in art.comment_set.all %}
    <li>
        {{com.comment}}
        <a href="{% url 'crud:comment_edit' art.id com.id %}"> 수정하기</a>
        <form action='{% url "crud:comment_del" art.id com.id %}' method='POST'> 
            {% csrf_token %}
            <input type='submit' value="삭제">
        </form>
    </li>
    {% empty %}
        <h2>등록된 댓글이 없어요~</h2>
    {% endfor %}
</ul>
{% endblock %}
```



#### comment_edit.html

```html
{% extends 'base.html'%}
{% block body %}
    <form action='' method='POST'> 
        {% csrf_token %}
        댓글 : <input type="text" name="comment" value="{{comment.comment}}">
        <input type='submit' value="댓글수정">
    </form>
{% endblock%}
```



#### index.html

```html
{% extends 'base.html' %}
{% block body %}
<h1>Article List</h1>
<ol>
    {% for art in articles %}
    <li><a href="{% url 'crud:detail' art.id %}">{{art.title}}</a></li>
    {% endfor %}
</ol>
{% endblock %}
```



#### new.html

```html
{% extends 'base.html' %}
{% block body %}
    <form action='{% url "crud:new" %}' method='POST'>
        {% csrf_token %}
        <input type="text" name="title"><br>
        <textarea name="content" cols="30" rows="10"></textarea><br>
        <input type='submit'>
    </form>
{% endblock %}
```



#### update.html

```html
{% extends 'base.html' %}
{% block body %}
    <form action='{% url "crud:update" art.id %}' method='POST'>
        {% csrf_token %}
        <input type="text" name="title" value="{{ art.title }}"> <br>
        <textarea name="content"cols="30" rows="10">{{ art.content }}</textarea> <br>
        <input type='submit'>
    </form>
{% endblock %}
```

