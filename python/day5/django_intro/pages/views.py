from django.shortcuts import render
import random
import requests


# Create your views here.

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    # print(request)
    # print(request.path)
    # print(request.method)
    # print(request.META)
    print(request.GET)
    message = request.GET.get('message')
    message2 = request.GET.get('message2')

    context = {
            'msg':message,
            'msg2':message2
        }

    return render(request, 'pages/catch.html', context)

def lotto(request):
    return render(request, 'pages/lotto.html')

def lotto_result(request):
    count = int(request.GET.get('count'))
    lotto_num = []
    for i in range(count):
       
        lotto_num.append(random.sample(range(1,47),6))
    
    context = {
        'count':count,
        'lotto_num':lotto_num
    }
    
    return render(request, 'pages/result.html', context)

def text(request):
    return render(request, 'pages/text.html')

def text_result(request):
    text = request.GET.get('text')

    f_url = "http://artii.herokuapp.com/fonts_list"
    fonts = requests.get(f_url).text
    fonts = fonts.split('\n')
    
    font = random.choice(fonts)

    url = f"http://artii.herokuapp.com/make?text={text}&font={font}"
    res = requests.get(url).text
    print(res)
    context = {
        'res':res
    }


    return render(request, 'pages/text_result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    username = request.POST.get('name')
    pw = request.POST.get('pw')

    context = {
        'username':username,
        'pw':pw
    }

    return render(request,'pages/user_create.html', context)

def menu(request):


    return render(request,'pages/menu.html')


def subway(request):
    name = request.POST.get("name")
    date = request.POST.get("date")
    sandwitch = request.POST.get("sandwitch")
    size = request.POST.get("size")
    bread = request.POST.get("bread")
    source = request.POST.getlist("source")

    
    context = {
        'name':name,
        'date':date,
        'sandwitch':sandwitch,
        'size':size,
        'bread':bread,
        'source':source
    }
    


    return render(request, 'pages/subway.html', context)

def static_ex(request):
    return render(request, 'pages/static.html')

def index(request):
    return render(request, 'pages/index.html')          