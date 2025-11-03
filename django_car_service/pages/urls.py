# cqs_django/django_car_service/pages/urls.py
from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    # Головна сторінка
    path("", views.welcome_page_view, name="welcome"),
    # Сторінка пошуку
    path("search/", views.search_page_view, name="search"),
    # HTMX endpoint для пошуку
    path("htmx/search/", views.search_car_htmx_view, name="htmx_search"),
]