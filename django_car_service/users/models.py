# cqs_django/django_car_service/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """
    Кастомна модель Користувача, що розширює вбудовану Django User.
    Вона вже має: id, username, first_name, last_name, email, password (hashed), date_joined.
    """

    # 1. Перевизначаємо email, щоб зробити його унікальним, як у вашому проекті
    email = models.EmailField(
        unique=True,
        max_length=254,
        verbose_name="email address"
    )

    # 2. Додаємо ваші кастомні поля
    phone_number = models.CharField(max_length=20, unique=True)
    show_phone_number = models.BooleanField(default=False)

    # 3. Використовуємо поле 'date_joined' з AbstractUser 
    #    замість вашого 'created_at'. Вони роблять те саме.

    # 4. 'hashed_password' керується Django автоматично.

    # 5. Вказуємо Django, що ми хочемо використовувати 'email' для входу
    USERNAME_FIELD = "email"

    # 6. Вказуємо 'username' як обов'язкове поле (для адмінки)
    #    Хоча ми логінимось по email, 'username' все ще корисний.
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email