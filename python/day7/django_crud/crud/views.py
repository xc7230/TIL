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

