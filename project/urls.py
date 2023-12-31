from random import random
from django.contrib import admin
from django.urls import path, include
from app_datetime.views import datetime_view
from app_weather.views import my_view
from store.views import products_view
from store.views import shop_view
from django.http import HttpResponse
from wishlist.views import wishlist_view

def random_view(request):
    if request.method == "GET":
        data = random()
        return HttpResponse(data)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('random/',random_view),
    path('datetime/', datetime_view),
    path('', include('app_weather.urls')),
    path('', include('store.urls')),
    path('login/', include('app_login.urls')),
    path('wishlist/', include('wishlist.urls')),

]