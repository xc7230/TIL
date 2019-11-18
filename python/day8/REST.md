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





## 