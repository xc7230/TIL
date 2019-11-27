from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from IPython import embed
from .forms import UserCustomChangeForm
from django.contrib.auth import update_session_auth_hash as update_session

def signup(request):

    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = UserCreationForm()
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

    return render(request, 'accounts/auth_form.html', context)

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


    
