from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from IPython import embed

def signup(request):

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
        'form':form
    }

    return render(request, 'accounts/signup.html', context)

def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        #embed()
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')

    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }

    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect('boards:index')

    
