# cqs_django/django_car_service/pages/views.py
from django.shortcuts import render
from cars.models import Car  # Імпортуємо модель з іншого "додатку"


def welcome_page_view(request):
    """
    Показує сторінку 'welcome.html'
    """
    return render(request, "welcome.html")


def search_page_view(request):
    """
    "Переклад" GET /pages/ (показує index.html)
    """
    return render(request, "index.html")


def search_car_htmx_view(request):
    """
    "Переклад" логіки пошуку HTMX (з вашого /public/search)
    """
    license_plate = request.POST.get("license_plate", "").upper()

    # Використовуємо Django ORM. 'select_related' - аналог 'selectinload'
    car = Car.objects.select_related('owner').filter(license_plate=license_plate).first()

    if not car:
        context = {"detail": "Автомобіль з таким номером не знайдено."}
    else:
        context = {"car": car}

    # Повертаємо HTML-фрагмент
    return render(request, "partials/car_result.html", context)