복습

ORM

sql을 몰라도 DB 활용할 수 있게

model

class

클래스 변수가 column 명

클래스 메소드로  __str__()재정의

- 데이터가 잘 저장됬는지 확인차.

makemigrations

​	장고에서 변경된 부분을 migrations 폴더 안에 0001_XXXX 같이 명세서를 자동 작성해준다.

​	혹시 오타면 마이그레이션 파일은 수정하지말고 models.py를 수정 장고에서 변경점을 못찾을 때는 새롭게 생성된 migration 파일 삭제



migrate

​	migration 파일을 바탕으로 DB에 테이블을 적용.

admin.py

​	DB 관리용 페이지

​	일반 사용자에게 보여지는 페이지는 아님.

​	fields : list, tuple 형식으로 수정할 항목이나 순서를 설정을 했음.

​		auto_now=True로 설정시, editable=False 로 자동 설정되서 fields에서 사용할 수 없음.

​	list_filter : bool, char, date, datetime, integer 속성만 필터링 가능





# CRUD

Create / Read / Update / Delete



서브젯

```html
{
	// Place your snippets for html here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }

	"post_form": {
		"prefix": "post_form",
		"body":[
			"<form action='' method='post'> ",
			"    {% csrf_token %}",
			"    <input type='submit'>",
			"</form>"

		],
		"description": "form tag"

	}

}
```







urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),   # crud/
    path('new/', views.new), # crud/new/
    path('create/', views.create),
    path('<int:pk>/article/', views.detail),
    path('<int:pk>/update/', views.update),
    path('<int:pk>/revise/', views.revise),
    path('<int:pk>/delete/', views.delete),
]
```





views.py

```python
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    #articles = Article.objects.all()[::-1]

    articles = Article.objects.order_by("-id")

    content = {
        "articles" : articles
   
    }
    return render(request, 'crud/index.html', content)

def new(request):
    return render(request, 'crud/new.html')

#form에서 데이터를 받아 DB에 저장하고 글 작성 성공메세지 작성
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    #DB에 저장시키자
    article = Article()
    article.title = title
    article.content = content
    article.save()

    return render(request, 'crud/create.html')
def detail(request, pk):
    
    article = Article.objects.get(pk=pk)

    context = {
        "article":article
    }
    return render(request, 'crud/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        "article":article
    }
    return render(request, 'crud/update.html', context)

def revise(request, pk):
    article = Article.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content

    article.save()

    return redirect(f'/crud/{article.id}/article/')

def delete(request,pk):
    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect('/crud/')


```



index.html

```html
{% extends 'base.html'%}

{% block body %}
<h1>Article List</h1>
<ul>
    {% for art in articles %}
    <li><a href="/crud/{{ art.pk }}/article/">{{art.title}}</a></li>
    {% endfor %}

</ul>

{% endblock%}
```





new.html

```html
{% extends 'base.html' %}

{% block body %}

    <form action='/crud/create/' method='post'> 
        {% csrf_token %}
        <label for="title">기사 제목</label>
        <input type="text" name="title" id="title">
        <textarea name="content"  cols="30" rows="5"></textarea>
        <input type='submit'>
        
    </form>

{% endblock %}
```





create.html

```html
{% extends 'base.html'%}
{% block body %}
글쓰기가 완료 되었습니다.
{% endblock%}
```



detail.html

```HTMl
{% extends 'base.html' %}
{% block body %}
    제목 : {{article.title}} <br>
    내용 : {{article.content}} <br>
    <a href="/crud/{{article.id}}/update/">수정하기</a>
    <a href="/crud/{{article.id}}/delete/">삭제하기</a>
{% endblock%}
```



update.html

```html
{% extends 'base.html'%}
{% block body %}
    <form action='/crud/{{article.id}}/revise/' method='post'> 
        {% csrf_token %}
        <input type="text" name="title" value="{{article.title}}"> <br>
        <textarea name="content" cols="30" rows="5">{{article.content}}</textarea> <br>
        <input type='submit'>
    </form>
{% endblock%}
```



