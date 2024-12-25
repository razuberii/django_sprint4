from django.urls import path  # Импортируем функцию path для определения маршрутов URL в Django

from . import views  # Импортируем views из текущего приложения для использования представлений

# Определяем список маршрутов URL для приложения
urlpatterns = [
    path('', views.UserCreateView.as_view(), name='registration'),  # Указываем маршрут для корневого URL, который вызывает представление UserCreateView, 
    # и задаем ему имя 'registration' для удобства ссылки на него в других частях приложения
]
