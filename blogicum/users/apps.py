from django.apps import AppConfig  # Импортируем класс AppConfig для настройки приложения Django


class UsersConfig(AppConfig):  # Определяем класс конфигурации приложения "Users"
    default_auto_field = 'django.db.models.BigAutoField'  # Указываем тип поля для автоматического увеличения идентификаторов (по умолчанию BigAutoField)
    name = 'users'  # Задаем имя приложения, которое будет использоваться в проекте
