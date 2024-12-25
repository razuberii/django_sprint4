"""
WSGI config for blogicum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os  # Импортируем модуль os для взаимодействия с операционной системой

from django.core.wsgi import get_wsgi_application  # Импортируем функцию для получения WSGI-приложения Django

# Устанавливаем переменную окружения 'DJANGO_SETTINGS_MODULE' в значение 'blogicum.settings'
# Это указывает Django, какой файл настроек использовать для конфигурации проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')

# Получаем WSGI-приложение Django, которое будет использоваться веб-сервером для обработки запросов
application = get_wsgi_application()

