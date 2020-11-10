import re
from datetime import datetime
import time
import requests
import json
import random

from Market.forms import CarForm
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext as _, activate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from Market.models import *


# select language

from django.utils import translation
def language_en(request):
    cur_language = translation.get_language()
    print(cur_language)
    translation.activate('en')
    cur_language = translation.get_language()
    print(cur_language)
    return render(request,
                  'start_page_support.html')



def language_ru(request):
   # activate('ru')
    cur_language = translation.get_language()
    print(cur_language)
    translation.activate('ru')
    cur_language = translation.get_language()
    print(cur_language)
    return render(request,
                  'start_page_support.html')


# start page entering

def start(request):
    # with translation.override('en'):
        return render(request, 'start_page_support.html')

# autorisation

def autorise(request):
    return render(request, 'autorised_page.html')

# do loginning

def login_user(request):
    context = {
        'try': 'Username or password is wrong! Try again!',
        'name': request.user.username
    }
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, 'autorised_page.html', context)
    else:
        login(request, user)
        return HttpResponseRedirect('/')

# do_logouting

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Ты не залогинен')


# функция обмена валюты
#
# def get_currency():
#     response = requests.get(
#         'https://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDATE=2020-10-13&endDate=2020-10-20'
#     )
#     data = json.loads(response.text)
#     sum = 0
#     for cur in data:
#         sum += float(cur["Cur_OfficialRate"])
#     average = sum / 7
#     context = {
#         'item1': average
#     }



# registration_page

def registration(request):
    return render(request, 'registration_page.html')

# registration user

def registrate_user(request):
    context = {
        'error': 'Username or e-mail address is invalid!'
    }
    a = request.POST['login']
    b = request.POST['email']
    if (re.match("^\w+$", a) is not None) and \
            (re.match("^[\w\d]+@\w{4,}\.\w{2,}$", b) is not None):
        user = User.objects.create_user(
            username=request.POST['login'],
            password=request.POST['password'],
            first_name=request.POST['fname'],
            last_name=request.POST['sname'],
            email=request.POST['email']
        )
        client = Client(user=user, address='Minsk')
        client.save()
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'registration_page.html', context)


def ti(request):
    response = {
        'message': request.POST['a'] + time.asctime()
    }
    return JsonResponse(response)


def logvalue(request):
    response = {
        'message': 1
    }
    a = request.POST['lg']
    c = User.objects.filter(username=a)
    if len(c) != 0:
        return JsonResponse(response)
    else:
        response['message'] = 0
        return JsonResponse(response)


def emvalue(request):
    response = {
        'message': 1
    }
    a = request.POST['emkey']
    c = User.objects.filter(email=a)
    if len(c) != 0:
        return JsonResponse(response)
    else:
        if (re.match("^[\w\d]+@\w{4,}\.\w{2,}$", a) is None):
            response['message'] = 2
            return JsonResponse(response)
        else:
            response['message'] = 0
            return JsonResponse(response)

# search cars

def search_car(request):
    if request.GET.get('ID'):
        car = Car.objects.filter(is_new=True).order_by('-created')
        return render(request, 'car_page.html', {'car': car, "old": 2})
    elif request.GET.get('PD'):
        car = Car.objects.filter(is_new=False).order_by('-created')
        return render(request, 'car_page.html', {'car': car, "old": 1})

# car description

def to_car_desc(request):
    car = Car.objects.get(id=request.GET.get('carId'))
    return render(request, 'description_car.html', {'car': car})


def to_add_auto(request):
    form = CarForm
    return render(request, 'adding_automobile.html', {'form': form})

# adding auto in catalog

def adding(request):
    warning = ''
    context = {
        'succsesful': "Your car has been successfuly added in our catalog!"
    }
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'adding_automobile.html', context)
        else:
            warning = "Some of dates is wrong. Try again"
    form = CarForm
    context = {
        'form': form,
        'warning': warning
    }
    return render(request, 'adding_automobile.html', context)

# \w([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$" regular for email

