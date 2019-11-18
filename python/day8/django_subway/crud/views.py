from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):

    articles = Article.objects.order_by('-id')

    content = {
        'articles':articles
    }

    return render(request, 'crud/index.html', content)


def new(request):
    return render(request, 'crud/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('/')

def detail(request, pk):
    article= Article.objects.get(pk=pk)

    content = {
        'article':article
    }

    return render(request, 'crud/detail.html')

def update(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        "article": article
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

def delete(request, pk):

    article = Article.objects.get(pk=pk)
    article.delete()
    
    return redirect('/crud/')



