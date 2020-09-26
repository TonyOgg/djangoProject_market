from django.urls import path
from Market.views import *

urlpatterns = [
    path('home', start)
]