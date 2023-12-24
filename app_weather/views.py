from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from weather_api import current_weather

def my_view(request):
    if request.method == "GET":
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        if lat and lon:
            weather_data = current_weather(lat,lon)
        else:
            weather_data = current_weather(59.93, 30.31)
        data = current_weather(59.93, 30.31) # Результат работы функции current_weather
        # А возвращаем объект JSON. Параметр json_dumps_params используется, чтобы передать ensure_ascii=False
        # как помните это необходимо для корректного отображения кириллицы
        return JsonResponse(weather_data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})