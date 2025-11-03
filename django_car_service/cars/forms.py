# cqs_django/django_car_service/cars/forms.py
from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    """
    Форма Django, що базується на моделі Car.
    Вона автоматично валідує дані, так само як Pydantic.
    """
    class Meta:
        model = Car  # На якій моделі базується

        # Які поля показувати у формі
        fields = ["license_plate", "brand", "model"]