from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from IPython import embed
from .forms import UserCustomChangeForm, UserCustomCreationForm
from django.contrib.auth import update_session_auth_hash as update_session
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


def signup(request):

    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method == "POST":
        # User model을 재설정해서 해당 폼을 사용할 수 없음.
        #그래서 새롭게 model을 설정한 폼으로 바꿈
        #form = UserCreationForm(request.POST)
        form = UserCustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        #form = UserCreationForm()
        form = UserCustomCreationForm()
        #embed()
    context = {
        'form':form,
        'label':'회원가입'
    }

    return render(request, 'accounts/signup.html', context)

def login(request):

    if request.user.is_authenticated:
        return redirect('boards:index')


    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        #embed()
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'boards:index')

    else:
        form = AuthenticationForm()
    context = {
        'form':form,
        'label':'로그인'
    }

    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect('boards:index')

def edit(request):

    if request.method == "POST":
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:

    #form = UserChangeForm()
        form = UserCustomChangeForm(instance=request.user)
    context = {
        'form':form,
        'label':'회원정보수정'

    }

    return render(request, 'accounts/auth_form.html', context)

def chg_pwd(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session(request, user)
            return redirect('accounts:adit')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
        'label':'비밀번호수정'
    }
    return render(request, 'accounts/auth_form.html', context)

def delete(request):
    if request.method == "POST":
        request.user.delete()

    return redirect('boards:index')

#Follow 로직 구현
@login_required
def follow(request, u_id):
    # 팔로우 할 우저 정보를 얻어옴.
    person = get_object_or_404(get_user_model(), id=u_id)

    #해당 유저 팔로우 목록에 접속한 유저가 있다면
    if person.followers.filter(id=request.user.id).exists():
        #팔로우 해제
        person.followers.remove(request.user)
    else:
        #팔로우
        person.followers.add(request.user)

    return redirect('boards:index')

def profile(request, name):
    person = get_object_or_404(get_user_model(), username=name)
    context = {
        'person':person
    }
    return render(request, 'accounts/profile.html', context)


    
