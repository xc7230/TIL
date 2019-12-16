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
    
def survey_edit(request, sur_id):
    # 설문(자식) 데이터를 가져오는 부분
    survey = Choice.objects.get(id=sur_id)

    # print(f'survey_edit method is {request.method}')
    # POST 방식일 때만 수정가능 하게
    if request.method == "POST":
        text = request.POST.get('survey')
        survey.survey = text
        survey.save()
        # 이미 부모정보는 저장이 되어 있기에 수정 부분만 저장해주면 됨.
        # 자식 인스턴스에서 부모의 정보를 가져오기 위해서는 
        return redirect('survey:detail', survey.question_id)
    else:
        # GET 방식일때는 폼을 보여줌.
        context = {
            "survey": survey
        }
        return render(request, 'survey/sur_edit.html', context)

# 설문 항목 삭제하는 부분
def survey_del(request, sur_id):
    survey = Choice.objects.get(id=sur_id)

    # 데이터를 직접 변경하기에 POST 일때만 동작하게!
    if request.method == "POST":
        survey.delete()
    
    return redirect('survey:detail', survey.question_id)

# 설문 항목에서 투표하기를 눌렀을때 처리 하는 곳

def vote(request, sur_id):
    survey = Comment.objects.get(id=sur_id)

    if request.method == "POST":
         survey.votes += 1
         survey.save()
    return redirect('survey:detail', survey.question_id)


   