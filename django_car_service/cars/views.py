# cqs_django/django_car_service/cars/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import qrcode
import io
from django.http import HttpResponse, HttpResponseForbidden, StreamingHttpResponse

from .models import Car
from .forms import CarForm


# Це "переклад" вашого @router.get("/", ...)
@login_required  # <-- Аналог Depends(get_current_user)
def car_list_view(request):
    """
    Показує повну сторінку зі списком авто
    (і формою для додавання нового).
    """
    # Аналог crud.get_user_cars()
    cars = Car.objects.filter(owner=request.user)

    # Створюємо порожню форму для відправки у шаблон
    form = CarForm()

    context = {
        "cars": cars,
        "form": form
    }
    return render(request, "cabinet.html", context)


# Це "переклад" вашого @router.post("/", ...)
@login_required
@require_POST  # Дозволяє тільки POST-запити
def create_car_view(request):
    """
    Обробляє POST-запит (від HTMX) для створення нового авто.
    Повертає HTML-фрагмент з новим рядком для таблиці.
    """
    form = CarForm(request.POST)  # <-- Django Form валідує дані

    if form.is_valid():
        # Створюємо, але ще не зберігаємо в БД
        car = form.save(commit=False)

        # Додаємо власника (аналог owner_id=current_user.id)
        car.owner = request.user
        car.save()

        # УСПІХ: Повертаємо HTML-фрагмент для HTMX
        return render(request, "partials/car_row.html", {"car": car})
    else:
        # ПОМИЛКА: Повертаємо форму з помилками валідації
        return render(request, "partials/car_form.html", {"form": form})


# Це "переклад" вашого @router.delete("/{car_id}", ...)
@login_required
def delete_car_view(request, car_id: int):
    """
    Обробляє DELETE-запит від HTMX.
    Видаляє авто і повертає порожню відповідь (200 OK).
    """
    # Аналог crud.get_car_by_id()
    car = get_object_or_404(Car, id=car_id)

    # Аналог перевірки if db_car.owner_id != current_user.id
    if car.owner != request.user:
        # Повертаємо 403 (Forbidden)
        return HttpResponseForbidden()

    car.delete()

    # HTMX очікує 200 OK, щоб видалити елемент з DOM.
    return HttpResponse(status=200)


@login_required
def generate_qr_code_view(request, license_plate: str):
    """
    Генерує QR-код для авто, що належить поточному користувачу.
    """
    # car = get_object_or_404(Car, license_plate=license_plate)

    # Оптимізована перевірка, що авто належить юзеру
    car = get_object_or_404(Car,
                            license_plate=license_plate,
                            owner=request.user)

    # Формуємо URL
    public_url = request.build_absolute_uri(
        f"/public/cars/{car.license_plate}"  # Ми створимо цей /public/ роут пізніше
    )

    # Генеруємо QR-код
    qr_img = qrcode.make(public_url)
    buffer = io.BytesIO()
    qr_img.save(buffer, format="PNG")
    buffer.seek(0)

    return StreamingHttpResponse(buffer, content_type="image/png")