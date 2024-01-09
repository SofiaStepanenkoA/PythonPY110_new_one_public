from django.urls import path
from .views import wishlist_view#  TODO Импортируйте ваше представление
from .views import wishlist_add_json, wishlist_del_json, wishlist_json, remove_from_wishlist,wishlist_remove_view

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist_view, name='wishlist_view'),  # TODO Зарегистрируйте обработчик
    path('api/add/<str:id_product>', wishlist_add_json),
    path('api/del/<str:id_product>', wishlist_del_json),
    path('api/', wishlist_json),
    path('remove/<str:id_product>', wishlist_remove_view, name="remove_from_wishlist"),
]