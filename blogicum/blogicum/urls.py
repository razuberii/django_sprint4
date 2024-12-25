"""blogicum URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static  # Импортируем функцию для обработки статических файлов
from django.contrib import admin  # Импортируем административный интерфейс Django
from django.urls import include, path  # Импортируем функции для маршрутизации URL
from django.conf import settings  # Импортируем настройки проекта

# Список маршрутов URL для приложения
urlpatterns = [
    path('admin/', admin.site.urls),  # URL для административной панели Django
    path('', include('blog.urls')),  # Включаем маршруты из приложения 'blog'
    path('pages/', include('pages.urls')),  # Включаем маршруты из приложения 'pages'
    path('auth/', include('django.contrib.auth.urls')),  # Включаем маршруты аутентификации от Django
    path('auth/registration/', include('users.urls')),  # Включаем маршруты регистрации пользователей
]

# Обработчик ошибок 403 (доступ запрещен)
handler403 = 'pages.views.csrf_failure'

# Обработчик ошибок 404 (страница не найдена)
handler404 = 'pages.views.page_not_found'

# Обработчик ошибок 500 (внутренняя ошибка сервера)
handler500 = 'pages.views.internal_error'

# Если проект работает в режиме отладки
if settings.DEBUG:
    import debug_toolbar  # Импортируем инструмент отладки
    # Добавляем маршруты из приложения debug_toolbar к списку urlpatterns
    urlpatterns += (path('debug/', include(debug_toolbar.urls)),)

# Обработка статических файлов и медиафайлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Настройка доступа к медиафайлам
