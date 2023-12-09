from django.shortcuts import render
import requests
from django.http import JsonResponse
from datetime import datetime
# Create your views here.
def current_weather(lat=59.93, lon=30.31):

    token = 'cba50521-c49a-4a1d-8c3d-bf2c40320923'  # Вставить ваш токен
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"  # Если вдруг используете тариф «Погода на вашем сайте»
    # то вместо forecast используйте informers. url = f"https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}"
    headers = {"X-Yandex-API-Key": f"{token}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    result = {
        'city': data['geo_object']['locality']['name'],
        # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
        'time': datetime.fromtimestamp(data['fact']['uptime']).strftime("%H:%M"),
        # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
        'temp': data['fact']['temp'],  # Реализовать вычисление температуры из данных полученных от API
        'feels_like_temp': data['fact']['feels_like'],
        # Реализовать вычисление ощущаемой температуры из данных полученных от API
        'pressure': data['fact']['pressure_mm'],  # Реализовать вычисление давления из данных полученных от API
        'humidity': data['fact']['humidity'],  # Реализовать вычисление влажности из данных полученных от API
        'wind_speed': data['fact']['wind_speed'],  # Реализовать вычисление скорости ветра из данных полученных от API
        'wind_gust': data['fact']['wind_gust'],
        # Реализовать вычисление скорости порывов ветка из данных полученных от API
        #'wind_dir': DIRECTION_TRANSFORM.get(data['fact']['wind_dir']),
        # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
    }
    return result

def weather_view(request):
    if request.method == "GET":
        data = current_weather()
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})


