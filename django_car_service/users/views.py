# cqs_django/django_car_service/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm  # Ми створимо це у 'users/forms.py'


def register_view(request):
    """
    "Переклад" GET /pages/register та POST /pages/register
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматичний логін
            return redirect("cars:list")  # Редірект в кабінет
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    """
    "Переклад" GET /pages/login та POST /pages/login
    """
    if request.method == "POST":
        # 'username' - це назва поля, але ми логінимось по email
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("cars:list")  # Редірект в кабінет
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    """
    Нова функція для кнопки "Вийти"
    """
    logout(request)
    return redirect("pages:welcome")  # Редірект на головну