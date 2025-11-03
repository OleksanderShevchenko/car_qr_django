# cqs_django/django_car_service/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Додаємо наші кастомні поля до форми
        fields = ("email", "username", "first_name", "last_name", "phone_number", "show_phone_number")