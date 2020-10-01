from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Market.models import Client
import re


def start(request):
    return render(request, 'log_in.html')

def autorise(request):
    return render(request, 'autorised_page.html')

def login_user(request):
    context = {
        'try': 'Username or password is wrong. Try again.',
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
        return HttpResponseRedirect('ined')

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Ты не залогинен')

def ined(request):
    context = {
        'name': request.user.username
    }
    if request.user.is_authenticated:
         return render(request, 'log_outed.html', context)
    else:
        return HttpResponseRedirect('/')

def reg(request):
    return render(request, 'registration_page.html')

def register(request):
    context = {
        'error': 'Username or e-mail address is invalid!'
    }
    a = request.POST['login']
    b = request.POST['email']
    if (re.match("^\w+$", a) is not None) and \
            (re.match("^[\d\w]+@\w+.\w+$", b) is not None):
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
        return HttpResponseRedirect('ined')
    else:
        return render(request, 'registration_page.html', context)
