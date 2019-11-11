from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
from faker import Faker
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def age(request, age):
    context = {
        'age' : age
        }
    return render(request, 'age.html', context)

def squared(request, squared):

    context = {
        'squared':squared**2
        }
    return render(request, 'squared.html', context)

def plus(request, num, num2):

    result = {
        'result':num + num2
        }
    return render(request, 'num.html', result)

def minus(request, num, num2):

    result = {
        'result':num - num2
        }
    return render(request, 'num.html', result)

def division(request, num, num2):

    result = {
        'result':num / num2
        }
    return render(request, 'num.html', result)

def mult(request, num, num2):

    result = {
        'result':num * num2
        }
    return render(request, 'num.html', result)


def profile(request, name, age):

    list_1 = ['말 많은', '푸른', '어두운', '웅크린', '조용한', '용감한', '지혜로운']
    list_2 = ['늑대', '태양','양', '매', '황소', '불꽃']
    list_3 = ['와 함께 춤을', '의 기상', '은 그림자 속에', '의 환생', '의 죽음', '아래에서', '을 보라', '의 그림자']
    l1 = random.choice(list_1)
    l2 = random.choice(list_2)
    l3 = random.choice(list_3)
    indian = l1 + l2 + l3

    #로또
    num = range(1,47) # range(시작값, 끝값) : 시작값<= x <끝값  범위의 숫자를 List 형태로 반환함.
    lotto = sorted(random.sample(num, 6))

    l_num = [str(l) for l in lotto ]


    
   
    result = {
        'name':name,
        'age':age,
        'indian': indian,
        'lotto': ", ".join(l_num)

        }
    return render(request, 'profile.html', result)


def faker(request, name):
   
    fake = Faker('ko_KR')
    job = fake.job()
    adress = fake.address()

    context = {
        'name':name,
        'job':job,
        'adress':adress

    }
    return render(request, 'faker.html', context)



def image(request):

    num = random.choice(range(1, 300))
    url = f"https://picsum.photos/id/{num}/200/300"

    context = {
        'url':url
    }

    return render(request, 'image.html', context)

def dtl(request):
    foods = ["짜장면","탕수육","짬뽕","양장피","군만두","고추잡채","볶음밥"]
    my_sentence = 'life is short, you need pythin'
    messages = ['apple', 'banana', 'cucumber','mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        "foods":foods,
        "my_sentence":my_sentence,
        "messages":messages,
        "timenow":datetimenow,
        "empty_list":empty_list
    }

    return render(request, 'dtl.html',context)


def birth(request):
    today = datetime.now()

    if today.month == 6 and today.date ==12:
        res = True
    else:
        res = False

    birth = datetime(today.year+1, 7, 22)

    d_day = abs((today-birth).days)


    context = {
        'result':res,
        'd_day':d_day
    }

    return render(request, 'birth.html', context)






