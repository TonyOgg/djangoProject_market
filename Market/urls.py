from django.urls import path
from Market.views import *

urlpatterns = [
    path('home', start),
    path('login', login_user),
    path('start', main)
]