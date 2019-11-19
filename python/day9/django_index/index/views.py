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
    sur = que.comment_set.all()
    context = {
        'que':que,
        'survey':sur
    }

    return render(request, 'index/detail.html', context)

def update(request, que_id):
    que = Question.objects.get(id=que_id)

    if request.method == "POST":
        que.question = request.POST.get('question')
        que.save()
        return redirect('index:detail', que.id)
    else:
        return render(request, 'index/update.html', {'que':que})

def delete(request, que_id):
    que = Question.objects.get(id=que_id)

    if request.method == "POST":
        que.delete()
        return redirect('index:index')
    else:
        return redirect('index:detail', que_id)

def survey(request, que_id):
    question = Question.objects.get(id=que_id)

    if request.method == "POST":
        survey = request.POST.get('survey')

        sur = Comment()
        sur.survey = survey
        sur.question = question
        sur.save()
        
        return redirect('index:detail', que_id)

def vote(request, sur_id):
    survey = Comment.objects.get(id=sur_id)

   