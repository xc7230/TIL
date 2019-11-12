from django.shortcuts import render
import random
import requests

# Create your views here.

def throw(request):
    return render(request, 'throw.html')

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

    return render(request, 'catch.html', context)

def lotto(request):
    return render(request, 'lotto.html')

def lotto_result(request):
    count = int(request.GET.get('count'))
    lotto_num = []
    for i in range(count):
       
        lotto_num.append(random.sample(range(1,47),6))
    
    context = {
        'count':count,
        'lotto_num':lotto_num
    }
    
    return render(request, 'result.html', context)

def text(request):
    return render(request, 'text.html')

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


    return render(request, 'text_result.html', context)