from django.shortcuts import render, redirect, get_object_or_404
from .forms import BoardForm, CommentForm
from .models import Board, Comment
from django.contrib.auth.decorators import login_required
from IPython import embed
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseBadRequest

# Create your views here.
def index(request):
    boards = Board.objects.all()

    # Paginator(전체리스트, 페이지당 보여지는 갯수)
    paging = Paginator(boards, 5)

    page = request.GET.get('page')
    page_list = paging.get_page(page)

    context ={
        'boards':page_list
    }
    return render(request, 'boards/index.html', context)

# @login_required
def new(request):
    # embed()
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            
            board.save()
            return redirect('boards:index')

    else:
        form = BoardForm()

    context = {
        'form':form
    }
    return render(request, 'boards/new.html', context)

def detail(request, b_id):
    board = get_object_or_404(Board, id=b_id)
    comment_form = CommentForm()

    comments = board.comment_set.all()

    person = get_object_or_404(get_user_model(), id=board.user.id)

    context = {
        'board':board,
        'comment_form':comment_form,
        'comments':comments,
        'person':person,
    }

    return render(request, 'boards/detail.html', context)

def edit(request, b_id):
    board = get_object_or_404(Board, id=b_id)

    if request.user != board.user:
        return redirect('boards:index')
        
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
    
@login_required
def delete(request, b_id):
    board = get_object_or_404(Board, id=b_id)

    if request.user != board.user:
        return redirect('boards:index')

    if request.method == "POST":
        board.delete()
        return redirect('boards:index')

    return redirect('boards:detail', board.id)

@login_required
@require_POST
def new_comment(request, b_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.board_id = b_id
        comment.user = request.user
        comment.save()
        return redirect('boards:detail', b_id)

    else:
        board = Board.objects.get(id=b_id)
        comments = board.comment_set.all()

        context = {
            'board':board,
            'comment_form':comment_form,
            'comments':comments
        }

        return render(request, 'boars/detail.html', context)

@login_required
@require_POST
def del_comment(request, c_id):
    comment = get_object_or_404(Comment, id=c_id)
    board_id = comment.board_id
    if request.user == comment.user:
        comment.delete()

    return redirect('boards:detail', board_id)


@require_POST
@login_required
def like(request, b_id):
    board = get_object_or_404(Board, pk=b_id)

    if request.is_ajax():
        # if board.like_users.filter(id).exists()
        if request.user in board.like_users.all():
            board.like_users.remove(request.user)
            liked = False
        else:
            board.like_users.add(request.user)
            liked = True


        context = {
            'liked':liked,
            'count':board.like_users.count()
        }

        return JsonResponse(context)
    else:
        return HttpResponseBadRequest

    #return redirect('boards:index')

def search(request):
    text = request.GET.get('search')

    results = Board.objects.filter(title__contain=text)

    context={
        'results':results
    }

    return render(request,'boards/search.html', context)



    
