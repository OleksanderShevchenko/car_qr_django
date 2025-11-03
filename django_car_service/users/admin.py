from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Реєструємо нашу кастомну модель User
# Використання UserAdmin дає нам крутий інтерфейс для керування паролями
admin.site.register(User, UserAdmin)