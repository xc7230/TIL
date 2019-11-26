from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from IPython import embed

def signup(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = UserCreationForm()
        #embed()
    context = {
        'form':form
    }

    return render(request, 'accounts/signup.html', context)
