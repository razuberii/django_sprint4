"""
ASGI config for blogicum project.

This module configures the ASGI (Asynchronous Server Gateway Interface) settings for the Django project named 'blogicum'.
It exposes the ASGI callable as a module-level variable named application.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os  # Импортируем модуль os для работы с операционной системой

from django.core.asgi import get_asgi_application  # Импортируем функцию для получения ASGI приложения из Django

# Устанавливаем переменную окружения 'DJANGO_SETTINGS_MODULE' на значение 'blogicum.settings'
# Это необходимо для того, чтобы Django знал, где искать настройки проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')

# Получаем ASGI приложение, которое будет использоваться для обработки входящих запросов
application = get_asgi_application()
