# cqs_django/django_car_service/cars/urls.py
from django.urls import path
from . import views

app_name = "cars"  # <--- Важливо для HTMX-шаблонів

urlpatterns = [
    # 1. Сторінка, що показує список авто (GET)
    path("", views.car_list_view, name="list"),

    # 2. Endpoint для СТВОРЕННЯ авто (POST)
    path("create/", views.create_car_view, name="create"),

    # 3. Endpoint для ВИДАЛЕННЯ авто (DELETE)
    #    Ми використовуємо hx-delete, тому метод DELETE буде тут
    path("<int:car_id>/delete/", views.delete_car_view, name="delete"),
    path("qr-code/<str:license_plate>/", views.generate_qr_code_view, name="qr_code"),
]