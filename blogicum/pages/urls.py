from django.urls import path  # Импортируем функцию path для определения URL-шаблонов

from . import views  # Импортируем представления (views) из текущего пакета

app_name = 'pages'  # Задаем пространство имен для приложения 'pages', чтобы избежать конфликтов имен

# Определяем список URL-шаблонов для приложения 'pages'
urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),  # URL для страницы "О нас", связанный с представлением AboutView
    path('rules/', views.RulesView.as_view(), name='rules'),  # URL для страницы "Правила", связанный с представлением RulesView
]
