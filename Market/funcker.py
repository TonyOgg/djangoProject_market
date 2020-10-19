""" Its need to delete """
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Market.models import Client
import re
import time
import random
import unittest
from unittest.mock import Mock

def mocker(request):
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

def unders(first, last):
    try:
        a = random.randint(0, 100) / first * last
    except ValueError:
        return 'Zero division'

    if mocker(request):
        return 'ok'
    else:
        return 'Error'

