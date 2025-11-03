from django.contrib import admin
from .models import Car

# Реєструємо модель Car в адмін-панелі
admin.site.register(Car)