from django.shortcuts import render, redirect, get_object_or_404
from .forms import BoardForm
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()

    context ={
        'boards':boards
    }
    return render(request, 'boards/index.html', context)

def new(request):
    if request.user.is_authenticated:
        return redirect('boards:index')


    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            return redirect('boards:index')

    else:
        form = BoardForm()

    context = {
        'form':form
    }
    return render(request, 'boards/new.html', context)

def detail(request, b_id):
    board = get_object_or_404(Board, id=b_id)

    context = {
        'board':board
    }

    return render(request, 'boards/detail.html', context)

def edit(request, b_id):
    board = get_object_or_404(Board, id=b_id)


    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save()
            return redirect('boards:detail', board.id)
    
    else:
        form = BoardForm(instance=board)

    context = {
        'form':form
    }

    return render(request,'boards/edit.html', context)

def delete(request, b_id):
    board = get_object_or_404(Board, id=b_id)

    if request.method == "POST":
        board.delete()
        return redirect('boards:index')

    return redirect('boards:detail', board.id)
