from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Question, Comment

# Create your views here.

def index(request):
    questions = Question.objects.all()

    context ={
        'questions':questions
    }

    return render(request, 'index/index.html', context)

def new(request):

    if request.method == "POST":
        question = Question(question=request.POST.get('question'))
        question.save()
        return redirect('index:index')
    else:
        return render(request, 'index/new.html')


def detail(request, que_id):
    que = Question.objects.get(id=que_id)

    context = {
        'que':que,
    }

    return render(request, 'index/detail.html', context)

def update(request, que_id):
    que = Question.objects.get(id=que_id)

    if request.method == "POST":
        que.question = request.POST.get('question')
        que.save()
        return redirect('index:detail', que.id)