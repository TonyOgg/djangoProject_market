from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

def start(request):
    return render(request, 'enter_page.html')

def login_user(request):
    context = {
        'isin': request.user.is_authenticated
    }
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, 'enter_page.html', context)
    else:
        login(request, user)
        return HttpResponseRedirect('start')

def main(request):
    return render(request, 'main_page.html')

