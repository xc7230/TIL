static file 

위치가 고정

웹 서비스에서 사용할려고 미리 준비한 파일 변경없이 서비스시 제공하는 파일 위치가 고정이 되어있음.

```html
{% static %}으로 불러와서 사용.

{% load static %}상단에 기재해줘야함. 필수

app_name/static/app_name(templates와 같음)

boards/static/boards/images/a.jpeg

{% load static %}
<img src = "{% static 'boards/images/a.jpeg '%}">
<!-- setting.py에서 static 추가 경로를 설정 할 수 있음. --!>


```

STATIC_URL : 웹에서 사용할 정적 파일의 최상위 URL(실제 파일이 위치한 디렉토리가 아님.)

튜플이나 리스트 형식으로 지정

STATICFILES_DIR : 

```python
STATICFILES_DIR = [
    "/assets/image/*"
    os.path.join(BASE_DIR, 'assets','image'),

]
```



STATIC_ROOT

debug=True 일떄는 동작하지 않음.배포용

```
python manage.py collectstatic
```







```python
#python manage.py collectstatic : 프로젝트안에 모든 static file을 모아줌.
#해당 경로에 위치한 모든 파일을 웹 서버가 직접 제공하기 위해 존재
```







media file

사용자 한테서 업로드 받는 이미지도 스태틱한 소스 



Null : DB에서 유효성 검사

Blank : 유효성 검사를 하는데 폼에서 함.

 input tag 옵션에 required



Null을 허용하고 싶을땐(models에 들어감)

Null=False, Blank=False

null = True, blank = false

charfield, textfield

blank = True

booleanfield, Nullbooleanfield

Field.null

Null=True 컬럼을 비워둘수가 있음.(default=false)

db에서 유효성검사를 함.



Field.blank

blank=True 빈 값으로 저장을 허용(default = false)

form에서 유효성 검사를 함.

''빈값이 들어갈수있음



Field.default

디폴트값 설정.





form태그에서 enctype

application/x-www-form-urlencoded (기본값)

공백은 + 특문도 ascii hex 변환

multipart/form-data : 파일 업로드에 필요. POST요청을 해야함

text/plain : 공백은 +로 변환 특문 X



MEDIA FILE

업로드 받은 이미지가 나타나게 설정해 봅시다.

MEDIA_ROOT

- 업로드가 될때 저장시키는 걸로
- staticfiles_dirs 비슷한

MEDIA_URL

- static_url 비슷. 파일의 주소를 만들어주는 역할
- 실제 파일이 위치한 디렉토리가 아님
- /가 필수이고 문자열로 설정필요.
- "/media/"

url



Image Resizing 하기

1. Pillow : PIL 프로젝트에서 fork된 라이브러리

   - 이미지 파일형식 지원
   - 다양한 이미지를 처리
   - ImageField 생성할때 필수

2. pilkit : pillow를 쉽게 쓸 수 있도록 도와주는 패키지, 다양한 프로세서를 지원 (pip install pilkit)

   - Thumbnail
   - Resize
   - Crop

3. django-imagekit : 이미지 썸네일 django app(실제로 처리할때는 pilkit)  (pip install django-imagekit)

   - 이미지 썸네일 헬퍼 장고앱
   - settings.py 에 등록해서 사용.(INSTALLED_APP)

   PNG와 JPEG의 차이

   - PNG: 스크린샷, 단순한 그림, 아이콘, 8bit 색상이 적은 이미지
   - JPEG: 자연적인 이미지, 다양한 색상의 이미지

processor

- ResizeToFill : 지정한 사이즈를 맞추고 넘치는 부분을 잘라냄.
- ResizeTofit : 지정한 사이즈를 맞추고 남는 부분은 빈공간으로 둠.



favicon

faverite + icon

favicon 은 link tag로 설정

link 

- type : 연결 문서의 MIME 유형
- rel : 현재 문서와 연결되는 문서의 관계 표시
  - stylesheet
  - alternate
  - author
  - help
  - search



favicon-generator.org

파일을 받아서 static 경로 저장

link rel="shorcut icon" href={static "파비콘 경로"} type="image/x-icon"

link rel="icon" href={static "파비콘 경로"} type="image/x-icon"



실습

settings.py

```python
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nt91nn=0th-1z&55nasyp)divj)=$w)y97qa@o6pz*cq6(otvj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'boards',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'imagekit',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "config", "templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets", "images"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "sf")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")



```



