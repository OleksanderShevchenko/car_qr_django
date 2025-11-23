# cqs_django/django_car_service/pages/views.py
from django.http import HttpResponse
from django.views.decorators.http import require_POST
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


@require_POST  # Дозволяє тільки POST-запити
def send_sms_view(request, license_plate: str):
    """
    Заглушка для відправки SMS. Повертає простий HTML-рядок.
    """
    message = request.POST.get("message", "")
    print(f"Імітація відправки SMS для авто {license_plate} з повідомленням: '{message}'")

    # Повертаємо той самий HTML-рядок, що й у FastAPI
    return HttpResponse(
        content='<span class="text-green-600">✓ Повідомлення надіслано!</span>'
    )


# "Переклад" POST /public/initiate-call
@require_POST
def initiate_call_view(request):
    """
    Заглушка для ініціації дзвінка.
    Повертає HTML-фрагмент 'call_success.html'.
    """
    license_plate = request.POST.get("license_plate", "")
    print(f"Initiating call to owner of {license_plate}")

    # Переконуємося, що файл лежить у 'templates/partials/'
    return render(
        request, "partials/call_success.html", {"license_plate": license_plate}
    )