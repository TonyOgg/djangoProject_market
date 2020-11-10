from django.urls import path
from Market.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', start),
    path('loginning', autorise),
    path('do_login', login_user),
    path('logouting', logout_user),
    path('registration', registration),
    path('do_registration', registrate_user),
    path('timer', ti),
    path('logisin', logvalue),
    path('emisin', emvalue),
    path('select_rus', language_ru),
    path('select_en', language_en),
    path('cars', search_car),
    path('add', to_add_auto, name="add_auto"),
    path('adding', adding, name="adding"),
    path('car_description', to_car_desc),
    path('finish', to_finish)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)