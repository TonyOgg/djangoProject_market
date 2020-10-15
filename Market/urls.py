from django.urls import path
from Market.views import *

urlpatterns = [
    path('', start),
    path('logged', autorise),
    path('login', login_user),
    path('logout', do_logout),
    path('ined', ined),
    path('go_to_regist', reg),
    path('regist', register),
    path('timer', ti),
    path('logisin', logvalue),
    path('emisin', emvalue)
]