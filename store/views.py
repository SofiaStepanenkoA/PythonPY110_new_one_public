from django.http import JsonResponse
from .models import DATABASE
from django.http import HttpResponse,HttpResponseNotFound

def products_view(request):
    if request.method == "GET":
        id = request.GET.get('id')
        if id :
            if id in DATABASE:
                return JsonResponse(DATABASE[id], json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})
            else:
                return HttpResponseNotFound('Данного продукта нет в базе данных')
        else:
            return  JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})


def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ


def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
            for data in DATABASE.values():
                if data['html'] == page:  # Если значение переданного параметра совпадает именем html файла

                    with open (f'store/products/{page}.html','r', encoding="utf-8") as f:
                        data = f.read()
                        return HttpResponse(data)
        elif isinstance(page, int):
            if str(page) in DATABASE:
                with open(f'store/products/{DATABASE[str(page)]["html"]}.html', 'r', encoding="utf-8") as f:
                    data = f.read()
                return HttpResponse(data)

        # Если за всё время поиска не было совпадений, то значит по данному имени нет соответствующей
        # страницы товара и можно вернуть ответ с ошибкой HttpResponse(status=404)
        return HttpResponse(status=404)