config.urls.py

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('boards.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#첫번째 인자 : 어떤 URL을 정적으로 추가할건지
#두번째 인자 : 실제 미디어파일은 어디에 있는지
#   decument_root에 미디어 파일 경로를 전달해주면됨.
```





base.html

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="shortcut icon" href="{% static 'boards/favicon/favicon.ico'%}" type="image/x-icon">
    <link rel="icon" href="{% static 'boards/favicon/favicon.ico'%}" type="image/x-icon">
    <title>Document</title>
</head>
<body>
    {% block body %}
    {% endblock %}
    
</body>
</html>
```



models.py

```python
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, Thumbnail

# Create your models here.
# Board를 새로 생성할때 save() 가 호출되고 나서 pk가 생성
def board_img_path(instance, filename):
    return f'boards/user_{instance.user.pk}번글/{filename}'


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    # #ResizeToFill Ver.1
    # image = ProcessedImageField(
    #     upload_to = "boards/images_rtf" ,
    #     processors= [ResizeToFill(600, 500)],
    #     format = "JPEG",
    #     options = {
    #         'quality':85

    #     }
    # )
    
    # #Thumbnail Ver.1 (원본 x, 썸네일 o)
    # image = ProcessedImageField(
    #     upload_to = "boards/thumbnail" ,
    #     processors= [ResizeToFill(100, 100)],
    #     format = "JPEG",
    #     options = {
    #         'quality':90

    #     }
    # )


    #Thumbnail 원본은 저장하고 썸네일은 캐쉬형태로 Ver.2
    #원본 저장 o  thumbnail은 캐시형태로 ~
    image = models.ImageField(blank=True, upload_to=board_img_path)
    image_thumbnail = ImageSpecField(
        source = 'image',
        processors = [Thumbnail(250,250)],
        format= "JPEG",
        options = {
             'quality':90

        }

    )

    
    
    # image = models.ImageField(blank=True)
    # image_thumb = ImageSpecField(
    #     source = 'image',
    #     processors = [Thumbnail(200, 300)],
    #     format = "JPEG",
    #     options = {
    #         'quality':90
    #     }
    # )

```





boards.urls.py

```python
from django.urls import path
from . import views

app_name = "boards"

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('<int:b_id>/', views.detail, name="detail"),
    path('<int:b_id>/edit', views.edit, name="edit"),

]
```





views.py

```python
from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()
    
    context = {
        "boards":boards
    }
    
    return render(request, 'boards/index.html', context)

def new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        board = Board(title=title, content=content, image=image)
        board.save()

        return redirect('boards:index')
    else:
        return render(request, 'boards/new.html')


def detail(request, b_id):
    board = Board.objects.get(id=b_id)

    context = {
        "board":board
    }
    return render(request, 'boards/detail.html', context)


def edit(request, b_id):
        board = Board.objects.get(id=b_id)

        if request.method == "POST":
            board.title = request.POST.get('title')
            board.content = request.POST.get('content')
            img = request.FILES.get('image')
            if img is not None:
                board.image = img
            board.save()
            return redirect('boards:detail', board.id)
        
        else:

            context = {
                "board":board
            }

            return render(request, 'boards/edit.html', context)

```



detail.html

```html
{% extends 'base.html'%}
{% load static %}
{% block body %}


<h2>detail</h2>

<div>
    TITLE : {{board.title}} <br>
    content : {{board.content}} <br>
    IMAGE: <br>

    {% if board.image %}
        <img src="{{board.image.url}}" alt="{{board.image.url}}">
        [<img src="{{board.image_thumbnail.url}}" alt="{{board.image_thumbnail}}">]
    {% else %}
        <img src="{static 'bob.jpg'}" alt="">
    {% endif %}

</div>
<a href="{% url 'boards:edit' board.id %}"> 수정하기</a>

{% endblock %}
```





edit.html

```html
{% extends 'base.html'%}
{% load static %}
{% block body %}

<h1>edit</h1>

<form action="{% url 'boards:edit' board.id %}" enctype="multipart/form-data" method="POST">
    {% csrf_token %}
    <input type="text" name="title" required value="{{board.title}}"><br>
    <input type="text" name="content" required value="{{board.content}}"><br>
    <input type="file" name="image" accept='image/*'>
    <hr>
    <input type="submit">
</form>

{% endblock %}
```





index.html

```html
{% extends 'base.html'%}
{% load static %}
{% block body %}

<h1>index page</h1>

<img src="{% static 'boards/images/peng.jpg' %}" alt="peng.jpg">
<img src="{% static 'bob.jpg' %}" alt="bob.jpg">
<hr><br><hr>

{% for board in boards %}
    <li><a href="{% url 'boards:detail' board.id%}"> {{board.title}}</a></li>

{% endfor %}
<hr><br><br>

<a href="{% url 'boards:new' %}"> 새로만들기 </a>
{% endblock %}
```





new.py

```python
{% extends 'base.html'%}
{% load static %}
{% block body %}

<h1>new</h1>

<form action="{% url 'boards:new' %}" enctype="multipart/form-data" method="POST">
    {% csrf_token %}
    <input type="text" name="title" required>
    <input type="text" name="content" required>
    <input type="file" name="image" accept='image/*'>
    <input type="submit">
</form>

{% endblock %}

```



pip install pillow

```python
from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)

```



