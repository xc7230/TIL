from django.shortcuts import render
from boards.models import Subway

# Create your views here.

def index(request):
    return render(request, "boards/index.html")


def menu(request):


    return render(request,'boards/menu.html')


def subway(request):
    name = request.POST.get("name")
    date = request.POST.get("date")
    sandwitch = request.POST.get("sandwitch")
    size = request.POST.get("size")
    bread = request.POST.get("bread")
    source = request.POST.getlist("source")

    Subway.objects.create(name=name,date=date,sandwitch=sandwitch,size=size,bread=bread,source=source)

    result = Subway.objects.all()

    context = {
        'name':name,
        'date':date,
        'sandwitch':sandwitch,
        'size':size,
        'bread':bread,
        'source':source,
        'result':result
    }


    return render(request, 'boards/subway.html', context)

def result_sub(request, number):
    result = Subway.objects.filter(id=number)

    context = {
        'result':result
    }
    return render(request, 'boards/result_sub.html', context)
