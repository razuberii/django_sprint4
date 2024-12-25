"""
Django settings for blogicum project.

Этот файл содержит настройки для проекта Django с именем 'blogicum'.
Он был сгенерирован с помощью команды 'django-admin startproject' и использует Django версии 3.2.16.

Для получения дополнительной информации об этом файле, смотрите
https://docs.djangoproject.com/en/3.2/topics/settings/

Для полного списка настроек и их значений, смотрите
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path  # Импортируем класс Path для работы с файловыми путями

# Определяем базовую директорию проекта, чтобы удобно строить пути к файлам
BASE_DIR = Path(__file__).resolve().parent.parent  # Получаем родительскую директорию текущего файла дважды

# Быстрые настройки для разработки - не рекомендуется для продакшена

SECRET_KEY = 'django-insecure--8^bwsu-l^(yfk+)r&e!+2(wbncaem$t2btk^@z0$h3w+c8yce'

DEBUG = True  # Включение режима отладки для разработки

# Разрешенные хосты для доступа к приложению
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Локальные адреса

# Определение приложений, которые будут использоваться в проекте
INSTALLED_APPS = [
    'blog.apps.BlogConfig',  # Приложение блога
    'pages.apps.PagesConfig',  # Приложение страниц
    'django.contrib.admin',  # Административная панель Django
    'django.contrib.auth',  # Аутентификация пользователей
    'django.contrib.contenttypes',  # Поддержка типов контента
    'django.contrib.sessions',  # Поддержка сессий
    'django.contrib.messages',  # Сообщения для пользователей
    'django.contrib.staticfiles',  # Обслуживание статических файлов
    'debug_toolbar',  # Инструмент отладки
    'django_bootstrap5',  # Поддержка Bootstrap 5
]

# Путь к директории для медиафайлов (загружаемых пользователями)
MEDIA_ROOT = BASE_DIR / 'media'

# URL для доступа к медиафайлам
MEDIA_URL = 'media/'

# Определение промежуточного ПО (middleware) для обработки запросов
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Защита безопасности
    'django.contrib.sessions.middleware.SessionMiddleware',  # Обработка сессий
    'django.middleware.common.CommonMiddleware',  # Общие функции промежуточного ПО
    'django.middleware.csrf.CsrfViewMiddleware',  # Защита от CSRF-атак
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Аутентификация пользователей
    'django.contrib.messages.middleware.MessageMiddleware',  # Обработка сообщений
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Защита от Clickjacking
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # Инструмент отладки
]

# Основной файл маршрутов URL приложения
ROOT_URLCONF = 'blogicum.urls'

# Путь к директории с шаблонами
TEMPLATES_DIR = BASE_DIR / 'templates'

# Определение настроек для шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Используемый движок шаблонов
        'DIRS': [TEMPLATES_DIR],  # Директории, где будут искаться шаблоны
        'APP_DIRS': True,  # Разрешение на поиск шаблонов в директориях приложений
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Процессор контекста для отладки
                'django.template.context_processors.request',  # Процессор контекста для запросов
                'django.contrib.auth.context_processors.auth',  # Процессор контекста для аутентификации
                'django.contrib.messages.context_processors.messages',  # Процессор контекста для сообщений
            ],
        },
    },
]

# Указываем WSGI приложение для обработки запросов
WSGI_APPLICATION = 'blogicum.wsgi.application'


# Настройки базы данных

DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.sqlite3',  # Используем SQLite как базу данных
        'NAME': BASE_DIR / 'db.sqlite3',  # Путь к файлу базы данных
    }
}


# Валидация паролей

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Проверка на схожесть атрибутов пользователя
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Минимальная длина пароля
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Проверка на распространенные пароли
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Проверка на числовые пароли
    },
]


# Интернационализация (i18n)

LANGUAGE_CODE = 'ru-RU'  # Код языка по умолчанию

TIME_ZONE = 'UTC'  # Часовой пояс

USE_I18N = True  # Включение интернационализации

USE_L10N = False  # Отключение локализации форматов дат и чисел

USE_TZ = True  # Включение поддержки временных зон


# Статические файлы (CSS, JavaScript, изображения)

STATIC_URL = '/static/'  # URL для доступа к статическим файлам

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev'  # Директория для статических файлов во время разработки
]

# Тип поля первичного ключа по умолчанию

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Используем BigAutoField как тип поля первичного ключа

INTERNAL_IPS = [
    '127.0.0.1',  # Локальный IP-адрес для внутреннего использования (например, для инструмента отладки)
]

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'  # Используем "пустой" бэкенд для отправки электронной почты (для разработки)

EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'  # Путь к директории, где будут храниться отправленные электронные письма (для разработки)

CSRF_FAILURE_VIEW = 'pages.views.csrf_failure'  # Представление для обработки ошибок CSRF

LOGIN_REDIRECT_URL = 'blog:index'  # URL, на который будет перенаправлен пользователь после входа в систему

